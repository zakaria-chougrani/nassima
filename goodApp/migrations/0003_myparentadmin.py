# Generated by Django 4.2 on 2023-04-06 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goodApp', '0002_alter_enfant_genre_alter_enfant_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyParentAdmin',
            fields=[
                ('parent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='goodApp.parent')),
            ],
            bases=('goodApp.parent',),
        ),
    ]
