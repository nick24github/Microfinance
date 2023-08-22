"""Micro_Finance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView, CreateView, ListView
from Micro_Finance import settings
from django.conf.urls.static import static

from Micro_Finance.settings import MEDIA_ROOT
from app_MF import views
from app_MF.models import User_Registration, User_Register2, Assistance

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', TemplateView.as_view(template_name="home_sideindex.html")),
    path('aboutus/', TemplateView.as_view(template_name="about_us.html")),
    path('user/', TemplateView.as_view(template_name="user.html")),
    path('loan_hist/',TemplateView.as_view(template_name='enterid.html')),
    path('userfilter/',views.userfilter),
    path('Registration/', TemplateView.as_view(template_name="userregister.html")),
    # user register page2
    path('register2/', views.Register),
    path('saveuser/', views.Register2),

    # user login
    path('signin/', TemplateView.as_view(template_name='sign in.html')),
    path('user_signin/', views.userlogin),
    # path('loan_hist/', views.loan_hist),

    path('payments/', views.payments.as_view()),

    # admin login
    path('admin1/', TemplateView.as_view(template_name="admin.html")),

    # welcome admin
    path('Welcome_Admin/', views.AdminLogin),
    # Finance_Details
    path('Finance_Details/', views.Finance.as_view()),
    # Loan Creation
    path('loancreation/', TemplateView.as_view(template_name="Loancreation.html")),
    path('saveloan/',views.Loancreation),
    # assistance
    path('assistance/', views.assistance.as_view()),
    path('cust_det/', views.Cust_Details.as_view()),

    # manger login
    path('manager/', TemplateView.as_view(template_name="manager.html")),
    # weloome manager
    path('Welcome_Manager/', views.managerlogin),
    path('manage_loan_hist/',views.manage_loan_hist),

    path('Payment_det/',views.Payment_det),
    path('Approve_loans/',views.Approve_loans),
    path('approve/',TemplateView.as_view(template_name='approve.html')),
    path('reject/',views.reject)

]
if settings.DEBUG :
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)