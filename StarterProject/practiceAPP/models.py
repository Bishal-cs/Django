from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class all_typs_imgs(models.Model):
    TYPES_OF_CHOICES = [
        ('type1', 'Type 1'),
        ('type2', 'Type 2'),
        ('type3', 'Type 3'),
        ('type4', 'Type 4'),
        ('type5', 'Type 5'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    date_time_stamp = models.DateTimeField(default=timezone.now)
    type = models.CharField(
        max_length=20,
        choices=TYPES_OF_CHOICES)
    description = models.TextField(default='')
    
    def __str__(self):
        return self.name
    
# one to many relationship with user 
class Image_review(models.Model):
    image = models.ForeignKey(
        all_typs_imgs,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    ratings = models.IntegerField(default=0),
    comment = models.TextField(default=''),
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} reviewed {self.image.name}'
    
# Many to many relationship with user
class specific_image(models.Model):
    name = models.CharField(max_length=100)
    image_info = models.CharField(max_length=100)
    image_type = models.ManyToManyField(all_typs_imgs, related_name='specific_images')

    def __str__(self):
        return self.name
    
# one to one relationship with user

class ImageProfile(models.Model):
    user = models.OneToOneField(all_typs_imgs, on_delete=models.CASCADE, related_name='profile')
    profile_number = models.CharField(max_length=100)
    isshu_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'{self.user.name} Profile'