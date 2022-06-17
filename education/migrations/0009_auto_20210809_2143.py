# Generated by Django 3.2.4 on 2021-08-09 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0008_alter_course_typee'),
    ]

    operations = [
        migrations.DeleteModel(
            name='C',
        ),
        migrations.AddField(
            model_name='lecture',
            name='typee',
            field=models.CharField(choices=[(1, 'academic'), (2, 'functional')], default='global', max_length=200),
        ),
    ]
