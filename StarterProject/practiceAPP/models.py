from django.db import models
from django.utils import timezone

# Create your models here.
class all_typs_imgs(models.Model):
    TYPES_OF_CHOICES = [
        ('type1', 'Type 1'),
        ('type2', 'Type 2'),
        ('type3', 'Type 3'),
        ('type4', 'Type 4'),
        ('type5', 'Type 5'),
    ]
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')
    date_time_stamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name