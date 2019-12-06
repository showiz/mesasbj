from django.db import models
from system.models import Categoria, Mesa
# Create your models here.

#----------------------------------------------------CUSTOM USER---------------------
from django.contrib.auth.models import AbstractUser, BaseUserManager ## A new class is imported. ##
from django.db import models
from django.core.validators import MaxValueValidator
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,  **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)



class CustomUser(AbstractUser):
    categoria = models.ForeignKey(Categoria, null=True, on_delete=models.CASCADE, related_name="categoria_user")
    mesa = models.ForeignKey(Mesa, null=True, on_delete=models.CASCADE, related_name="mesa_user")



    email = models.EmailField(_('E-mail'), unique=True)
    nombre = models.CharField(verbose_name="Nombre usuario", max_length=255, null=True)
    apellido = models.CharField(verbose_name="Apellido usuario", max_length=255, null=True)

    rut = models.CharField(verbose_name="Rut", max_length=8, validators=[RegexValidator(r'^\d{1,10}$')], null=True, blank=True)
    dig_rut = models.CharField(verbose_name="Dígito Rut", max_length=1, null=True, blank=True)

    def __str__(self):
        return self.email

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['rut','dig_rut']

    objects = UserManager()
