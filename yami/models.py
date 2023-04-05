from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=50)
    describe = models.TextField()
    picture = models.ImageField(upload_to="Productimages")
    is_pub = models.BooleanField(default=False)
    price = models.IntegerField()
    category = models.ForeignKey(Category, related_name="items", on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.title
