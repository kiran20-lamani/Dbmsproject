from django.db import models
from decimal import Decimal
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class instruments(models.Model):
	inst_id= models.AutoField(primary_key=True)
	def individual():
		return 'some string'
	inst_name= models.CharField(max_length=30,default=individual)
	cost= models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('00000000.00'),validators=[MinValueValidator(Decimal('0.01'))])
	class Meta:
		db_table= "instruments"

class departments(models.Model):
	dept_id= models.AutoField(primary_key=True)
	def individual():
		return 'some string'
	dept_name= models.CharField(max_length=30,default=individual)
	class Meta:
		db_table= "departments"

class contracts(models.Model):
	con_id= models.AutoField(primary_key=True)
	def individual():
		return 'some string'
	con_com= models.CharField(max_length=30,default=individual)
	con_amt= models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('00000000.00'),validators=[MinValueValidator(Decimal('0.01'))])
	con_equip= models.CharField(max_length=30,default=individual)
	class Meta:
		db_table= "contracts"

class order(models.Model):
	ord_id= models.AutoField(primary_key=True)
	Inst_id= models.ForeignKey(instruments,on_delete=models.CASCADE)
	Con_id= models.ForeignKey(contracts, on_delete=models.CASCADE)
	Dept_id= models.ForeignKey(departments, on_delete=models.CASCADE)
	ord_quan= models.IntegerField(default=0,validators=[MinValueValidator(1)])
	class Meta:
		db_table= "orders"

class stock(models.Model):
	st_id= models.AutoField(primary_key=True)
	order_id= models.ForeignKey(order, on_delete=models.CASCADE)
	depa_id= models.ForeignKey(departments, on_delete=models.CASCADE)
	quantity= models.IntegerField(default=0,validators=[MinValueValidator(1)])
	class Meta:
		db_table= "stocks"