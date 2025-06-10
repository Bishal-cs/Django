from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class all_typs_imgs(models.Model):
    TYPES_OF_CHOICES = [
        ('gaming', 'Gaming'),
        ('nature', 'Nature & Landscapes'),
        ('urban', 'Urban'),
        ('abstract', 'Abstract'),
        ('portrait', 'Portrait'),
        ('technology', 'Technology'),
        ('fashion', 'Fashion'),
        ('architecture', 'Architecture'),
        ('wildlife', 'Wildlife'),
        ('sports', 'Sports'),
        ('travel', 'Travel'),
        ('food', 'Food & Cuisine'),
        ('macro', 'Macro'),
        ('aerial', 'Aerial'),
        ('cinematic', 'Cinematic'),
        ('fantasy', 'Fantasy'),
        ('vintage', 'Vintage'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    date_time_stamp = models.DateTimeField(default=timezone.now)
    type = models.CharField(
        max_length=20,
        choices=TYPES_OF_CHOICES
    )
    description = models.TextField(default='')

    def __str__(self):
        return self.name


# One-to-many relationship: one image can have many reviews
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
    ratings = models.IntegerField(default=0)
    comment = models.TextField(default='')
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} reviewed {self.image.name}'


# Many-to-many relationship: a specific image can be linked with many image types
class image_store(models.Model):
    name = models.CharField(max_length=100)
    image_info = models.CharField(max_length=100)
    image_type = models.ManyToManyField(all_typs_imgs, related_name='specific_images')

    def __str__(self):
        return self.name


# One-to-one relationship with user: a profile for each user
class ImageProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_number = models.CharField(max_length=100)
    isshu_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'{self.user.username} Profile'