# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nameB', models.CharField(max_length=50)),
                ('datePubB', models.DateField()),
                ('namePubB', models.CharField(max_length=50)),
                ('commentB', models.CharField(max_length=50)),
                ('idB', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
