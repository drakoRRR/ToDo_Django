from django.test import SimpleTestCase
from django.urls import reverse, resolve
from todo.views import main_page, create_task, delete_task, sort_tasks

class TestUrls(SimpleTestCase):
    def test_main_url_is_resolved(self):
        url = reverse('main')
        self.assertEquals(resolve(url).func, main_page)

    def test_create_task_url_is_resolved(self):
        url = reverse('create')
        self.assertEquals(resolve(url).func, create_task)

    def test_delete_task_url_is_resolved(self):
        url = reverse('delete_task', args=[1])
        self.assertEquals(resolve(url).func, delete_task)

    def test_sort_tasks_url_is_resolved(self):
        url = reverse('sort_tasks')
        self.assertEquals(resolve(url).func, sort_tasks)