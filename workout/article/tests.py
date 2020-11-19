from django.test import TestCase, Client
from django.urls import reverse_lazy
from .models import Article, Comment
from accounts.models import CustomUser
from django.contrib.auth import get_user_model

# Create your tests here.
class TestArticleList(TestCase):
    def test_get(self):
        Article.objects.create(title="test", content="this is test")
        Article.objects.create(title="test2", content="this is test2")

        res = self.client.get(reverse_lazy('article:article_list'))

        self.assertTemplateUsed(res, 'article_list.html')
        self.assertContains(res, 'test')
        self.assertContains(res, 'this is test')
        self.assertEqual(len(res.context['article_list']), 2)


class TestArticleDetail(TestCase):
    def test_get(self):
        Article.objects.create(id=1, title="test", content="this is test")

        res = self.client.get(reverse_lazy('article:article_detail', args=(1,)))
        
        self.assertTemplateUsed(res, 'article_detail.html')
        self.assertContains(res, 'test')
        self.assertContains(res, 'this is test')

    def test_error(self):
        res = self.client.get(reverse_lazy('article:article_detail', args=(1,)))
        self.assertEqual(res.status_code, 404)

    def test_sort(self):
        article = Article.objects.create(id=1, title="test", content="this is test")
        Comment.objects.create(article=article, comment='comment')
        Comment.objects.create(article=article, comment='comment2')
        res = self.client.get(reverse_lazy('article:article_detail', args=(1,)))
        self.assertGreaterEqual(res.context['comments'][0].created_at, res.context['comments'][1].created_at)

class LoggedInTestCase(TestCase):
    def setUp(self):
        self.password = 'password'
        self.test_user = get_user_model().objects.create_user(
            username='name',
            password=self.password
        )

        self.client.login(username=self.test_user.username, password=self.password)

class TestArticleCreate(LoggedInTestCase):
    def test_create(self):
        params = {'photo': '',
                  'title': 'テストタイトル',
                  'content': '内容'
                  }
        res = self.client.post(reverse_lazy('article:article_create'), params)
        
        self.assertRedirects(res, reverse_lazy('article:article_list'))

        self.assertEqual(Article.objects.filter(title='テストタイトル').count(), 1)

    def test_create_failure(self):
        res = self.client.post(reverse_lazy('article:article_create'))
        self.assertFormError(res, 'form', 'title','このフィールドは必須です。')

class TestDiaryUpdate(LoggedInTestCase):
    def test_update(self):
        article = Article.objects.create(user=self.test_user, title='before')
        params = {'title': 'after'}
        
        res = self.client.post(reverse_lazy('article:article_update', kwargs={'pk': article.pk}), params)
        self.assertRedirects(res, reverse_lazy('article:article_detail', kwargs={'pk': article.id}))
        self.assertEqual(Article.objects.get(pk=article.pk).title, 'after')

    def test_update_failure(self):
        res = self.client.post(reverse_lazy('article:article_update', kwargs={'pk': 10}))
        self.assertEqual(res.status_code, 404)
