from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    #記事関連
    path('article-list/',views.ArticleListView.as_view(),name="article_list"),
    path('article-detail/<int:pk>/',views.detail,name="article_detail"),
    path('article-create/',views.ArticleCreateView.as_view(),name="article_create"),
    path('article-update/<int:pk>/',views.ArticleUpdateView.as_view(),name="article_update"),
    path('article-delete/<int:pk>/',views.ArticleDeleteView.as_view(),name="article_delete"),

    #コメント関連
    path('comment-create/<int:num>/',views.CommentCreateView.as_view(),name="comment_create"),


]
