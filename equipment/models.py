from django.db import models

# Create your models here.

class Clients(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)

    def __str__(self):
        return self.name
    
class Repairs(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='Describe the repair here.')
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)

    def __str__(self):
        return self.name
