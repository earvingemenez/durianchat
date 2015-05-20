from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    """ Model class that will contain the user's messages
    """
    sender = models.ForeignKey(User, related_name="sender")
    recipient = models.ForeignKey(User, related_name="recipient")

    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{} to {}".format(self.sender, self.recipient)