import requests


def get_all_booking_ids():
    response = requests.get("https://restful-booker.herokuapp.com/booking")
    return response


def get_booking_by_id(booking_id):
    response = requests.get(f"https://restful-booker.herokuapp.com/booking/{booking_id}")
    return response


# print(get_booking_by_id(4))


def create_booking(firstname, lastname, totalprice, depositpaid, bookingdate, additionalneeds):
    data = {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": totalprice,
        "depositpaid": depositpaid,
        "bookingdates": {
            "checkin": bookingdate["checkin"],
            "checkout": bookingdate["checkout"]
        },
        "additionalneeds": additionalneeds
    }
    response = requests.post("https://restful-booker.herokuapp.com/booking", json=data)
    return response


def update_booking(booking_id, firstname, lastname, totalprice, depositpaid, bookingdate, additionalneeds):
    username = "admin"
    password = "password123"
    data = {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": totalprice,
        "depositpaid": depositpaid,
        "bookingdates": {
            "checkin": bookingdate["checkin"],
            "checkout": bookingdate["checkout"]
        },
        "additionalneeds": additionalneeds
    }
    response = requests.put(f"https://restful-booker.herokuapp.com/booking/{booking_id}", json=data,
                            auth=(username, password))
    return response


def partial_update_booking(booking_id, totalprice, depositpaid, additionalneeds):
    username = "admin"
    password = "password123"
    data = {
        "totalprice": totalprice,
        "depositpaid": depositpaid,
        "additionalneeds": additionalneeds
    }
    response = requests.patch(f"https://restful-booker.herokuapp.com/booking/{booking_id}", json=data,
                              auth=(username, password))
    return response


def delete_booking(booking_id):
    username = "admin"
    password = "password123"
    response = requests.delete(f"https://restful-booker.herokuapp.com/booking/{booking_id}", auth=(username, password))
    return response


def health_check():
    response = requests.get("https://restful-booker.herokuapp.com/ping")
    return response
