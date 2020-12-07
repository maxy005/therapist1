from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six
from .models import therapist
from six import text_type
class AppTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, th, timestamp):
        return (
            six.text_type(th.pk) + six.text_type(timestamp) +
            six.text_type(th.is_valid)
        )

token_generator = AppTokenGenerator()