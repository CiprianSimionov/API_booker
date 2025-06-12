import unittest

from requests_folder.booking_requests import get_all_booking_ids, get_booking_by_id, create_booking, update_booking, \
    partial_update_booking, delete_booking, health_check


class TestBookings(unittest.TestCase):
    def test_get_all_bookings(self):
        get_bookings_response = get_all_booking_ids()
        assert get_bookings_response.status_code == 200

    def test_get_booking_by_id(self):
        booking_info = {
            "checkin": "2025-06-17",
            "checkout": "2025-06-25"
        }
        create_booking_response = create_booking("Marry", "Jones", 4000, True,
                                                 bookingdate=booking_info, additionalneeds="large breakfast")
        booking_id = create_booking_response.json()["bookingid"]
        get_booking_by_id_response = get_booking_by_id(booking_id)
        assert get_booking_by_id_response.status_code == 200
        assert get_booking_by_id_response.json()["firstname"] == "Marry"
        assert get_booking_by_id_response.json()["lastname"] == "Jones"
        assert get_booking_by_id_response.json()["totalprice"] == 4000
        assert get_booking_by_id_response.json()["depositpaid"] == True
        assert get_booking_by_id_response.json()["bookingdates"]["checkin"] == "2025-06-17"
        assert get_booking_by_id_response.json()["bookingdates"]["checkout"] == "2025-06-25"
        assert get_booking_by_id_response.json()["additionalneeds"] == "large breakfast"

    def test_create_booking(self):
        booking_info = {
            "checkin": "2025-08-14",
            "checkout": "2025-08-21"
        }
        create_booking_response = create_booking("Alice", "Park", 4500, True,
                                                 bookingdate=booking_info, additionalneeds="extra towels")
        assert create_booking_response.status_code == 200
        assert create_booking_response.json()["booking"]["firstname"] == "Alice"
        assert create_booking_response.json()["booking"]["totalprice"] == 4500
        assert create_booking_response.json()["booking"]["bookingdates"]["checkout"] == "2025-08-21"
        assert create_booking_response.json()["booking"]["additionalneeds"] == "extra towels"

    def test_update_booking(self):
        booking_info = {
            "checkin": "2026-09-12",
            "checkout": "2026-09-18"
        }
        create_booking_response = create_booking("Mark", "Twain", 7500, False,
                                                 bookingdate=booking_info, additionalneeds="sea view")
        booking_id = create_booking_response.json()["bookingid"]
        update_booking_response = update_booking(booking_id, "Marcus", "Twain", 7500, True,
                                                 bookingdate=booking_info, additionalneeds="extra icecream")
        assert update_booking_response.status_code == 200
        assert update_booking_response.json()["firstname"] == "Marcus"
        assert update_booking_response.json()["totalprice"] == 7500
        assert update_booking_response.json()["depositpaid"] == True
        assert update_booking_response.json()["bookingdates"]["checkout"] == "2026-09-18"
        assert update_booking_response.json()["additionalneeds"] == "extra icecream"

    def test_partial_update_booking(self):
        booking_info = {
            "checkin": "2025-10-15",
            "checkout": "2025-10-19"
        }
        create_booking_response = create_booking("Marcus", "Twain", 9000, True,
                                                 bookingdate=booking_info, additionalneeds="extra beer")
        booking_id = create_booking_response.json()["bookingid"]
        partial_update_booking_response = partial_update_booking(booking_id, 9500, True, "late breakfast")
        assert partial_update_booking_response.status_code == 200
        assert partial_update_booking_response.json()["totalprice"] == 9500
        assert partial_update_booking_response.json()["depositpaid"] == True
        assert partial_update_booking_response.json()["additionalneeds"] == "late breakfast"

    def test_delete_booking(self):
        booking_info = {
            "checkin": "2025-06-17",
            "checkout": "2025-06-25"
        }
        create_booking_response = create_booking("Alex", "Correcia", 3600, True,
                                                 bookingdate=booking_info, additionalneeds="early bird")
        booking_id = create_booking_response.json()["bookingid"]
        delete_booking_response = delete_booking(booking_id)
        assert delete_booking_response.status_code == 201, delete_booking_response.status_code

    def test_delete_booking_already_deleted(self):
        booking_info = {
            "checkin": "2025-06-17",
            "checkout": "2025-06-25"
        }
        create_booking_response = create_booking("Stan", "Smith", 1000, True,
                                                 bookingdate=booking_info, additionalneeds="early bird")
        booking_id = create_booking_response.json()["bookingid"]
        delete_booking(booking_id)
        delete_booking_response = delete_booking(booking_id)
        assert delete_booking_response.status_code == 405

    def test_health_check(self):
        health_check_response = health_check()
        assert health_check_response.status_code == 201
