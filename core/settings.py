import json
import os


class Settings:
    def __init__(self, file_path="settings.json"):
        self.file_path = file_path

    ## Загружает настройки. Если файла нет — возвращает дефолт.
    def load(self):
        if not os.path.exists(self.file_path):
            return {"first_run": True}
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {"first_run": True}

    ## Сохраняет настройки в файл.
    def save(self, data):
         with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    ## Возвращает True, если это первый запуск.        
    def is_first_run(self):
        data = self.load()
        return data.get("first_run", True)

    ## Отмечает, что первый запуск завершён.
    def mark_first_run_done(self):
        data = self.load()
        data["first_run"] = False
        self.save(data)