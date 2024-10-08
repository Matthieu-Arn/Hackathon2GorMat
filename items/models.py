from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who reported the item
    public_description = models.CharField(max_length=100)  # Two-word public description
    full_description = models.TextField()  # Detailed description for admin visibility
    date_reported = models.DateField()  # Date the item was reported
    location = models.CharField(max_length=255)  # Location where the item was lost or found
    status = models.CharField(max_length=10, choices=[('Lost', 'Lost'), ('Found', 'Found')])  # Lost or found status
    resolved = models.BooleanField(default=False)  # Item recovered or not

    def __str__(self):
        return self.public_description


class Comment(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)  # Related item
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who posted the comment
    content = models.TextField()  # Comment content
    timestamp = models.DateTimeField(auto_now_add=True)  # When the comment was posted

    def __str__(self):
        return f'Comment by {self.user} on {self.item}'
