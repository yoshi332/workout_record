from django.test import TestCase, Client
from django.urls import reverse_lazy
# Create your tests here.
class TestNutrition(TestCase):

    def test_get(self):
        res = self.client.get(reverse_lazy('nutrition:nutrition'))
        self.assertTemplateUsed(res, 'nutrition.html')
    
    def test_post(self):
        res = self.client.post(reverse_lazy('nutrition:nutrition'),
                                data = {'height':'160', 'weight':'60', 'age':'20', 'sex':'man', 'style':'1.2'})
        expected_calory = 1416
        diet = 1200
        maintenance = 1700
        protein = 360
        self.assertEqual(expected_calory, res.context['calory'])
        self.assertEqual(diet, res.context['diet'])
        self.assertEqual(maintenance, res.context['maintenance'])
        self.assertEqual(protein, res.context['protein'])

    def test_post_invalid(self):
        res = self.client.post(reverse_lazy('nutrition:nutrition'),
                                data = {'height':'', 'weight':'char', 'age':'20', 'sex':'man', 'style':'1.2'})
        self.assertTemplateUsed(res, 'nutrition.html')
        self.assertFalse(res.context['form'].is_valid())
