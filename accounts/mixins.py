from django.contrib.auth.models import User
from django.http import Http404


class UserMixin(object):

    def __init__(self, *args, **kwargs):
        self.user_model = User
        self.queryset = User.objects.all()
        return super(UserMixin, self).__init__(*args, **kwargs)

    def get_object(self, user_id):
        try:
            return self.user_model.objects.get(id=user_id)
        except self.user_model.DoesNotExist as e:
            # log error
            raise Http404