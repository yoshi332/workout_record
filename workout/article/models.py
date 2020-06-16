from django.db import models
from accounts.models import CustomUser
# Create your models here.
class Article(models.Model):
    """記事用モデル"""
    user = models.ForeignKey(CustomUser,on_delete=models.PROTECT,blank=True,null=True)
    photo = models.ImageField(blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True,null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Comment(models.Model):
    """コメントモデル"""
    article = models.ForeignKey(Article,related_name='comments',on_delete=models.CASCADE,blank=True,null=True)
    comment = models.TextField(blank=True,null=True)
    created_at = models.DateField(auto_now_add=True)
