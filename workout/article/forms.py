from .models import Article, Comment
from django import forms
class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('photo','title','content')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


