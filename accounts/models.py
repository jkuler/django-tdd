import uuid
from django.db import models
from django.contrib import auth
from django.utils import timezone

auth.signals.user_logged_in.disconnect(auth.models.update_last_login)


class User(models.Model):
    email = models.EmailField(primary_key=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    last_login = timezone.now()
    is_anonymous = False
    is_authenticated = True


class Token(models.Model):
    email = models.EmailField()
    uid = models.CharField(default=uuid.uuid4, max_length=40)


# class ListUserManager(BaseUserManager):
#
#     def create_user(self, email):
#         ListUser.objects.create(email=email)
#
#     def create_superuser(self, email, password):
#         self.create_user(email)


# class ListUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(primary_key=True)
#     USERNAME_FIELD = 'email'
#     #REQUIRED_FIELDS = ['email', 'x']
#
#     objects = ListUserManager()
#
#     @property
#     def is_staff(self):
#         return self.email == 'josh.kula@outlook.com'
#
#     @property
#     def is_active(self):
#         return True