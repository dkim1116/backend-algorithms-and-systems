# 1. Only users in "USA"

# 2. Age > 30

# 3. Sorted by salary (descending)

# 4. Return this format:
# [
#     {"name": "Charlie", "salary": 150000},
# ]
import csv

def process_csv(file_path):
    result = []

    with open(file_path, newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                country = row["country"]
                age = row["age"]
                salary = row["salary"]
                name = row["name"]
            except (ValueError, KeyError):
                continue

            if country == "USA" and int(age) > 30:
                result.append({
                    "name": name,
                    "salary": int(salary)
                })
    result.sort(key=lambda x: x["salary"], reverse=True)
    print(result)
    return result

if __name__ == '__main__':
    process_csv("./data.csv")