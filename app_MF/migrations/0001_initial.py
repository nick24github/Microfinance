# Generated by Django 2.1.4 on 2019-02-26 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Assistance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=30)),
                ('issue_amnt', models.IntegerField()),
                ('org_type', models.CharField(choices=[('Government', 'Government'), ('Private', 'Private')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='LoanCreation',
            fields=[
                ('un', models.CharField(max_length=30)),
                ('loan_id', models.IntegerField(primary_key=True, serialize=False)),
                ('loan_amnt', models.IntegerField()),
                ('loan_type', models.CharField(max_length=30)),
                ('insta_no', models.IntegerField()),
                ('insta_amnt', models.IntegerField()),
                ('pay_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User_Register2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bank_Name', models.CharField(max_length=30)),
                ('Bank_ACNO', models.IntegerField()),
                ('Branch', models.CharField(max_length=30)),
                ('Profession', models.CharField(max_length=30)),
                ('Security_document', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='User_Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=30)),
                ('Confirm_Password', models.CharField(max_length=30)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=30)),
                ('Address', models.CharField(max_length=100)),
                ('Image', models.ImageField(default=False, upload_to='media')),
                ('Email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('loantype', models.CharField(choices=[('Education', 'Education'), ('Cultivation', 'Cultivation'), ('Home', 'Home'), ('Home', 'Home')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserPayment',
            fields=[
                ('Loan_Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Installment_amount', models.IntegerField()),
                ('Payment', models.CharField(choices=[('Netbanking', 'Netbanking'), ('Debit Card', 'Debit Card'), ('Credit Card', 'Credit Card')], max_length=30)),
            ],
        ),
    ]
