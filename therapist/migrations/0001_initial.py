# Generated by Django 3.1.2 on 2020-11-07 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='therapist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12)),
                ('created_at', models.DateField()),
                ('password_hash', models.CharField(max_length=100)),
                ('invite_code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='therapist_working_hour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starttime', models.TimeField(blank=True, null=True)),
                ('endtime', models.TimeField(blank=True, null=True)),
                ('rate', models.CharField(max_length=40)),
                ('therapist_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='therapist.therapist')),
            ],
        ),
        migrations.CreateModel(
            name='therapist_technique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technique', models.CharField(max_length=100)),
                ('therapist_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='therapist.therapist')),
            ],
        ),
        migrations.CreateModel(
            name='therapist_special_hour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starttime', models.CharField(max_length=50)),
                ('endtime', models.CharField(max_length=50)),
                ('day', models.CharField(max_length=50)),
                ('therapist_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='therapist.therapist')),
            ],
        ),
        migrations.CreateModel(
            name='therapist_social_media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(default=None, max_length=100, null=True)),
                ('instagram', models.CharField(default=None, max_length=100, null=True)),
                ('linkedIn', models.CharField(default=None, max_length=100, null=True)),
                ('twitter', models.CharField(default=None, max_length=100, null=True)),
                ('youtube', models.CharField(default=None, max_length=100, null=True)),
                ('therapist_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='therapist.therapist')),
            ],
        ),
        migrations.CreateModel(
            name='therapist_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('credentials', models.CharField(max_length=50)),
                ('experience', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('shortbio', models.CharField(max_length=100)),
                ('background', models.CharField(max_length=100)),
                ('personalbelief', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100)),
                ('therapist_id', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='therapist.therapist')),
            ],
        ),
        migrations.CreateModel(
            name='therapist_languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=50)),
                ('therapist_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='therapist.therapist')),
            ],
        ),
        migrations.CreateModel(
            name='therapist_issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.CharField(max_length=100)),
                ('other_issue', models.CharField(max_length=100)),
                ('therapist_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='therapist.therapist')),
            ],
        ),
        migrations.CreateModel(
            name='session_tab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_session', models.CharField(max_length=100)),
                ('end_session', models.CharField(max_length=100)),
                ('therapist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='therapist.therapist')),
            ],
        ),
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starttime', models.CharField(max_length=50, null=True)),
                ('endtime', models.CharField(max_length=50, null=True)),
                ('therapist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='therapist.therapist')),
            ],
        ),
        migrations.CreateModel(
            name='blocked_slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starttime', models.CharField(max_length=50)),
                ('endtime', models.CharField(max_length=50)),
                ('therapist_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='therapist.therapist')),
            ],
        ),
    ]