import pytest
import requests
from requests.auth import HTTPBasicAuth
import logging
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("HOMEWORK_24_FLASK_BASE_URL")


def pytest_configure(config):
    logger = logging.getLogger("test_search")
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler("test_search.log", mode="w")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)


@pytest.fixture
def auth_session():
    logger = logging.getLogger("test_search")
    logger.info("Session setup")
    session = requests.Session()

    try:
        auth_url = f"{BASE_URL}/auth"
        logger.info(f"Sending POST request to login to {auth_url}")

        response = session.post(auth_url, auth=HTTPBasicAuth("test_user", "test_pass"))

        assert response.status_code == 200, f"Auth problem: {response.text}"

        token = response.json().get("access_token")
        assert token

        session.headers.update({"Authorization": f"Bearer {token}"})
        logger.info("Auth successful")

        yield session

    except Exception as e:
        logger.error(f"Something went wrong: {e}")
        raise e
    finally:
        logger.info("Closing session")
        session.close()
