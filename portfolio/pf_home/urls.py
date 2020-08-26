from django.urls import path
from pf_home import views


app_name = 'pf_home'

urlpatterns = [

    path('',views.home_page,name="home_page"),
    path('portfolio',views.portfolio,name="portfolio"),
    path('portfolio/about',views.about,name="about"),
    path('portfolio/contact',views.contact,name="contact"),
    path('portfolio/contact/<str:parameter>/',views.contact,name="contact_second"),
    path('portfolio/process',views.process,name="process"),
    

]