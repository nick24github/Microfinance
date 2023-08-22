from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from app_MF.models import *


def Register(request):
    username = request.POST.get('uname')
    password = request.POST.get('password')
    confirm_password= request.POST.get('cpassword')
    gender= request.POST.get('gender')
    adress= request.POST.get('adress')
    image= request.FILES['image']
    email= request.POST.get('email')
    cno= request.POST.get('cno')
    loantype= request.POST.get('loan')
    if password==confirm_password:
        User_Registration(Username=username,Password=password,Confirm_Password=confirm_password,
                      Gender=gender,Address=adress,Image=image,Email=email,phone_number=cno,loantype=loantype).save()
        return render(request,"userregister2.html")
    else:
        return render(request,"userregister.html",{'msg':'Password does not match'})


def Register2(request):
    bankname  = request.POST.get('bname')
    acno = request.POST.get('acno')
    branch = request.POST.get('branch')
    profession = request.POST.get('prof')
    sec = request.POST.get('sec')
    User_Register2(Bank_Name=bankname,Bank_ACNO=acno,Branch=branch,Profession=profession,Security_document=sec).save()
    return render(request,"userregister2.html",{'msg':'Saved'})
def userlogin(request):
    username = request.POST.get('uname')
    password = request.POST.get('password')
    qs = User_Registration.objects.filter(Username=username,Password=password)
    if not qs:
        return render(request,'sign in.html',{'data':'Invalid User'})
    else:
        return render(request,'welcomeuser.html')
    return None
def AdminLogin(request):
    username = request.POST.get('uname')
    password = request.POST.get('password')
    # Admin(Username=username,Password=password).save()
    # return render(request,"admin.html")
    qs = Admin.objects.filter(Username=username,Password=password)
    if not qs:
        return render(request,"admin.html",{'msg':'Invalid'})
    else:
        return render(request,"Welcomeadmin.html")
def managerlogin(request):
    username = request.POST.get('uname')
    password = request.POST.get('password')
    if username == "manager" and password == "manager":
        return render(request,"Welcomemanager.html")
    else:
        return render(request,"manager.html",{'msg':'Invalid'})
class payments(CreateView):
    template_name = 'Repayment.html'
    model = UserPayment
    fields = ('Loan_Id','Installment_amount','Payment')
    success_url = '/payments/'
    success_messages = "Successfull"
class Cust_Details(ListView):
    template_name = "cust_det.html"
    model = User_Registration
    fields = ('userid','Username','Password','Gender','Adress','Image','Email','cno','loantype')
    success_url = '/cust_det/'

class assistance(CreateView,SuccessMessageMixin):
    template_name = 'Assistance.html'
    model = Assistance
    fields = ('org_name','issue_amnt','org_type')
    success_url = '/assistance/'
    success_message = 'Saved'
class Finance(ListView):
    template_name = 'Finace_Details.html'
    model = Assistance
    fields = ('org_name', 'issue_amnt','org_type')
    success_url = '/Finance_Details/'
def Loancreation(request):

    un = request.POST.get('un')
    loan_id = request.POST.get('loanid')
    loanamnt = request.POST.get('loan_amnt')
    loantype = request.POST.get('Loan_type')
    insta_no = request.POST.get('insta_no')
    insta_amnt = request.POST.get('insta_amnt')
    date = request.POST.get('date')
    LoanCreation(un = un,loan_id=loan_id,loan_amnt=loanamnt,loan_type=loantype,insta_no=insta_no,insta_amnt=insta_amnt,pay_date=date).save()
    return render(request,'Loancreation.html')

#
# def loan_hist(request):
#     # un = request.POST.get('un')
#     qs = LoanCreation.objects.all()
#     # if qs:
#     return render(request,'History_loans.html',{'data':qs})
#     # else:
#     #     return render(request,'welcomeuser.html')


def Payment_det(request):
    qs = UserPayment.objects.all()
    return render(request,'Payment.html',{'data':qs})


def Approve_loans(request):
    qs = User_Register2.objects.all()
    return render(request,'approve_loans.html',{'data':qs})


def manage_loan_hist(request):
    qs = LoanCreation.objects.all()
    return render(request,'manager loan_hist.html',{'data':qs})


def userfilter(request):
    loanid = request.POST.get('id')
    qs = LoanCreation.objects.filter(loan_id=loanid)
    print(qs)
    if qs:
        return render(request,'History_loans.html',{'data':qs})
    else:
       return render(request,'enterid.html',{'msg':'Invalid'})


def reject(request):
    return render(request,'approve_loans.html',{'msg':'Rejected'})