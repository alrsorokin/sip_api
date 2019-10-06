import secrets
import time

from base64 import b64encode
from datetime import datetime

from flask_testing import TestCase

from sip_api.app import app, db
from sip_api.models import Call, Operator, User
from sip_api.lib import const as c


class TestBase(TestCase):

    def create_app(self):
        return app

    def setUp(self):
        db.create_all()
        User(login='test', password='test', token='test').save()
        self.headers = {
            'Authorization': 'Bearer test'
        }
        self._setTestData()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def _setTestData(self):
        pass


class TestHealthCheck(TestBase):
    def test_health_check(self):
        response = self.client.get('/api/v1/health-check')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'OK')


class TestAuth(TestBase):
    def test_auth(self):
        headers = {
            'Authorization': 'Basic ' + b64encode(bytes("test:test", 'ascii')).decode('ascii')
        }
        response = self.client.get("/users", headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json['token'])


class TestGetEmptyOperatorList(TestBase):
    def test_get_operators(self):
        response = self.client.get('/api/v1/operators', headers=self.headers)
        self.assertEqual(response.status_code, 200)

        operators = response.json['operators']
        self.assertEqual(len(operators), 0)


class TestGetOperatorList(TestBase):
    def _setTestData(self):
        for i in range(0, 10):
            Operator(phone_number=f'92{i}', name=f'operator_{i}').save()

    def test_get_operators(self):
        response = self.client.get('/api/v1/operators', headers=self.headers)
        self.assertEqual(response.status_code, 200)

        operators = response.json['operators']
        self.assertEqual(len(operators), 10)
        for i in range(0, 10):
            self.assertEqual(operators[i]['phone_number'], f'92{i}')
            self.assertEqual(operators[i]['name'], f'operator_{i}')


class TestGetEmptyCallList(TestBase):
    def test_get_calls(self):
        response = self.client.get('/api/v1/calls', headers=self.headers)
        self.assertEqual(response.status_code, 200)

        calls = response.json['calls']
        self.assertEqual(len(calls), 0)


class TestGetCallList(TestBase):
    def _setTestData(self):
        for i in range(0, 10):
            operator = Operator(phone_number=f'92{i}', name=f'operator_{i}').save()
            Call(
                id=secrets.token_hex(nbytes=16),
                type=c.CALL_TYPES['OUTGOING'],
                date=int(time.mktime(datetime.now().replace(hour=i).timetuple())),
                duration_answer=5,
                status=c.CALL_STATUSES['ACCEPTED'],
                phone_number_client='88005553535',
                phone_number_operator=operator.phone_number
            ).save()

    def test_get_calls(self):
        response = self.client.get('/api/v1/calls', headers=self.headers)
        self.assertEqual(response.status_code, 200)

        calls = response.json['calls']
        self.assertEqual(len(calls), 10)

        for i in range(0, 10):
            self.assertEqual(calls[i]['phone_number_operator'], f'92{i}')

    def test_get_call_with_params(self):
        date_from = int(time.mktime(datetime.now().replace(hour=0, minute=0).timetuple()))
        date_till = int(time.mktime(datetime.now().replace(hour=5, minute=0).timetuple()))
        response = self.client.get(f'/api/v1/calls?date_from={date_from}&date_till={date_till}',
                                   headers=self.headers)

        self.assertEqual(response.status_code, 200)

        calls = response.json['calls']
        self.assertEqual(len(calls), 5)

    def test_get_empty_call_list(self):
        date_from = int(time.mktime(datetime.now().replace(hour=12).timetuple()))
        date_till = int(time.mktime(datetime.now().replace(hour=23, minute=59).timetuple()))

        response = self.client.get(f'/api/v1/calls?date_from={date_from}&date_till={date_till}',
                                   headers=self.headers)
        self.assertEqual(response.status_code, 200)

        calls = response.json['calls']
        self.assertEqual(len(calls), 0)


class TestRecording(TestBase):
    def _setTestData(self):
        for i in range(0, 1):
            operator = Operator(phone_number=f'92{i}', name=f'operator_{i}').save()
            Call(
                id=i,
                type=c.CALL_TYPES['OUTGOING'],
                date=int(time.mktime(datetime.now().replace(hour=i).timetuple())),
                duration_answer=5,
                status=c.CALL_STATUSES['ACCEPTED'],
                phone_number_client='88005553535',
                phone_number_operator=operator.phone_number
            ).save()

    def test_get_recording_success(self):
        response = self.client.get('/api/v1/recording?call_id=0', headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'audio/wav')
        self.assertIsNotNone(response.data)

    def test_get_recording(self):
        response = self.client.get('/api/v1/recording?call_id=test', headers=self.headers)
        self.assertEqual(response.status_code, 400)
