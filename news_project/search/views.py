from django.shortcuts import render
import requests
from django.views.generic.base import View
from jsonview.decorators import json_view
from embedly import Embedly
import nltk
from readability.readability import Readability
from datetime import datetime
from articles.models import Article, Source
from django.forms.models import model_to_dict
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
import tldextract
from django.core import serializers

nltk.download('punkt')

client = Embedly("ffdea8be9a1c410da69b9f74922ff9dc")


# Create your views here.

class GradeLevelView(View):
    
    def get(self, request, *args, **kwargs):
        level = 0
        if "level" in request.GET:
            level = request.GET['level']
        elif "level" in kwargs:
            level = kwargs['level']
        print level
        level_high = int(level) + 1
        level_low = int(level) - 1
        articles = Article.objects.filter(flesch_kincaid__lte=level_high,
                                          flesch_kincaid__gte=level_low)
        return HttpResponse(

            json.dumps([a.json_data() for a in articles],
                       cls=DjangoJSONEncoder),
            mimetype='application/json')

class GoogleNewsView(View):
    
    def get(self, request):
        return_val = []
        query = request.GET['query']
        payload = {'v': '1.0', 'q': query}
        r = requests.get("https://ajax.googleapis.com/ajax/services/search/news", params=payload)
        data = r.json()
        # cursor = data['responseData']['cursor']
        # estimated_results = cursor['estimatedResultCount']
        articles = data['responseData']['results']
        parsed_articles = parse_articles(articles)
        for pub, domain, title, url, date in parsed_articles:
            old = Article.objects.filter(title=title, source__domain=domain)
            if old.exists():
                return_val.append(old.first())
            else:
                processed = client.extract(url)
                if processed['content'] is not None:
                    clean_content = nltk.clean_html(processed['content'])
                    rd = Readability(clean_content)
                    source, _ = Source.objects.get_or_create(domain=domain, defaults={'name': pub})
                    article = Article(source=source,
                                            title=title,
                                            content=processed['content'],
                                            clean_content=clean_content,
                                            url=url,
                                            ari=rd.ARI(),
                                            flesch=rd.FleschReadingEase(),
                                            flesch_kincaid=rd.FleschKincaidGradeLevel(),
                                            gunning_fog=rd.GunningFogIndex(),
                                            smog_index=rd.SMOGIndex(),
                                            coleman_liau_index=rd.ColemanLiauIndex(),
                                            lix=rd.LIX(),
                                            rix=rd.RIX())
                    article.save()
                    return_val.append(article)

        return HttpResponse(
            json.dumps([a.json_data() for a in return_val],
                       cls=DjangoJSONEncoder),
            mimetype='application/json')


def parse_articles(articles):
    all_articles = [item for article in map(get_related, articles) for item in article]
    return map(article_data, all_articles)

def get_related(article):
    if "relatedStories" in article.keys():
        related = article['relatedStories']
        related.append(article)
        return related
    else:
        return [article]

def article_data(article):
    if article['language'] == "en":
        domain_parts = tldextract.extract(article['unescapedUrl'])
        domain = '.'.join(domain_parts[1:])
        return (article['publisher'],
                domain,
                article['titleNoFormatting'],
                article['unescapedUrl'],
                article['publishedDate'])

