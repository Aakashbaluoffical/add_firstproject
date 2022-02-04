
from django.urls import path
from . import views
from todo.core.views import home

urlpatterns = [

    path('',views.home,name="name"),
]
