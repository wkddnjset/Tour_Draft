from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class User(AbstractUser):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    age = models.IntegerField(null=True)
    sex = models.CharField(max_length=1, null=True, choices=GENDER, default = 'M') # m 이면 남, f이면 여

    def __str__(self):
        return str(self.username)


class Review(models.Model):
    item_id = models.ForeignKey('_Item.Item', related_name="reviews", on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="reviews", on_delete=models.CASCADE)
    star_point = models.IntegerField( default=5,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ])
    comment = models.TextField()

    class Meta:
        unique_together = ('item_id', 'user_id')

    def __str__(self):
        return str(self.comment)


class Category(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return str(self.name)


class Pick(models.Model):
    item_id = models.ForeignKey('_Item.Item', related_name = "picks", on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = "picks", on_delete=models.CASCADE)

    class Meta:
        unique_together = ('item_id', 'user_id')

    def __str__(self):
        return str(self.user_id) + ':' + str(self.item_id)
