from django.urls import path
from . import views

app_name = 'nutrition'

urlpatterns = [
    #カロリー計算
    path('',views.nutrition,name="nutrition"),
]
