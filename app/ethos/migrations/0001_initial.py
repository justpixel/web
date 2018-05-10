# Generated by Django 2.0.5 on 2018-05-10 08:32

from django.db import migrations, models
import django.db.models.deletion
import economy.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('ip', models.GenericIPAddressField(protocol='IPv4')),
                ('twitter_username', models.CharField(max_length=255)),
                ('twitter_profile_pic', models.URLField()),
                ('txid', models.CharField(default='', max_length=255)),
                ('web3_address', models.CharField(max_length=255)),
                ('gif', models.FileField(null=True, upload_to='ethos/shortcodes/gifs/')),
                ('png', models.ImageField(null=True, upload_to='ethos/hops/pngs/')),
                ('previous_hop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ethos.Hop')),
            ],
            options={
                'verbose_name_plural': 'Hops',
            },
        ),
        migrations.CreateModel(
            name='ShortCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('num_scans', models.PositiveSmallIntegerField(default=0)),
                ('shortcode', models.CharField(default='', max_length=255)),
                ('gif', models.FileField(null=True, upload_to='ethos/shortcodes/gifs/')),
                ('png', models.ImageField(null=True, upload_to='ethos/shortcodes/pngs/')),
            ],
            options={
                'verbose_name_plural': 'ShortCodes',
            },
        ),
        migrations.CreateModel(
            name='TwitterProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('profile_picture', models.ImageField(blank=True, max_length=255, null=True, upload_to='ethos/twitter_profiles/')),
                ('username', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Twitter Profiles',
            },
        ),
        migrations.AddField(
            model_name='hop',
            name='shortcode',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hops', to='ethos.ShortCode'),
        ),
        migrations.AddField(
            model_name='hop',
            name='twitter_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hops', to='ethos.TwitterProfile'),
        ),
    ]