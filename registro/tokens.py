from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six


class AccountActuvationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
                six.text_type(user.pk) + six.text_type(timestamp) +
                six.text_type(user.profile.singup_confirmation)
        )


account_activation_token = AccountActuvationTokenGenerator()

# neste modelo crio o tokens
