# Generated by Django 5.0.7 on 2024-07-20 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='full_image',
            field=models.ImageField(blank=True, default='what_a_week.jpg', upload_to=''),
        ),
    ]
