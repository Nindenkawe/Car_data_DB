from django.urls import path
from . import views

urlpatterns = [
    path("", views.Dashboard, name="Dashboard"),
    path("signup", views.register, name="signup"),
    path("signin", views.signin, name="signin"),
    path("signout", views.signout, name="signout"),
    path("signout", views.signout, name="signout"),
    path("Buyinsurance", views.Buyinsurance, name="Buyinsurance"),
    path("book_chauffeur", views.book_chauffeur, name="book_chauffeur"),
    path('get_sub_profile/<int:pk>', views.get_sub_profile, name='get_sub_profile'),
]