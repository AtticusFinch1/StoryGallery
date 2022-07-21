# Generated by Django 4.0.1 on 2022-02-24 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0007_postman_phone_postman_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postman',
            name='profile_pic',
            field=models.ImageField(blank=True, default='avatar1.jpg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='postman',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher_name', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=50)),
                ('publication_date', models.DateField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.category')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.post')),
                ('postman', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.postman')),
            ],
        ),
    ]