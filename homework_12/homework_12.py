from unittest import TestCase, main
from homework_12.test_data import tom_sawer_lower
from homework_12.test_data import h_repeats_in_original_text
from homework_12.test_data import car_list_filtering
from homework_12.test_data import lists_operations
from homework_12.test_data import uniq_characters_count
from homework_9.homework_9 import input_data
from homework_8.homework_8 import student_1
from unittest.mock import patch


class TestTomSawer(TestCase):
    def test_lower_case(self):
        result = tom_sawer_lower()
        self.assertEqual(result, result.lower(), f"Text is not in lower case")

    def test_no_integers_in_text(self):
        result = tom_sawer_lower()
        single_letters = any(char.isdigit() for char in result)
        self.assertFalse(single_letters, f"There are digits in the text")

    def test_fixed_count_h(self):
        result = h_repeats_in_original_text()
        self.assertEqual(result, 40, f"There are no 40 letters " "h" " in the text")


class TestCarFiltering(TestCase):
    def test_filter_limit_is_five(self):
        result = len(car_list_filtering())
        self.assertEqual(result, 5, f"There are no 5 items in the list")

    def test_car_price_limit(self):
        result = car_list_filtering()
        car_prices = []
        for car in result:
            car_prices.append(car[1])
        self.assertTrue(
            all(price <= 36000 for price in car_prices),
            f"Filtering result contain cars with price" f" more then 36000",
        )

    def test_list_sorting(self):
        result = car_list_filtering()
        expected_sorting = sorted(result, key=lambda item: item[1])
        self.assertEqual(result, expected_sorting, f"List is not sorted")


class TestListOperations(TestCase):
    def test_data_valid_format(self):
        result = lists_operations()
        self.assertTrue(
            all(isinstance(a, str) for a in result), f"Not all list items are strings"
        )


class TestGeometryFigure(TestCase):
    def test_correct_angle_b_calculation(self):
        angle_b_value = input_data.angle_b_calculation()
        angle_b_correct_value = 180 - input_data.angle_a
        self.assertEqual(
            angle_b_value, angle_b_correct_value, f"Angle b value is wrong"
        )


class TestStudentData(TestCase):
    def test_new_grade_updates(self):
        original_grade = student_1.average_grade
        new_grade_value = 50
        student_1.new_grade(new_grade_value)
        self.assertNotEqual(original_grade, new_grade_value)


class TestUniqCharacters(TestCase):
    @patch("builtins.input", return_value="qwertyuiop[")
    def test_more_than_ten_unique(self, mock_input):
        result = uniq_characters_count()
        self.assertTrue(result)

    @patch("builtins.input", return_value="qwertyuio")
    def test_less_than_ten_unique(self, mock_input):
        result = uniq_characters_count()
        self.assertFalse(result)


if __name__ == "__main__":
    main()
