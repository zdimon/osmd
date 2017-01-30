# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, null=True, verbose_name='\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True)),
                ('image', models.ImageField(upload_to='photo', null=True, verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, verbose_name='\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
            ],
            options={
                'verbose_name': '\u0442\u0435\u043c\u0430',
                'verbose_name_plural': '\u0442\u0435\u043c\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='photo',
            name='subject',
            field=models.ForeignKey(to='page.Subject'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.CharField(max_length=250, verbose_name='slug', blank=True),
        ),
    ]
