import customtkinter as ctk
from core.theme import (
    PANEL, TEXT, TEXT_MUTED, ACCENT, ACCENT_HOVER
)


class WelcomeWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master, fg_color=PANEL)

        self.title("Добро пожаловать!")
        self.geometry("500x400")
        self.attributes("-topmost", True)

        # Заголовок
        self.header_label = ctk.CTkLabel(
            self,
            text="Добро пожаловать в RP+",
            text_color=TEXT,
            font=("Arial", 22, "bold")
        )
        self.header_label.pack(pady=(40, 20))

        # Описание
        self.description_label = ctk.CTkLabel(
            self,
            text=(
                "Приложение находится на стадии бета-тестирования\n\n"
                "Данная версия не отображает финальное качество продукта\n"
                "Приятного использования!"
            ),
            text_color=TEXT_MUTED,
            font=("Arial", 14),
            wraplength=400,
            justify="center"
        )
        self.description_label.pack(pady=(0, 30))

        # Кнопка
        self.button = ctk.CTkButton(
            self,
            text="Начать",
            text_color=TEXT,
            font=("Arial", 16, "bold"),
            width=200,
            height=45,
            corner_radius=10,
            fg_color=ACCENT,
            hover_color=ACCENT_HOVER,
            command=self.destroy
        )
        self.button.pack(pady=(0, 20))

        self.after(100, self.center_on_screen)

    def center_on_screen(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()
        x = (screen_w - width) // 2
        y = (screen_h - height) // 2
        self.geometry(f"{width}x{height}+{x}+{y}")