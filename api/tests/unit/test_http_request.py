from api.utils.http_rest import HttpRest
from django.test import TestCase
import requests
import mock


class HttpRestTest(TestCase):

    def setUp(self):
        self.http = HttpRest()

    def test_get_request_without_url(self):

        try:
            self.http.execute_request()
            self.fail("Should be give Exception")
        except Exception as e:
            pass

    req = mock.Mock()
    req.ok = True
    req.status_code = 200
    
    @mock.patch('requests.get', mock.Mock(return_value=req))
    def test_get_request_200(self):

        parameter = HttpRest.parameter

        response = self.http.execute_request("http://www.mocky.io/v2/5185415ba171ea3a00704eed", method=HttpRest.method.GET, parameter=parameter)
        self.assertNotEqual(response, None)

    req = mock.Mock()
    req.ok = False
    req.status_code = 500

    @mock.patch('requests.get', mock.Mock(return_value=req))
    def test_get_request_500(self):

        parameter = self.http.parameter
        response = self.http.execute_request("http://www.mocky.io/v2/593805ba11000026156bb8b5", parameter=parameter)
        self.assertNotEqual(response, None)

    def test_get_timeout_error(self):

        try:
            parameter = self.http.parameter
            parameter.timeout = 0.0001
            self.http.execute_request("http://www.google.com.br", parameter=parameter)
            self.fail("Should be give Timeout Exception")
        except requests.exceptions.Timeout as e:
            pass
