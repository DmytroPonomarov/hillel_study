"""Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json.
результат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log"""

import json
from pathlib import Path
import logging

logging.basicConfig(
    filename='json_Ponomarov.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

current_dir = Path(__file__)
test_data_dir = current_dir.parent / 'test_data'

json_files = [file for file in test_data_dir.iterdir() if file.suffix == '.json']
print(json_files)

for json_file in json_files:
    with open(json_file, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            logging.error(f"{json_file.name} file is invalid")