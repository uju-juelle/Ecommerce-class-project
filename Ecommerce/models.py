from django.db import models

CATEGORY_CHOICES = (
    ("ELECTRONICS", "ELECTRONICS"), 
    ("FASHION", "FASHION"),
    ("BABY", "BABY"),
    ("WOMEN", "WOMEN"),
    ("MEN", "MEN")
)

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100)
    image = models.ImageField(upload_to="product_images", default="product.jpg")


    def __str__(self):
        return self.name