# Generated by Django 3.2.12 on 2022-12-21 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last update date')),
                ('number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Issue number')),
                ('volume', models.CharField(blank=True, max_length=20, null=True, verbose_name='Issue volume')),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='Issue year')),
                ('month', models.IntegerField(blank=True, null=True, verbose_name='Issue month')),
                ('creator', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='issue_creator', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('journal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='journal.scielojournal', verbose_name='Journal')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='issue_last_mod_user', to=settings.AUTH_USER_MODEL, verbose_name='Updater')),
            ],
            options={
                'verbose_name': 'Issue',
                'verbose_name_plural': 'Issues',
            },
        ),
        migrations.AddIndex(
            model_name='issue',
            index=models.Index(fields=['number'], name='issue_issue_number_780a64_idx'),
        ),
        migrations.AddIndex(
            model_name='issue',
            index=models.Index(fields=['volume'], name='issue_issue_volume_71bce1_idx'),
        ),
        migrations.AddIndex(
            model_name='issue',
            index=models.Index(fields=['year'], name='issue_issue_year_7b3c42_idx'),
        ),
        migrations.AddIndex(
            model_name='issue',
            index=models.Index(fields=['month'], name='issue_issue_month_a53df7_idx'),
        ),
    ]