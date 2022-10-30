from django.db import models


class Owner(models.Model):
    owner_id = models.IntegerField(primary_key=True)
    surname = models.CharField(max_length=30, null=False, blank=False)
    name = models.CharField(max_length=30, null=False, blank=False)
    birthday_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return "{} {} {}".format(self.surname, self.name, self.birthday_date)


class Car(models.Model):
    car_id = models.IntegerField(primary_key=True)
    number = models.CharField(max_length=15, null=False, blank=False)
    brand = models.CharField(max_length=20, null=False, blank=False)
    model = models.CharField(max_length=20, null=False, blank=False)
    color = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return "{} {} {} {}".format(self.number, self.brand, self.model, self.color)


class Ownership(models.Model):
    owner_car_id = models.IntegerField(primary_key=True)
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)


class DrivingLicense(models.Model):
    license_id = models.IntegerField(primary_key=True)
    owner_id = models.OneToOneField(Owner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10, null=False, blank=False)
    type = models.CharField(max_length=10, null=False, blank=False)
    date_of_issue = models.DateField(null=False, blank=True)








