from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient


class MyInfoTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    @patch('myinfo.client.MyInfoPersonalClientV4.get_authorise_url')
    def test_auth_create_url(self, mock_auth_url):
        mock_auth_url.return_value = 'https://localhost.com/auth'
        res = self.client.get(reverse('myinfo_integration:auth'))
        self.assertEqual(res.status_code, 200)
        self.assertIn('auth_url', res.data)
        self.assertEqual(res.data['auth_url'], 'https://localhost.com/auth')
        self.assertIn('state', res.data)

    @patch('myinfo.client.MyInfoPersonalClientV4.retrieve_resource')
    def test_callback_success(self, mock_retrieve):
        mock_retrieve.return_value = {
            'name': {'value': 'ABNK Tester'},
            'sex': {'value': 'M'},
        }

        ses = self.client.session
        ses['myinfo_oauth_state'] = 'test_state'
        ses.save()
        
        res = self.client.get(
            reverse('myinfo_integration:callback'),
            {'code': 'test_code'}
        )
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data['name']['value'], 'ABNK Tester')
    
    def test_callback_no_code(self):
        res = self.client.get(reverse('myinfo_integration:callback'))
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.data['error'], 'Auth code is required')

    def test_callback_session_missing(self):
        res = self.client.get(
            reverse('myinfo_integration:callback'),
            {'code': 'test_code'}
        )

        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.data['error'], 'Invalid session')
    
    @patch('myinfo.client.MyInfoPersonalClientV4.retrieve_resource')
    def test_callback_auth_code_wrong(self, mock_retrieve):
        mock_retrieve.side_effect = Exception("Invalid auth code")
        ses = self.client.session
        ses['myinfo_oauth_state'] = 'test_state'
        ses.save()
        res = self.client.get(
            reverse('myinfo_integration:callback'),
            {'code': 'invalid_code'}
        )

        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.data['error'], 'Invalid auth code')
