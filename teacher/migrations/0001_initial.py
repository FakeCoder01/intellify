# Generated by Django 3.2.12 on 2022-09-15 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacher_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, default='t-avatar.jpg', null=True, upload_to='teachers/')),
                ('full_name', models.CharField(default='', max_length=50, null=True)),
                ('phone', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('gender', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('subject', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('address', models.TextField(blank=True, default='', null=True)),
                ('zipcode', models.CharField(blank=True, default='', max_length=6, null=True)),
                ('psw', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('classroom', models.ManyToManyField(blank=True, null=True, related_name='classroommodel', to='school.Classroom')),
                ('school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schoolprofile', to='school.school')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacherprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
