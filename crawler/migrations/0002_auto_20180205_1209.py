# Generated by Django 2.0.1 on 2018-02-05 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crawl',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crawler.Project'),
        ),
        migrations.AlterField(
            model_name='globalstat',
            name='crawl_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crawler.Crawl'),
        ),
        migrations.AlterField(
            model_name='link',
            name='url_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crawler.UrlDetail'),
        ),
        migrations.AlterField(
            model_name='project',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='urldetail',
            name='crawl_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crawler.Crawl'),
        ),
        migrations.AlterField(
            model_name='urlstat',
            name='url_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crawler.UrlDetail'),
        ),
    ]
