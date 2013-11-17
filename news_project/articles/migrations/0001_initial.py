# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table(u'articles_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source', self.gf('django.db.models.fields.TextField')()),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('ari', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
            ('flesch', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
            ('flesch_kincaid', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
            ('gunning_fog', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
            ('smog_index', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
            ('coleman_liau_index', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
            ('lix', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
            ('rix', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
        ))
        db.send_create_signal(u'articles', ['Article'])

        # Adding unique constraint on 'Article', fields ['source', 'title']
        db.create_unique(u'articles_article', ['source', 'title'])


    def backwards(self, orm):
        # Removing unique constraint on 'Article', fields ['source', 'title']
        db.delete_unique(u'articles_article', ['source', 'title'])

        # Deleting model 'Article'
        db.delete_table(u'articles_article')


    models = {
        u'articles.article': {
            'Meta': {'unique_together': "(('source', 'title'),)", 'object_name': 'Article'},
            'ari': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'coleman_liau_index': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'flesch': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'flesch_kincaid': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'gunning_fog': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lix': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'rix': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'smog_index': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'source': ('django.db.models.fields.TextField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['articles']