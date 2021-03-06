# Generated by Django 2.2.2 on 2019-06-14 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20190613_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedWork',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='Anonymous', max_length=100)),
                ('workuploaddate', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(default='Anonymous@example.com', max_length=100)),
                ('srsdoc', models.FileField(upload_to='documents/')),
                ('descriptions', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='member',
            name='descriptions',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='descriptions',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='descriptions',
            field=models.TextField(blank=True),
        ),
    ]
