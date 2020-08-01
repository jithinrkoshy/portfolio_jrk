from django.urls import path
from pf_home import views


app_name = 'pf_home'

urlpatterns = [

    path('',views.home_page,name="home_page"),

]