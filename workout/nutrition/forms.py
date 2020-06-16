from django import forms

class NutritionForm(forms.Form):
    choice_sex = (('man','男性'),('woman','女性'))
    choice_style = ((1.2,'デスクワークが中心の方'),(1.375,'出勤等で軽い運動を行う方'),(1.55,'立ち仕事や移動が多い方'),(1.725,'習慣的に運動や筋トレをされる方'),(1.9,'激しいトレーニング、肉体労働をされる方'))
    height=forms.FloatField(label="身長(cm)")
    weight=forms.FloatField(label="体重(kg)")
    age=forms.IntegerField(label="年齢")
    sex=forms.ChoiceField(choices=choice_sex,label="性別")
    style=forms.ChoiceField(choices=choice_style,label="生活スタイル")



