# Generated by Django 4.2.6 on 2023-10-17 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recruit', '0001_initial'),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('apply_id', models.AutoField(primary_key=True, serialize=False, verbose_name='지원_id')),
                ('recruit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruit.recruit', verbose_name='채용공고_id')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='company.user', verbose_name='사용자_id')),
            ],
        ),
    ]
