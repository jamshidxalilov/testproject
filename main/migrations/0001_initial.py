# Generated by Django 3.2.3 on 2021-05-25 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.action')),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.branch')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.country')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('legal', models.IntegerField(choices=[(0, 'True'), (1, 'False')])),
                ('firm', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('birthday', models.DateTimeField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.country')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.district')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.country')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anons', models.TextField()),
                ('result', models.TextField()),
                ('expire_at', models.DateTimeField()),
                ('amount', models.IntegerField(null=True)),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.action')),
                ('branch', models.ManyToManyField(to='main.Branch')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.country')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.district')),
                ('organization', models.ManyToManyField(to='main.Organization')),
                ('partner', models.ManyToManyField(to='main.Partner')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.region')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.status')),
            ],
        ),
        migrations.AddField(
            model_name='partner',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.region'),
        ),
        migrations.AddField(
            model_name='district',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.region'),
        ),
    ]
