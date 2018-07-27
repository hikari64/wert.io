from django.db import models
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

class MyManager(models.Manager):
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except ObjectDoesNotExist:
            return None
class GradingCriteria(models.Model):
	Name = models.CharField(max_length=20)
	Description = models.TextField()

	def __str__(self):
		return str(self.Name)


class IndividualGrading(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)
	A = 'A'
	BPLUS = 'B+'
	B = 'B'
	CPLUS = 'C+'
	C = 'C'
	DPLUS = 'D+'
	D = 'D'
	Grade_Choices = (
		(A ,'A'),
		(BPLUS , 'B+'),
		(B , 'B'),
		(CPLUS , 'C+'),
		(C , 'C'),
		(DPLUS , 'D+'),
		(D , 'D'),
	)
	Criteria = models.ForeignKey(GradingCriteria,on_delete=models.CASCADE)
	Grade = models.CharField(max_length=2,choices=Grade_Choices,default=A)
	
	
	def __str__(self):
		return '%s---- %s' %(self.user,self.Criteria)
	
	objects = MyManager()