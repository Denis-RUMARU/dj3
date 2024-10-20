from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=15)


class Car(models.Model):
    BODY_TYPE_CHOICES = [
        ('sedan', 'Седан'),
        ('hatchback', 'Хэтчбек'),
        ('suv', 'Внедорожник'),
        ('coupe', 'Купе'),
        # Добавьте другие типы кузова
    ]

    DRIVE_UNIT_CHOICES = [
        ('fwd', 'Передний привод'),
        ('rwd', 'Задний привод'),
        ('awd', 'Полный привод'),
    ]

    GEARBOX_CHOICES = [
        ('manual', 'Механическая'),
        ('automatic', 'Автоматическая'),
    ]

    FUEL_TYPE_CHOICES = [
        ('petrol', 'Бензин'),
        ('diesel', 'Дизель'),
        ('electric', 'Электрический'),
    ]

    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=30)
    mileage = models.IntegerField()
    volume = models.DecimalField(max_digits=3, decimal_places=1)
    body_type = models.CharField(max_length=20, choices=BODY_TYPE_CHOICES)
    drive_unit = models.CharField(max_length=10, choices=DRIVE_UNIT_CHOICES)
    gearbox = models.CharField(max_length=10, choices=GEARBOX_CHOICES)
    fuel_type = models.CharField(max_length=10, choices=FUEL_TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')

class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
