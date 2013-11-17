# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Source'
        db.create_table(u'articles_source', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('domain', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'articles', ['Source'])


        # Changing field 'Article.title'
        db.alter_column(u'articles_article', 'title', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Article.timestamp'
        db.alter_column(u'articles_article', 'timestamp', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Renaming column for 'Article.source' to match new field type.
        db.rename_column(u'articles_article', 'source', 'source_id')
        # Changing field 'Article.source'
        db.alter_column(u'articles_article', 'source_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['articles.Source']))
        # Adding index on 'Article', fields ['source']
        db.create_index(u'articles_article', ['source_id'])


    def backwards(self, orm):
        # Removing index on 'Article', fields ['source']
        db.delete_index(u'articles_article', ['source_id'])

        # Deleting model 'Source'
        db.delete_table(u'articles_source')


        # Changing field 'Article.title'
        db.alter_column(u'articles_article', 'title', self.gf('django.db.models.fields.TextField')())

        # User chose to not deal with backwards NULL issues for 'Article.timestamp'
        raise RuntimeError("Cannot reverse this migration. 'Article.timestamp' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Article.timestamp'
        db.alter_column(u'articles_article', 'timestamp', self.gf('django.db.models.fields.DateTimeField')())

        # Renaming column for 'Article.source' to match new field type.
        db.rename_column(u'articles_article', 'source_id', 'source')
        # Changing field 'Article.source'
        db.alter_column(u'articles_article', 'source', self.gf('django.db.models.fields.TextField')())

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
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['articles.Source']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'articles.source': {
            'Meta': {'object_name': 'Source'},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['articles']