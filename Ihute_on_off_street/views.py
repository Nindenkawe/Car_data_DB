from contextvars import Context
from distutils.log import error
from django.http import Http404, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import reverse
from django.shortcuts import redirect, render
from .decoretors import allowed_users
from .forms import Registration_Form, rqst_chauffeur
from .serializers import *
from .models import *

@login_required(login_url='signin')
@allowed_users(allowed_roles=['Admin'])
def Dashboard(request):
    user_name = Subscriber.objects.all()
    Provider_data = Provider.objects.all()
    Transaction_data = Transaction.objects.all()
    context = {
        "user_name":user_name, 
        "Transaction_data":Transaction_data, 
        "Provider_data":Provider_data,
        }
    return render(request,"ihute/Dashboard.html", context)


def register(request):
    form = Registration_Form()
    if request.method == "POST":
        form = Registration_Form(request.POST)
        if form.is_valid():
            user = form.save()
            sub_id = form.cleaned_data.get('username')
            group = Group.objects.get(name='subscriber')
            user.groups.add(group)
            messages.success(request, 'succesfully registerd' + sub_id)
            return redirect("signin")
    return render(request, "ihute/signup.html", {"form": form})


def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("Dashboard"))
        else:
            return redirect(request, "ihute/signin.html",{
                "message":"invalid credetials."
            })
    return render(request, "ihute/signin.html")

def signout(request):
    logout(request)
    return render(request, "ihute/signin.html", {"message":"Signed out"})


@api_view(['GET'])
@login_required(login_url='signin')
@allowed_users(allowed_roles=['Admin'])
def get_sub_profile(request, pk):
    try:
        profile = Subscriber.objects.get(id = pk)
    except Exception as e:
        raise Http404
    profile = SubscriberSerializer(profile, many=False)
    return Response(profile.data)

@api_view(['GET','POST'])
def book_chauffeur(request): 
    submitted = False
    if request.method == "POST":
        form = rqst_chauffeur(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/Ihute_on_off_street/testcharts?submitted=True')
    else:
        form = rqst_chauffeur
        if submitted in request.GET:
            submitted = True
    return Response(request, "ihute/testcharts.html", {'form':form, 'submitted':submitted})   


@login_required(login_url='signin')
@api_view(['GET','POST'])
def Buyinsurance(request):
    if request.method == "POST":
        insuranceForm = Proposed_insucoversSerializer(data=request.data)
        if insuranceForm.is_valid():
            insuranceForm.save()
    print(request.data)
    
    buy_insurance = TransactionSerializer(data=request.data)
    if buy_insurance.is_valid():
        buy_insurance.save()
    Insurance_Premiums = Insurance_Premiums.objects.all()
    return Response(Insurance_Premiums)
