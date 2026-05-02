"""Для файла ideas_for_test/work_with_xml/groups.xml
створіть функцію пошуку по group/number і повернення значення timingExbytes/incoming результат виведіть у консоль
через логер на рівні інфо"""

from pathlib import Path
import xmltodict
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def main_function(xml_path, group_numbers):

    with open(xml_path) as f:
        content = f.read()
        converted_file = xmltodict.parse(content)
        groups = converted_file["groups"]["group"]
        full_log = []
        for group in groups:
            if group["number"] in group_numbers:
                result = group["timingExbytes"]["incoming"]
                full_log.append(
                    logging.info(
                        f"For group with number {group['number']} timingExbytes/incoming data = {result}"
                    )
                )
        return full_log


current_path = Path(__file__)
xml_file_path = current_path.parent / "test_data" / "groups.xml"

search_group_num = ["0", "2", "4", "5"]


main_function(xml_file_path, search_group_num)
