# Generated by Django 2.1.7 on 2019-04-15 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20190415_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='client_mail',
            field=models.EmailField(default='qeq@qeq.ru', max_length=250, verbose_name='E-mail'),
            preserve_default=False,
        ),
    ]
