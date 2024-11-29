
from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
   path("index/", views.index, name="index"),
   path("landlord/", views.landlord, name="landlord"),
   path("students/", views.students, name="students"),
   path("hostel/", views.hostel, name="hostel"),
   path("register/", views.register, name="register"),
]
