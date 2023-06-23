from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('book/',views.book),
    path('menu/',views.menu),
    path('contact/',views.contact),
    path('order/',views.order)
    
]
