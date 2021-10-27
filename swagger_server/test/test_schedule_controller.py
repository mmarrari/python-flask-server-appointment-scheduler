# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.appointment_item import AppointmentItem  # noqa: E501
from swagger_server.test import BaseTestCase


class TestScheduleController(BaseTestCase):
    """ScheduleController integration test stubs"""

    def test_add_appointment(self):
        """Test case for add_appointment

        adds an appointment
        """
        body = AppointmentItem()
        response = self.client.open(
            '/mmarrari/scheduler/1.0.0/appointment',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_appointments(self):
        """Test case for list_appointments

        searches scheduled appointments
        """
        query_string = [('user_id', 'user_id_example')]
        response = self.client.open(
            '/mmarrari/scheduler/1.0.0/appointment',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
