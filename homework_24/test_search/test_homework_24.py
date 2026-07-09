import os

import pytest
import logging

logger = logging.getLogger("test_search")
BASE_URL = os.getenv("HOMEWORK_24_FLASK_BASE_URL")


class TestCarsSearch:

    @pytest.mark.parametrize(
        "sort_by, limit",
        [
            ("price", 5),
            ("year", 3),
            ("brand", 2),
            ("engine_volume", 10),
            (None, 5),
            ("price", None),
            (None, None),
        ],
    )
    def test_search_cars(self, auth_session, sort_by, limit):
        params = {}
        if sort_by is not None:
            params["sort_by"] = sort_by
        if limit is not None:
            params["limit"] = limit

        logger.info(f"Sorting by: {sort_by} with limit: {limit}")

        try:
            response = auth_session.get(f"{BASE_URL}/cars", params=params)
            logger.info(f"Response status: {response.status_code}")
            assert (
                response.status_code == 200
            ), f"Request failed {response.status_code}: {response.text}"

            data = response.json()

            logger.info(f"Number of cars: {len(data)}")
            if limit is not None:
                assert (
                    len(data) == limit
                ), f"Expected max cars: {limit}, response: {len(data)}"

            if sort_by is not None and len(data) > 1:
                actual_values = [car[sort_by] for car in data]
                expected_values = sorted(actual_values)
                assert actual_values == expected_values, f"Sorting by {sort_by} failed"
            logger.info(f"Cars successfully sorted by {sort_by}")

            logger.info(f"Test completed for: sort_by= {sort_by} and limit= {limit}")

        except Exception as e:
            logger.error(f"Something went wrong: {e}")
            raise e
