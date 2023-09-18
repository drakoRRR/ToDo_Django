from django.test import TestCase, Client
from django.urls import reverse
from todo.models import Task
import json

class TestViews(TestCase):
    def test_main_page_GET(self):
        client = Client()
        response = client.get(reverse('main'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/mainpage.html')