from django.db import models

from profiles.models import UserProfile
from products.models import Product


class Comment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_comment')
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    """
    Creates a review model to allow user to perform
    CRUD operations on product reviews
    """

    RATE = [
        (1, '1 out of 5'),
        (2, '2 out of 5'),
        (3, '3 out of 5'),
        (4, '4 out of 5'),
        (5, '5 out of 5'),
    ]

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_rating')
    title = models.CharField(max_length=50)
    # description = models.TextField()
    rating = models.IntegerField(choices=RATE)
    # upvotes = models.IntegerField(default=0)
    # downvotes = models.IntegerField(default=0)
    # date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
