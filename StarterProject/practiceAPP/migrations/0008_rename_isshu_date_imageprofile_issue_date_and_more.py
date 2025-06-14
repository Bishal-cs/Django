# Generated by Django 5.2.2 on 2025-06-10 07:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practiceAPP', '0007_image_review_comment_image_review_ratings_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='imageprofile',
            old_name='isshu_date',
            new_name='issue_date',
        ),
        migrations.RenameField(
            model_name='specific_image',
            old_name='image_type',
            new_name='image_types',
        ),
        migrations.AlterField(
            model_name='all_typs_imgs',
            name='name',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='imageprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='specific_image',
            name='name',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]
