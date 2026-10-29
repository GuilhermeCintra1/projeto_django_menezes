from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('notes', '0008_remove_cliente_hash_senha'),
    ]

    operations = [
        migrations.RemoveField(model_name='cliente', name='login'),
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
    ]
