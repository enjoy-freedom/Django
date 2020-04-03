
import time

from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
import jwt
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from myapi.settings import SECRET_KEY, EXPIRE_MINUTES
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.base_user import AbstractBaseUser


class App(AbstractBaseUser):
    userNameValidator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[userNameValidator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_superuser = models.BooleanField(
        _('superuser status'),
        default=False,
        help_text=_(
            'Designates that this user has all permissions without '
            'explicitly assigning them.'
        ),
    )

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = UserManager()
    # objects = MyBaseUserManager()

    def create_token(self):
        headers = {
            "typ": "JWT",
            "alg": "HS256",
            "user_id": self.username
        }

        playload = {
            "headers": headers,
            "iss": 'myapi',
            "exp": time.time()+EXPIRE_MINUTES,
            'iat': time.time()
        }
        signature = jwt.encode(playload, SECRET_KEY, algorithm='HS256')
        return signature, playload['exp']



