# Generated by Django 3.1.6 on 2021-02-17 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers'),
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='book',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(choices=[['HB', 'HOBBIT'], ['LOTR', 'LORD OF THE RING']], default='Book Title', max_length=50, unique=True),
        ),
    ]
