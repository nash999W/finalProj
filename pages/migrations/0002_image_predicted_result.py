from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='predicted_result',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]