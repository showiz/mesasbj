# Generated by Django 2.2 on 2019-12-06 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
        ('user', '0003_auto_20191206_0153'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categoria_user', to='system.Categoria'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='mesa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mesa_user', to='system.Mesa'),
        ),
    ]
