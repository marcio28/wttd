# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r

class HomepageTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:homepage'))

    def test_get(self):
        'GET / deve retornar status code 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Homepage deve usar template index.html'
        self.assertTemplateUsed(self.resp, 'index.html')
