# Generated by Django 3.1.3 on 2020-11-25 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0004_pizza_date_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzas.pizza')),
            ],
        ),
    ]