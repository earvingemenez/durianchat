from .models import Message


class MessageMixin(object):

    def __init__(self, *args, **kwargs):
        self.queryset = Message.objects.all()
        return super(MessageMixin, self).__init__(*args, **kwargs)

    def clean_param(self, qdict):
        data = {}
        for key, value in qdict.iteritems():
                data[key] = value

        return data

    def get_object(self, message_id):
        try:
            return Message.objects.get(id=message_id)
        except Message.DoesNotExist as e:
            # log e
            # Raise error
            raise Http404