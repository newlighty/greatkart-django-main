from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django_jalali.db import models as jmodels


# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('کاربر باید یک آدرس ایمیل داشته باشد')

        if not username:
            raise ValueError('کاربر باید یک نام کاربری داشته باشد')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser):
    first_name      = models.CharField(max_length=50,verbose_name='اسم کوچک')
    last_name       = models.CharField(max_length=50,verbose_name='نام خانوادگی')
    username        = models.CharField(max_length=50, unique=True,verbose_name='نام کاربری')
    email           = models.EmailField(max_length=100, unique=True,verbose_name='ایمیل')
    phone_number    = models.CharField(max_length=50,verbose_name='تلفن')

    # required
    date_joined     = jmodels.jDateTimeField(auto_now_add=True,verbose_name='تاریخ پیوستن')
    last_login      = jmodels.jDateTimeField(auto_now_add=True,verbose_name='اخرین  ورود')
    is_admin        = models.BooleanField(default=False,verbose_name='ادمین')
    is_staff        = models.BooleanField(default=False,verbose_name='کارمندان')
    is_active        = models.BooleanField(default=False,verbose_name='فعال')
    is_superadmin        = models.BooleanField(default=False,verbose_name='مدیر سایت')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    
    class Meta:
        verbose_name = ' حساب'
        verbose_name_plural = 'حسابها'


    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
