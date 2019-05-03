# Generated by Django 2.1.4 on 2019-04-24 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_investors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investors',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='companies', to='stock.Company'),
        ),
    ]
