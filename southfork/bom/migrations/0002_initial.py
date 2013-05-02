# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProductInfo'
        db.create_table(u'bom_productinfo', (
            ('part_number', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30, primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('product_generation', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('revision', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=5)),
            ('product_category', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('to_date', self.gf('django.db.models.fields.DateField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('theoretical_cycle_time', self.gf('django.db.models.fields.IntegerField')()),
            ('product_file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'bom', ['ProductInfo'])

        # Adding model 'Components'
        db.create_table(u'bom_components', (
            ('component_number', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50, primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('component_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('revision', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=5)),
            ('to_date', self.gf('django.db.models.fields.DateField')()),
            ('component_category', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('manufacturer', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'bom', ['Components'])

        # Adding model 'BOMInfo'
        db.create_table(u'bom_bominfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='parent', to=orm['bom.ProductInfo'])),
            ('child', self.gf('django.db.models.fields.related.ForeignKey')(related_name='child', to=orm['bom.ProductInfo'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'bom', ['BOMInfo'])


    def backwards(self, orm):
        # Deleting model 'ProductInfo'
        db.delete_table(u'bom_productinfo')

        # Deleting model 'Components'
        db.delete_table(u'bom_components')

        # Deleting model 'BOMInfo'
        db.delete_table(u'bom_bominfo')


    models = {
        u'bom.bominfo': {
            'Meta': {'ordering': "['parent']", 'object_name': 'BOMInfo'},
            'child': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'child'", 'to': u"orm['bom.ProductInfo']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'parent'", 'to': u"orm['bom.ProductInfo']"})
        },
        u'bom.components': {
            'Meta': {'ordering': "['component_number']", 'object_name': 'Components'},
            'component_category': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'component_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'component_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'revision': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '5'}),
            'to_date': ('django.db.models.fields.DateField', [], {})
        },
        u'bom.productinfo': {
            'Meta': {'ordering': "['part_number']", 'object_name': 'ProductInfo'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bom_number': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['bom.ProductInfo']", 'null': 'True', 'through': u"orm['bom.BOMInfo']", 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'part_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30', 'primary_key': 'True'}),
            'product_category': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'product_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'product_generation': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'revision': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '5'}),
            'theoretical_cycle_time': ('django.db.models.fields.IntegerField', [], {}),
            'to_date': ('django.db.models.fields.DateField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['bom']