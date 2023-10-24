from django.urls import path
from. import views
urlpatterns =[
    path('',views.Home,name="welcome to emobilis"),
    path('about',views.about,name="about emobilis")
]