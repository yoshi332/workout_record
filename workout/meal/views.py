from django.shortcuts import render, redirect
from .models import Meal
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.db.models import Q
from django.contrib import messages
from pykakasi import kakasi
from .Advice import make_advice
# Create your views here.

def top(request):

    #検索条件のクエリセット取得
    query = request.GET.get('query')
    #convert Kanji to Hiragana
    ka = kakasi()
    ka.setMode('J', 'H')
    conv = ka.getConverter()
    sub_query = conv.do(str(query))
    foods = Meal.objects.all().order_by("id")[:10]    
    if (query):
        foods = Meal.objects.filter(
             Q(food__icontains=query) | Q(food__icontains=sub_query)
        )


    
    add_list = request.session.get("add", {'id': [], 'name': [], 'gram': [], 'created_num':[], 'cnt': 0})

    #削除ボタンは押されたときにセッションから削除(重複があったら最初を削除)
    delete_id = request.GET.get('delete_id')
    if(delete_id):
        for i,target in enumerate(add_list['created_num']):
            if int(delete_id) == target:
                index = i
                add_list['id'].pop(index)
                add_list['name'].pop(index)
                add_list['gram'].pop(index)
                add_list['created_num'].pop(index)

                break
    
    #すべて削除ボタンが押されたときの処理
    all_delete = request.GET.get('all_delete')
    if(all_delete):
        add_list['id'].clear()
        add_list['name'].clear()
        add_list['gram'].clear()
        add_list['created_num'].clear()
        add_list['cnt'] = 0

    #指定された食品をsessionに追加する処理(重複を許す)
    gram = request.GET.get('gram')
    food_id = request.GET.get('food_id')

    if(gram and food_id):
        meal = Meal.objects.get(pk=int(food_id))
        add_list['id'].append(int(meal.id))
        add_list['name'].append(meal.food)
        add_list['gram'].append(int(gram))
        add_list['created_num'].append(add_list['cnt'])
        add_list['cnt'] += 1
        
    request.session["add"] = add_list
    
    display = []
    for i,n,g in zip(add_list['created_num'], add_list['name'],add_list['gram']):
        display.append((i,n,g))
    
    data = {'foods':foods, 'display':display}

    return render(request,'top.html',data)

def meal_cal(request):
    add_list = request.session.get("add", {'id': [], 'name': [], 'gram': [], 'created_num': [], 'cnt': 0})
    #追加された食材の栄養素を計算
    energy, protein, fat, carbo = 0,0,0,0
    for food_id, gram in zip(add_list['id'], add_list['gram']):
        food = Meal.objects.get(pk=food_id)
        energy += food.energy * gram
        protein += food.protein * gram
        fat += food.fat * gram
        carbo += food.carbo * gram

    #計算結果のセッション情報を取得
    reduce_info = request.session.get('reduce', {})
    #アドバイスの生成
    text = ""
    if reduce_info:
        text = make_advice(reduce_info, energy, protein, fat, carbo, text)

    nutrition = {'energy':int(energy), 'protein':int(protein), 'fat':int(fat), 'carbo':int(carbo), 'reduce_info': reduce_info, 'text': text}

    return render(request, 'meal_cal.html', nutrition)
