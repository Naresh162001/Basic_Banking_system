from django.db import models

# Create your models here.
class Customers(models.Model):
    name = models.CharField(db_column='Name', max_length=25)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=6)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age')  # Field name made lowercase.
    phone_no = models.CharField(db_column='Phone_no', max_length=10)  # Field name made lowercase.
    account_no = models.AutoField(db_column='Account_No', primary_key=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50)  # Field name made lowercase.
    balance = models.FloatField(db_column='Balance')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customers'

class History(models.Model):
    sender_name = models.CharField(db_column='Sender_Name', max_length=25)  # Field name made lowercase.
    sender_no = models.IntegerField(db_column='Sender_NO')  # Field name made lowercase.
    receiver_name = models.CharField(db_column='Receiver_Name', max_length=25)  # Field name made lowercase.
    receiver_no = models.IntegerField(db_column='Receiver_no')  # Field name made lowercase.
    date = models.DateField(db_column='Date',auto_now_add=True, blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'history'
