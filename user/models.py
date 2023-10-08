from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(
        self,
        fullname,
      
        email=None,
        phone_number=None,
        password=None,
        is_active=True,
        is_staff=False,
        is_superuser=False,
    ):
        if not email and not phone_number:
            raise ValueError("User must have an email or phone number")
        if not fullname:
            raise ValueError("User must have a full name")
       
        user = self.model(
            email=self.normalize_email(email) if email else None,
            phone_number=phone_number,
            fullname=fullname,
            
            is_active=is_active,
            is_staff=is_staff,
            is_superuser=is_superuser,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, fullname, email, password):
        user = self.create_user(
            fullname==fullname,
            
            email=email,
           # phone_number=phone_number,
            password=password,
            is_staff=True,
            is_superuser=True,
        )
        return user

class User(AbstractBaseUser, PermissionsMixin):
    fullname= models.CharField(verbose_name="fullname", max_length=255)
    #last_name = models.CharField(verbose_name="Last Name", max_length=255)
    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True,
        blank=True,
        null=True,
    )
    phone_number = models.CharField(
       
        max_length=15,
        unique=True,
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'# You can set it to 'phone_number' if you want to allow phone number as username
    REQUIRED_FIELDS = ['fullname']

    def get_username(self):
        # This method returns the username used for authentication.
        # You can modify this method to return email or phone_number based on your requirements.
        return self.email or self.phone_number

    def __str__(self):
        return self.get_username()
    



class Profileinfo1(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    # Add other additional fields for the profile here (e.g., profile_picture, bio, etc.)

    def __str__(self):
        return self.user.get_username()
    



class Profileinfolocationbd(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    District = models.CharField(max_length=255, blank=True, null=True)










class Profileinfolocationabroad(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    countryname = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    duration = models.PositiveIntegerField(default=0,null=True)




class Profileinfoexperience(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    durationstay = models.PositiveIntegerField(default=0,null=True)   

    industry = models.CharField(max_length=255, blank=True, null=True)
    areaofexpertise = models.CharField(max_length=255, blank=True, null=True) 
    durationstay = models.PositiveIntegerField(default=0,null=True) 

     





   

