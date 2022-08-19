# Generated by Django 4.0.6 on 2022-08-19 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frameapp', '0003_alter_text_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/')),
            ],
        ),
        migrations.RemoveField(
            model_name='text',
            name='image',
        ),
    ]
