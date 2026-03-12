# Given list of tuples (name, surname, age, profession, City location)

people_records = [
    ("John", "Doe", 28, "Engineer", "New York"),
    ("Alice", "Smith", 35, "Teacher", "Los Angeles"),
    ("Bob", "Johnson", 45, "Doctor", "Chicago"),
    ("Emily", "Williams", 30, "Artist", "San Francisco"),
    ("Michael", "Brown", 22, "Student", "Seattle"),
    ("Sophia", "Davis", 40, "Lawyer", "Boston"),
    ("David", "Miller", 33, "Software Developer", "Austin"),
    ("Olivia", "Wilson", 27, "Marketing Specialist", "Denver"),
    ("Daniel", "Taylor", 38, "Architect", "Portland"),
    ("Grace", "Moore", 25, "Graphic Designer", "Miami"),
    ("Samuel", "Jones", 50, "Business Consultant", "Atlanta"),
    ("Emma", "Hall", 31, "Chef", "Dallas"),
    ("William", "Clark", 29, "Financial Analyst", "Houston"),
    ("Ava", "White", 42, "Journalist", "San Diego"),
    ("Ethan", "Anderson", 36, "Product Manager", "Phoenix"),
]

# 1 - Add your new record o the beginning of the given list
people_records.insert(0, ("Dmytro", "Ponomarov", 30, "QA Engineer", "Kharkiv"))

# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
people_records[1], people_records[5] = people_records[5], people_records[1]

print(f"{'Name':<10} {'Second name':<12} {'Age':<5} {'Profession':<22} {'City'}\n")
for first, lastname, age, job, city in people_records:
    print(f"{first:<10} {lastname:<12} {age:<5} {job:<22} {city}")

# 3 - check that all people in modified list with records indexes 6, 10, 13 have age >=30. Print condition check result.
selected_person_index = [6, 10, 13]
selected_person = [people_records[record] for record in selected_person_index]
age_verification = all(person[2] >= 30 for person in selected_person)
print(age_verification)
