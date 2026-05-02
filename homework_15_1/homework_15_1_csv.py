"""Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх.
Результат запишіть у файл result_<your_second_name>.csv"""

import csv
import pandas as pd

# way_1
file_1 = pd.read_csv("r-m-c.csv")
file_2 = pd.read_csv("random-michaels.csv")

united_file = pd.concat([file_1, file_2])

united_file.to_csv("result_Ponomarov.csv", index=False)

# way_2
with open("r-m-c.csv", "r") as f:
    reader_1 = list(csv.reader(f))

with open("random-michaels.csv.", "r") as f:
    reader_2 = list(csv.reader(f))

united_file_2 = []

all_data = reader_1 + reader_2

for row in all_data:
    if row not in united_file_2:
        united_file_2.append(row)

with open("result_Ponomarov_1.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(united_file_2)
