from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('notes', '0010_alter_cliente_email'),
    ]

    operations = [
        migrations.RemoveField(model_name='cavalo', name='proprietario'),
        migrations.AddField(
            model_name='cavalo',
            name='proprietario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notes.cliente'),
        ),
    ]
