import csv

CARS_CSV_FILE = "cars.csv"
BIRTH_MONTH_CSV_FILE = "birth.csv"

# тут мы просто читаем, как список


def read_csv_cars():
    with open(CARS_CSV_FILE) as f:
        csv_reader = csv.reader(f, delimiter=",")

        print(csv_reader)
        for line in csv_reader:
            print(line)
            print(line[1], line[4])


# Тут мы будем читать как словарь


def read_csv_cars_as_dict():
    with open(CARS_CSV_FILE) as f:
        csv_reader = csv.DictReader(f, delimiter=",")
        print("filednames", csv_reader.fieldnames)

        for row in csv_reader:
            print(row["Make"], row["Year"], row["Price"])


class FieldName:
    NAME = "name"
    MONTH = "month"
    DEPARTAMENT = "departament"


def write_csv_dict():
    fieldnames = [
        FieldName.NAME,
        FieldName.MONTH,
        FieldName.DEPARTAMENT,
    ]

    with open(BIRTH_MONTH_CSV_FILE, "w", newline="") as f:
        csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
        csv_writer.writeheader()

        row = {
            FieldName.DEPARTAMENT: "IT",
            FieldName.NAME: "John",
            FieldName.MONTH: "June",
        }

        csv_writer.writerow(row)


def main():
    # read_csv_cars()
    read_csv_cars_as_dict()
    write_csv_dict()


if __name__ == "__main__":
    main()
