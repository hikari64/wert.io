from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core.validators import MaxValueValidator, MinValueValidator
class UserManager(BaseUserManager):
    def create_user(self,email,password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
			password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email,password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
			password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
	First_Name = models.CharField(max_length=20,null=True,unique=True)
	Last_Name = models.CharField(max_length=20,null=True,unique=True)
	Middle_Name = models.CharField(max_length=20,null=True,unique=True,)
	CSU_ID = models.IntegerField(unique=True,null=True,validators=[MaxValueValidator(1999999999),MinValueValidator(1000000000)])
	email = models.EmailField(verbose_name='email address',max_length=255,unique=True)
	GHSM ='GHSM'
	TE = 'TE'
	DC = 'DC'
	CSU_Class_Choices = (
		(GHSM,'Gospel Holiday School Of Ministry'),
		(TE, 'Truth Exposition'),
		(DC, 'Discipleship Class'),
		)
	CSU_Class = models.CharField(
		max_length=4,
		choices = CSU_Class_Choices,
		default = GHSM
		)

	none ='None'
	CCL ='CCL'
	CL= 'CL'
	TL = 'TL'
	CSU_Position_Choices = (
		(none,'None'),
		(CCL,'Cell Component Leader'),
		(CL,'Cell Leader'),
		(TL, 'Tissue Leader')
		)
	CSU_Position = models.CharField(
		max_length=4,
		choices=CSU_Position_Choices,
		default=none

		)

	none = 'None'
	MCAA = 'MCAA'
	MOSAF = 'MOSAF'
	MASA = 'MASA'
	MSO='MSO'
	ME = 'ME'
	MI = 'MI'
	MIAW = 'MIAW'
	MOM = 'MOM'
	MOH ='MOH'
	MOTA = 'MOTA'
	MEA = 'MEA'
	MOE = 'MOE'
	MOPAM = 'MOPAM'

	CSU_Ministry_Choices = (
		(none,'None'),
		(MCAA,'Ministry Of Creativity And Arts'),
		(MOSAF, 'Ministry Of Sports And Fitness'),
		(MASA, 'Ministry Of Seed Sowing And Admnistration'),
		(MSO,'Ministry Of Security And Order'),
		(ME,'Ministry Of Evangelism'),
		(MI,'Ministry Of Information'),
		(MIAW,'Ministry Of Interior And Welfare'),
		(MOM,'Ministry Of Music'),
		(MOH, 'Ministry Of Helps'),
		(MOTA,'Ministry Of Trade And Investment'),
		(MEA, 'Ministry Of Exterior Affairs'),
		(MOE, 'Ministry Of Events'),
		(MOPAM,'Ministry Of Property And Management')
		)
	CSU_Ministry= models.CharField(
		max_length=5,
		choices=CSU_Ministry_Choices,
		default=none
		)
	Cell_Component_Leader_Name = models.CharField(max_length=30, null=True)
	Cell_Leader_Name = models.CharField(max_length=30, null=True)
	Tissue_Leader_Name = models.CharField(max_length=30, null=True)

	active = models.BooleanField(default=True)
	staff = models.BooleanField(default=False) # a admin user; non super-user
	admin = models.BooleanField(default=False) # a superuser
    # notice the absence of a "Password field", that's built in.
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []
	def get_full_name(self):
        # The user is identified by their email address
		return '%s %s %s' %(self.First_Name,self.Last_Name,self.Middle_Name)
	def get_short_name(self): 
        # The user is identified by their email address
		return self.First_Name
	def __str__(self):              # __unicode__ on Python 2
		return'%s %s %s' %(self.First_Name,self.Last_Name,self.Middle_Name)
	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
		return True
	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
		return True
	@property
	def is_staff(self):
		"Is the user a member of staff?"
		return self.staff
	@property
	def is_admin(self):
		"Is the user a admin member?"
		return self.admin
	@property
	def is_active(self):
		"Is the user active?"
		return self.active
	
	objects = UserManager()