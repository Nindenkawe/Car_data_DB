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
from .serializers import SubscriberSerializer
from .models import *

@login_required(login_url='signin')
@allowed_users(allowed_roles=['Admin'])
def Dashboard(request):
    return render(request,"ihute/Dashboard.html")



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


@api_view(['GET','POST'])
@login_required(login_url='signin')
@allowed_users(allowed_roles=['Admin'])
def get_sub_profile(request, id):
    try:
        subscriber = Subscriber.objects.all()
        profile = Subscriber.objects.get(sub_id = id)
    except Exception as e:
        raise Http404
    subscriber = SubscriberSerializer(profile, many=True)
    return Response(subscriber.data)

def book_chauffeur(request): 
    submitted = False
    if request.method == "POST":
        form = rqst_chauffeur(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/Ihute_on_off_street/services?submitted=True')
    else:
        form = rqst_chauffeur
        if submitted in request.GET:
            submitted = True
    return render(request, "ihute/services.html", {'form':form, 'submitted':submitted})   