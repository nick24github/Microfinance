from django.db import models

class User_Registration(models.Model):
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)
    Confirm_Password = models.CharField(max_length=30)
    Gender = models.CharField(max_length=30,choices=(('Male','Male'),('Female','Female')))
    Address = models.CharField(max_length=100)
    Image = models.ImageField(upload_to="media",default=False)
    Email = models.EmailField()
    phone_number = models.IntegerField()
    loantype = models.CharField(max_length=50 ,choices=(('Education','Education'),('Cultivation','Cultivation'),('Home','Home'),('Home','Home')))

class User_Register2(models.Model):
    Bank_Name = models.CharField(max_length=30)
    Bank_ACNO = models.IntegerField()
    Branch = models.CharField(max_length=30)
    Profession = models.CharField(max_length=30)
    Security_document = models.ImageField(upload_to='media')

class Admin(models.Model):
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)

class UserPayment(models.Model):
    Loan_Id = models.IntegerField(primary_key=True)
    Installment_amount = models.IntegerField()
    Payment = models.CharField(max_length=30,choices=(('Netbanking','Netbanking'),('Debit Card','Debit Card'),('Credit Card','Credit Card')))

class Assistance(models.Model):
    org_name = models.CharField(max_length=30)
    issue_amnt = models.IntegerField()
    org_type = models.CharField(max_length=20,choices=(('Government','Government'),('Private','Private')))

class LoanCreation(models.Model):
    un = models.CharField(max_length=30)
    loan_id = models.IntegerField(primary_key=True)
    loan_amnt = models.IntegerField()
    loan_type = models.CharField(max_length=30)
    insta_no = models.IntegerField()
    insta_amnt = models.IntegerField()
    pay_date = models.DateField()