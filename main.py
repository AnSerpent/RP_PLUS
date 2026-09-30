import customtkinter as ctk
from PIL import Image
import json
import sys, os  
from datetime import datetime

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# --- Настройки темы ---
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

# Файл, куда будем сохранять историю
HISTORY_FILE = "history.json"
APP_VERSION = "v1.0.0 · 29.09.2026"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Настройки главного окна
        self.title("RP+")
        self.geometry("1000x650")
        self.minsize(800, 500)
        self.configure(fg_color="#1e1e1e")

        # Главная сетка на 2 колонки
        self.grid_columnconfigure(0, weight=1, minsize=400)
        self.grid_columnconfigure(1, weight=1, minsize=400)
        self.grid_rowconfigure(0, weight=1)

        # ================= ЛЕВАЯ КОЛОНКА (форма) =================
        self.left_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.left_frame.grid(row=0, column=0, padx=40, pady=40, sticky="nsew")

                 # Иконка (загружаем из файла)
        try:
            img = Image.open(resource_path("icon.png"))
            orig_w, orig_h = img.size

            # Хотим высоту 100px, ширину считаем по пропорции
            target_height = 100
            target_width = int(orig_w * (target_height / orig_h))

            icon_image = ctk.CTkImage(
                light_image=img,
                dark_image=img,
                size=(target_width, target_height)
            )
            self.logo_label = ctk.CTkLabel(
                self.left_frame,
                image=icon_image,
                text=""
            )
        except FileNotFoundError:
            # Если картинки нет — показываем эмодзи
            self.logo_label = ctk.CTkLabel(
                self.left_frame,
                text="⌛",
                font=("Arial", 80),
                text_color="white"
            )
        
        self.logo_label.pack(anchor="w", pady=(0, 40))

        # Поле "Причина"
        self.reason_entry = ctk.CTkEntry(
            self.left_frame,
            placeholder_text="Причина пополнения",
            height=55,
            corner_radius=15,
            fg_color="#333333",
            border_width=0,
            font=("Arial", 16)
        )
        self.reason_entry.pack(fill="x", pady=(0, 15))

        # 👇 Поле "Сумма" 
        self.amount_entry = ctk.CTkEntry(
            self.left_frame,
            placeholder_text="Сумма пополнения",
            height=55,
            corner_radius=15,
            fg_color="#333333",
            border_width=0,
            font=("Arial", 16),
            
        )
        self.amount_entry.pack(fill="x", pady=(0, 15))

        # Кнопка
        self.submit_btn = ctk.CTkButton(
            self.left_frame,
            text="Пополнить",
            height=55,
            corner_radius=15,
            fg_color="#e0e0e0",
            text_color="black",
            hover_color="#ffffff",
            font=("Arial", 18, "bold"),
            command=self.add_record
        )
        self.submit_btn.pack(fill="x")

        # ================= ПРАВАЯ КОЛОНКА (история) =================
        self.right_frame = ctk.CTkScrollableFrame(
            self,
            fg_color="#2b2b2b",
            corner_radius=20
        )
        self.right_frame.grid(row=0, column=1, padx=(0, 40), pady=40, sticky="nsew")

        # 👇 Принудительное обновление интерфейса после старта
        self.after(50, self.update_idletasks)
        self.after(100, self.update)

        # 👇 Загружаем историю из файла при запуске
        self.load_history()

        self.version_label = ctk.CTkLabel(
            self,
            text=APP_VERSION,
            font=("Arial", 12),
            text_color="#666666"
        )
        self.version_label.place(relx=0.02, rely=0.97, anchor="sw")

    def show_error(self, message):
        error_window = ctk.CTkToplevel(self)
        error_window.title("Ошибка")
        error_window.geometry("300x150")
        error_window.configure(fg_color="#1e1e1e")
        error_window.attributes("-topmost", True)   # поверх всех окон

        label = ctk.CTkLabel(
            error_window,
            text=message,
            font=("Arial", 14),
            text_color="#ff6666"
        )
        label.pack(pady=30)

        ok_btn = ctk.CTkButton(
            error_window,
            text="OK",
            width=100,
            command=error_window.destroy
        )
        ok_btn.pack(pady=10)


    def load_history(self):
        """Загружает записи из файла и отображает их."""
        if not os.path.exists(HISTORY_FILE):
            return
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                records = json.load(f)
            for record in records:
                self.render_card(record["date"], record["reason"], record["amount"])
        except (json.JSONDecodeError, KeyError):
            pass  # Если файл поврежден — просто игнорируем

    def save_history(self, date, reason, amount):
        """Добавляет новую запись в файл."""
        records = []
        if os.path.exists(HISTORY_FILE):
            try:
                with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                    records = json.load(f)
            except json.JSONDecodeError:
                records = []
        records.append({"date": date, "reason": reason, "amount": amount})
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(records, f, ensure_ascii=False, indent=2)

    def render_card(self, date, reason, amount):
        """Отрисовывает одну карточку в правой панели."""
        card = ctk.CTkFrame(self.right_frame, fg_color="#3a3a3a", corner_radius=12)
        card.pack(fill="x", pady=8, padx=8)

        ctk.CTkLabel(
            card, text=date,
            font=("Arial", 13), text_color="#888888", anchor="w"
        ).pack(fill="x", padx=15, pady=(10, 2))

        ctk.CTkLabel(
            card, text=f"Причина: {reason}",
            font=("Arial", 15, "bold"), text_color="white", anchor="w"
        ).pack(fill="x", padx=15, pady=2)

        ctk.CTkLabel(
            card, text=f"Сумма: {amount}.",
            font=("Arial", 15), text_color="#cccccc", anchor="w"
        ).pack(fill="x", padx=15, pady=(2, 10))

    def add_record(self):
        reason = self.reason_entry.get().strip()
        amount = self.amount_entry.get().strip()

        # Проверка: сумма должна быть числом
        if not amount.isdigit():
            self.show_error("Сумма должна быть числом!")
            return

        # Заглушки, если поля пустые
        reason = reason or "Без причины."
        amount = amount or "0"

        # Настоящая дата
        now = datetime.now().strftime("%d/%m/%Y")

        # Отрисовываем карточку и сохраняем
        self.render_card(now, reason, amount)
        self.save_history(now, reason, amount)

        # Очищаем поля
        self.reason_entry.delete(0, 'end')
        self.amount_entry.delete(0, 'end')


if __name__ == "__main__":
    app = App()
    app.mainloop()