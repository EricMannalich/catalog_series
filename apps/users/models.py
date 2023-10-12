from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from simple_history.models import HistoricalRecords
from django.utils.translation import gettext_lazy as _

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'perfil/user_{0}/{1}'.format(instance.id, filename)

class UserManager(BaseUserManager):
    def _create_user(self, username, email, first_name,last_name, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))
        user = self.model(
            username = username,
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, first_name,last_name, password=None, **extra_fields):
        return self._create_user(username, email, first_name,last_name, password, False, False, **extra_fields)

    def create_superuser(self, username, email, first_name,last_name, password=None, **extra_fields):
        return self._create_user(username, email, first_name,last_name, password, True, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('user name'),max_length = 255, unique = True)
    email = models.EmailField(_('email address'),max_length = 255, unique = True,)
    first_name = models.CharField(_('first name'),max_length = 255, blank = True, null = True)
    last_name = models.CharField(_('last name'),max_length = 255, blank = True, null = True)
    image = models.ImageField(upload_to=user_directory_path, max_length=255, null=True, blank = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    historical = HistoricalRecords()
    objects = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    def natural_key(self):
        return (self.email)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

