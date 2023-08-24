from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Dish(models.Model):
    image = models.ImageField(
        upload_to="dishes/%Y/%m/%d/", default="default/default.png", 
        max_length=255)
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True, related_name="dishes")
    description = models.TextField(blank=True, default="")
    price = models.PositiveIntegerField()

    def get_absolute_url(self):
        return reverse("dish", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("update_dish", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("delete_dish", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return self.name
