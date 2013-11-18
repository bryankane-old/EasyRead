from django.db import models
import nltk
nltk.download('punkt')

class Source(models.Model):
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='sources', blank=True, null=True)


class Article(models.Model):
    source = models.ForeignKey(Source)
    title = models.CharField(max_length=255)
    content = models.TextField()
    clean_content = models.TextField(blank=True, null=True)
    url = models.URLField(max_length=255)
    timestamp = models.DateTimeField(blank=True, null=True)

    # Reading levels
    ari = models.DecimalField(max_digits=12, decimal_places=6)
    flesch = models.DecimalField(max_digits=12, decimal_places=6)
    flesch_kincaid = models.DecimalField(max_digits=12, decimal_places=6)
    gunning_fog = models.DecimalField(max_digits=12, decimal_places=6)
    smog_index = models.DecimalField(max_digits=12, decimal_places=6)
    coleman_liau_index = models.DecimalField(max_digits=12, decimal_places=6)
    lix = models.DecimalField(max_digits=12, decimal_places=6)
    rix = models.DecimalField(max_digits=12, decimal_places=6)

    class Meta:
        unique_together = ("source", "title")

    def json_data(self):
        if self.clean_content is None:
            self.clean_content = nltk.clean_html(self.content)
        src = self.source
        return {
            "id": self.id, 
            "source": src.name,
            "domain": src.domain,
            "title": self.title,
            "content": self.content,
            "clean_content": self.clean_content,
            "url": self.url,
            "timestamp": self.timestamp,
            "levels": {
                "ari": self.ari,
                "flesch": self.flesch,
                "flesch_kincaid": self.flesch_kincaid,
                "gunning_fog": self.gunning_fog,
                "smog_index": self.smog_index,
                "coleman_liau_index": self.coleman_liau_index,
                "lix": self.lix,
                "rix": self.rix
            }
        }
