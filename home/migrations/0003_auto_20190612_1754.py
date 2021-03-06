# Generated by Django 2.2.2 on 2019-06-12 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='address',
            field=models.CharField(default='Noida IN', max_length=100),
        ),
        migrations.AddField(
            model_name='homepage',
            name='companydetail',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='customerfeedback',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='email',
            field=models.CharField(default='altf4upenter@gmail.com', max_length=100),
        ),
        migrations.AddField(
            model_name='homepage',
            name='mission',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='phone',
            field=models.CharField(default='9910741462', max_length=100),
        ),
        migrations.AddField(
            model_name='homepage',
            name='specialize',
            field=models.CharField(default='S', max_length=100),
        ),
        migrations.AddField(
            model_name='homepage',
            name='vision',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='company',
            field=models.CharField(default='SKFWEB', max_length=100),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='title',
            field=models.CharField(default='SKFWEB', max_length=100),
        ),
    ]
