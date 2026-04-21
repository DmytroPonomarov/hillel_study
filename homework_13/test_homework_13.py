import unittest
from homework_13.homework_13 import log_event


class TestLogEvent(unittest.TestCase):
    def setUp(self):
        with open("login_system.log", "w") as f:
            pass

    @staticmethod
    def last_log_info():
        with open("login_system.log", "r") as f:
            lines = f.readlines()
            return lines[-1]

    def test_log_event_success(self):
        log_event("user1", "success")
        last_log = self.last_log_info()
        self.assertIn("Login event - Username: user1, Status: success", last_log)

    def test_log_event_expired(self):
        log_event("user2", "expired")
        last_log = self.last_log_info()
        self.assertIn("Login event - Username: user2, Status: expired", last_log)

    def test_log_event_failed(self):
        log_event("user3", "failed")
        last_log = self.last_log_info()
        self.assertIn("Login event - Username: user3, Status: failed", last_log)


if __name__ == "__main__":
    unittest.main()
