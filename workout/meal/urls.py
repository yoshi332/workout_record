from django.urls import path
from . import views

app_name = 'meal'

urlpatterns = [
    #記事関連
    path('',views.top,name="top"),
    path('meal-cal/', views.meal_cal, name="meal_cal"),
   
]
