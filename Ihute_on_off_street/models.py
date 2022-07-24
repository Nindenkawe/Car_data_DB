from email.policy import default
from wsgiref import validate
from django.db import models
from django.contrib.auth.models import User
from .utils import create_new_ref_number

class Subscriber(models.Model):
	sub_id = models.OneToOneField(User,
        on_delete=models.CASCADE,
        related_name="Subscriber",
        null=True,
    )
	phone_number = models.CharField(max_length=20, null=True)
	plate_number = models.CharField(max_length=15, null=True)
	tin_number = models.CharField(max_length=64, null=True)
	chassis_number = models.CharField(max_length=20, null=True)
	make_year = models.CharField(max_length=10, null=True)
	vehicule_model = models.CharField(max_length=64, null=True)
	number_of_seats = models.CharField(max_length=64, null=True)
	use_of_vehicule_choice = (
	('Drive & Business', 'Drive & Business'),
	('Transport of goods', 'Transport of goods'),
	('Transport of Fuel', 'Transport of Fuel'),
	('Taxi', 'Taxi')
	)	
	use_of_vehicule = models.CharField(
	max_length=32,
	choices=use_of_vehicule_choice,)
	parking_wallet = models.IntegerField(default=0)
	
	def __str__(self):
		return (self.phone_number)

	def save(self, *args, **kwargs):
		self.plate_number = self.plate_number
		if self.plate_number == True:
			self.sub_id == validate
		super().save(*args, **kwargs)



class Transaction(models.Model):
	sub_id = models.ForeignKey(User,
        on_delete=models.CASCADE,
        related_name="Transaction",
        null=True,
    )
	
	transaction_id = models.CharField(
		max_length = 10,
		blank=True,
		editable=False,
		unique=True,
		default=create_new_ref_number
	)

	Transaction_choice = (
	('E_Parking', 'Pay_parking'),
	('E_Insurance', 'Buy_insurance'),
	('Mechanical_serv', 'Book_mechanic'),
	('Chauffeur_4hire', 'Chauffeur_4hire')
	)
	Transaction_type = models.CharField(
	max_length=32,
	choices=Transaction_choice,)

	providertype_id = (
	('E_Parking', 'E_Parking'),
	('E_Insurance', 'E_Insurance'),
	('Mechanical_serv', 'Mechanical_serv'),
	('Chauffeur_4hire', 'Chauffeur_4hire')
	)
	provider = models.CharField(max_length=50, choices=providertype_id)
	amount = models.IntegerField(default=0)
	transaction_status = models.BooleanField(default=False)


	def __str__(self):
		return f"{self.transaction_id}"

	def confirm_transaction(self, *args, **kwargs):
		self.amount = self.amount
		if self.transaction_id == True:
			self.transaction_status == validate
		super().save(*args, **kwargs)

class Provider(models.Model):
	provider = models.OneToOneField(User,
	on_delete=models.CASCADE,
	related_name="Provider",
	null=True,
    )

	service_offered = (
	('E_Parking', 'E_Parking'),
	('E_Insurance', 'E_Insurance'),
	('Mechanical_serv', 'Mechanical_serv'),
	('Chauffeur_4hire', 'Chauffeur_4hire')
	)	
	service_type = models.CharField(
	max_length=32,
	choices=service_offered,)
	
	def __str__(self):
		return f"{self.provider}"

class Proposed_insucovers(models.Model):
	sub_id = models.OneToOneField(User,
	on_delete=models.CASCADE,
	related_name="Proposed_insucovers",
	null=True,
)
	Third_party_liabilityGuarantee = models.BooleanField(default=False)
	window_breaking = models.BooleanField(default=False)
	Recoure = models.BooleanField(default=False)
	material_damaged = models.BooleanField(default=False)
	Theft_Covers = models.BooleanField(default=False)
	Fire_Covers = models.BooleanField(
	default=False)
	Third_party_plus = models.BooleanField(default=False)
	Without_deductible = models.BooleanField(default=False)
	Only_Localy_coverd = models.BooleanField(
	default=False,)
	Towing_system = models.BooleanField(default=False)
	accident_hist4thelast2years = models.CharField(max_length=20)
	was_your_previous_policy_canceled = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.sub_id}"