# Generated by Django 3.0.8 on 2020-08-17 06:43

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_image',
            field=models.ImageField(upload_to=users.models.PathAndRename('pics/2020/08/17')),
        ),
        migrations.AlterField(
            model_name='userextradetails',
            name='user_image',
            field=models.ImageField(default='default.png', upload_to=users.models.PathAndRename('profile/2020/08/17')),
        ),
        migrations.AlterField(
            model_name='userextradetails',
            name='user_resume',
            field=models.FileField(default='resume.pdf', upload_to=users.models.PathAndRename('files/2020/08/17')),
        ),
    ]