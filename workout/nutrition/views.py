from django.shortcuts import render,redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import Http404,JsonResponse

from .forms import NutritionForm
# Create your views here.
def nutrition(request):
    if request.method=='POST':
        form = NutritionForm(request.POST)
        if form.is_valid():
            common = 0.0481*float(request.POST['weight'])+0.0234*float(request.POST['height'])-0.0138*float(request.POST['age'])
            if request.POST['sex']=='man':
                calory=(common-0.4235)*1000/4.186
            else:
                calory=(common-0.9708)*1000/4.186
            maintenance=calory*float(request.POST['style'])

            diet = maintenance-500
            protein = int(diet*0.3)
            carbo = int(diet*0.5)
            fat = int(diet*0.2)
            pro_g = int(protein/4)
            carbo_g = int(carbo/4)
            fat_g = int(fat/9)

            data = {'calory':int(calory),'maintenance':int(maintenance),'diet':int(diet),'protein':protein,'carbo':carbo,'fat':fat,'pro_g':pro_g,'carbo_g':carbo_g,'fat_g':fat_g}
            return render(request,'nutrition.html',data)
    else:
        form = NutritionForm()
    return render(request,'nutrition.html',{'form':form})
