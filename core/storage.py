import json
import os


class Storage:
    def __init__(self, file_path="history.json"):
        self.file_path = file_path

    def load(self):
        ## Читает все записи из файла. Возвращает список словарей
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []

    def add(self, date, reason, amount):
        ## Добавляет новую запись и сохраняет в файл
        records = self.load()
        records.append({"date": date, "reason": reason, "amount": amount})
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(records, file, ensure_ascii=False, indent=2)

    def total_balance(self):
        ## Считает сумму всех amount
        return sum(int(record["amount"]) for record in self.load())