import connexion
import six
from typing import List
from swagger_server.models.appointment_item import AppointmentItem  # noqa: E501
from swagger_server import util
from flask import abort

users_appointments = {}
appointments_validation = {}
def add_appointment(body=None):  # noqa: E501
    """adds an appointment

    Adds an appointment to the system # noqa: E501

    :param body: Appointment to add
    :type body: dict | bytes

    :rtype: None
    """
    global appointments_validation
    global users_appointments
    if connexion.request.is_json:
        body = AppointmentItem.from_dict(connexion.request.get_json())  # noqa: E501

        if not(body.start_date.strftime("%M") in ("00","30") and body.start_date.strftime("%S") == "00"):
            return abort(409, "All appointments must start and end on the hour or half hour")
        start_date_truncated = body.start_date.replace(minute=0, hour=0, second=0, microsecond=0)
        user_key = str(body.user_id)
        if body.user_id not in appointments_validation:
            appointments_validation[user_key] = []
        if body.user_id not in users_appointments:
            users_appointments[user_key] = []

        if start_date_truncated not in appointments_validation[user_key]:
            appointments_validation[user_key].append(start_date_truncated)
        else:
            return abort(409, "For the user " + user_key + " an appointment has been created for that date: " + start_date_truncated.strftime("%Y-%m-%d"))
        users_appointments[user_key].append(body)
        return body 
    else:
        return abort(400)



def list_appointments(user_id):  # noqa: E501
    """searches scheduled appointments

    By passing the userId, you can search for all the appointments available for the user  # noqa: E501

    :param user_id: pass an User Id for retrieve all the appointments availables
    :type user_id: str

    :rtype: List[AppointmentItem]
    """
    global users_appointments
    user_key = str(user_id)
    if user_key not in users_appointments:
        users_appointments[user_key] = []
    return users_appointments[user_key]
