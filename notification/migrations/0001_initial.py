# Generated by Django 4.2.1 on 2023-05-13 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notificaiton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.BigIntegerField()),
                ('text', models.CharField(max_length=150)),
                ('is_seen', models.BooleanField(default=False)),
                ('notification_types', models.CharField(choices=[('Blog', 'Blog'), ('Like', 'Like'), ('Follow', 'Follow')], max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
    ]
