import csv
import openpyxl
from random import randint
from transliterate import translit
from datetime import date
import random


class QueryGenerator:
    def __init__(self):
        self.names = []
        self.phone = []

    def read_xslx(self):
        wb = openpyxl.load_workbook("my-calend.xlsx")
        ws = wb.active


        start_date = date.today().replace(day=1, month=1).toordinal()
        end_date = date.today().replace(year=2028).toordinal()

        is_first = True
        for row in ws.iter_rows(values_only=True):
            if is_first:
                is_first = False
            else:
                self.names.append(row[0])
                self.phone.append(row[1])

        return self

    def generate_insert_user(self):
        sql = "insert into user"
        raw = ''
        user_id = 0
        start_date = date.today().replace(day=1, month=1).toordinal()
        end_date = date.today().replace(year=2028).toordinal()

        for _ in range(1000):
            random_day = date.fromordinal(random.randint(start_date, end_date))
            name = self.names[randint(0, len(self.names) - 1)]
            card_num = ""
            for _ in range(4):
                card_num += str(randint(1000, 9999))
            phone_num = "7"
            for _ in range(2):
                phone_num += str(randint(10000, 99999))
            translit_name = translit(name, language_code='ru', reversed=True).replace("'", "")
            raw += f"('{phone_num}', '{name}', {user_id}, '{card_num}', {randint(100, 999)}, '{translit_name}', '{random_day}'),\n"

            user_id += 1

        return raw


if __name__ == '__main__':
    q = QueryGenerator()

    print(q.read_xslx().generate_insert_user())
