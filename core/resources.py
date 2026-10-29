import sys
import os


def resource_path(relative_path):
    """
    Возвращает правильный путь к файлу.
    Работает и при разработке (python main.py), и внутри .exe (PyInstaller).

    Как работает:
    - В обычном режиме ищет файл в папке проекта.
    - В .exe PyInstaller распаковывает файлы во временную папку,
      путь к которой хранится в sys._MEIPASS.
    """
    try:
        # Случай 1: запуск из .exe — PyInstaller
        base_path = sys._MEIPASS
    except AttributeError:
        # Случай 2: обычный запуск — папка с проектом
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path) 