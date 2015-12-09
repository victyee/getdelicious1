from django.db import models

# Create your models here.

SUBJECT = (
	('BE', "Bookings Enquiry"),
	('GE', "General Enquiry"),
	('YGR', "You guys rock!!"),
	('ME', "Media Enquiry"),
	('FTO', "I'm a foodtruck owner and would like more info"),
	('CO', "Complaints"),
	('SU', "Suggestions"),
	('OT', "Others"),
	)

class ContactUs(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=120)
	contact_number = models.CharField(max_length=100, null=True, blank=True)
	subject = models.CharField(max_length=120, choices=SUBJECT)
	message = models.TextField(max_length=850)

	def __unicode__(self):
		return self.name