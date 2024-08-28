# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
class CustomUser(AbstractUser):
    fname = models.CharField(max_length=50, null=True, blank=True)
    lname = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return f"{self.username} - {self.email}- {self.password}, {self.fname}- {self.lname}, {self.gender} - {self.phone}"


"""
class Bus(AbstractUser):
    no_seats = models.CharField(max_length=50, null=True, blank=True)
    plate_no = models.CharField(max_length=50, null=True, blank=True)
    side_no = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.no_seats} - {self.plate_no}- {self.side_no}"

class Route(AbstractUser):
    depcity = models.CharField(max_length=50, null=True, blank=True)
    descity = models.CharField(max_length=50, null=True, blank=True)
    side_no = models.CharField(max_length=20, null=True, blank=True)
    plate_no = models.CharField(max_length=20, null=True, blank=True)
    kilometer = models.CharField(max_length=20, null=True, blank=True)
    price = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.depcity} - {self.plate_no}- {self.side_no} {self.descity} - {self.kilometer}- {self.price}"

class City(AbstractUser):
    depcity = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return f"{self.depcity}"


class Fedback(AbstractUser):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    message = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.email}- {self.phone} {self.message}"

class Worker(AbstractUser):
    fname = models.CharField(max_length=50, null=True, blank=True)
    lname = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    plate_no = models.CharField(max_length=50, null=True, blank=True)
    side_no = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.email}- {self.phone} {self.message}"

class Worker(AbstractUser):
    fname = models.CharField(max_length=50, null=True, blank=True)
    lname = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    plate_no = models.CharField(max_length=50, null=True, blank=True)
    side_no = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.email}- {self.phone} {self.message}"

class Admin(AbstractUser):
    fname = models.CharField(max_length=50, null=True, blank=True)
    lname = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.fname} - {self.lname}- {self.phone} {self.password} - {self.gender} - {self.username}- {self.email}"

class Ticket(AbstractUser):
    firstname = models.CharField(max_length=50, null=True, blank=True)
    lastname = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    depcity = models.CharField(max_length=50, null=True, blank=True)
    descity = models.CharField(max_length=50, null=True, blank=True)
    date = models.CharField(max_length=50, null=True, blank=True)
    no_seat = models.CharField(max_length=50, null=True, blank=True)
    price = models.CharField(max_length=50, null=True, blank=True)
    side_no = models.CharField(max_length=50, null=True, blank=True)
    plate_no = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.firstname} - {self.lastname}- {self.phone} - {self.depcity} - {self.descity} - {self.date}- {self.no_seat} - {self.plate_no} - {self.side_no} - {self.price}"

class Ticket(AbstractUser):
    firstname = models.CharField(max_length=50, null=True, blank=True)
    lastname = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    depcity = models.CharField(max_length=50, null=True, blank=True)
    descity = models.CharField(max_length=50, null=True, blank=True)
    date = models.CharField(max_length=50, null=True, blank=True)
    no_seat = models.CharField(max_length=50, null=True, blank=True)
    price = models.CharField(max_length=50, null=True, blank=True)
    side_no = models.CharField(max_length=50, null=True, blank=True)
    plate_no = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.firstname} - {self.lastname}- {self.phone} - {self.depcity} - {self.descity} - {self.date}- {self.no_seat} - {self.plate_no} - {self.side_no} - {self.price}"


class Buschange(AbstractUser):
    depcity = models.CharField(max_length=50, null=True, blank=True)
    descity = models.CharField(max_length=50, null=True, blank=True)
    date = models.CharField(max_length=50, null=True, blank=True)
    side_no = models.CharField(max_length=50, null=True, blank=True)
    plate_no = models.CharField(max_length=50, null=True, blank=True)
    new_side_no = models.CharField(max_length=50, null=True, blank=True)
    new_plate_no = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.depcity} - {self.descity}- {self.date} - {self.side_no} - {self.plate_no} - {self.new_side_no}- {self.new_plate_no}"
class Worker(CustomUser):
    groups = models.ManyToManyField(Group, related_name='worker_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='worker_permissions')

class Fedback(CustomUser):
    user_permissions = models.ManyToManyField(Permission, related_name='fedback_permissions')

class Route(CustomUser):
    user_permissions = models.ManyToManyField(Permission, related_name='route_permissions')

class Ticket(CustomUser):
    user_permissions = models.ManyToManyField(Permission, related_name='ticket_permission')
"""
