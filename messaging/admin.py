from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    """ Admin class that contains the configuration for
        `model:Message`
    """
    model = Message
    list_display = ['sender', 'recipient', 'content']


# Register to admin panel
admin.site.register(Message, MessageAdmin)