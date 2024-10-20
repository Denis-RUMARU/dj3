# Generated by Django 4.2.7 on 2024-10-20 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='client',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='client',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='client',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='phone',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='body_type',
            field=models.CharField(choices=[('sedan', 'Седан'), ('hatchback', 'Хэтчбек'), ('suv', 'Внедорожник'), ('coupe', 'Купе')], max_length=20),
        ),
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='car',
            name='drive_unit',
            field=models.CharField(choices=[('fwd', 'Передний привод'), ('rwd', 'Задний привод'), ('awd', 'Полный привод')], max_length=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(choices=[('petrol', 'Бензин'), ('diesel', 'Дизель'), ('electric', 'Электрический')], max_length=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='gearbox',
            field=models.CharField(choices=[('manual', 'Механическая'), ('automatic', 'Автоматическая')], max_length=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='volume',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sale',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.car'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.client'),
        ),
    ]