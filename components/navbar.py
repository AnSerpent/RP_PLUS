import customtkinter as ctk
from core.theme import (
    PANEL, CARD, ACCENT, ACCENT_HOVER,
    TEXT, TEXT_MUTED
)


class Navbar(ctk.CTkFrame):
    def __init__(self, master, on_tab_change):
        super().__init__(master, fg_color="transparent",)

        self.on_tab_change = on_tab_change

        # Серый контейнер с элементами (компактный, по содержимому)
        self.container = ctk.CTkFrame(self, fg_color=PANEL, corner_radius=20, border_width=1, border_color="#1B2940")
        self.container.pack(side="left", ipady=10)

        # Логотип
        self.icon_label = ctk.CTkLabel(
            self.container,
            text="⌛",
            font=("Arial", 20)
        )
        self.icon_label.pack(side="left", padx=20)

        # Название
        self.name_label = ctk.CTkLabel(
            self.container,
            text="RP+",
            font=("Arial", 20),
            text_color=TEXT
        )
        self.name_label.pack(side="left")

        # Фрейм с кнопками-вкладками
        self.buttons_frame = ctk.CTkFrame(self.container, fg_color="transparent")
        self.buttons_frame.pack(side="left", padx=(0, 15))

        # Кнопки-вкладки
        self.deposit_button = ctk.CTkButton(
            self.buttons_frame,
            text="Пополнение",
            font=("Arial", 20),
            command=lambda: self.on_click("deposit"),
            text_color=TEXT,
            height=30,
            corner_radius=20,
            hover_color=ACCENT_HOVER
        )
        self.timers_button = ctk.CTkButton(
            self.buttons_frame,
            text="Таймеры",
            font=("Arial", 20),
            command=lambda: self.on_click("timers"),
            text_color=TEXT,
            height=30,
            corner_radius=20,
            hover_color=ACCENT_HOVER
        )
        self.extended_button = ctk.CTkButton(
            self.buttons_frame,
            text="Расширенное",
            font=("Arial", 20),
            command=lambda: self.on_click("extended"),
            text_color=TEXT,
            height=30,
            corner_radius=20,
            hover_color=ACCENT_HOVER
        )
        self.settings_button = ctk.CTkButton(
            self.buttons_frame,
            text="Настройки",
            font=("Arial", 20),
            command=lambda: self.on_click("settings"),
            text_color=TEXT,
            height=30,
            corner_radius=20,
            hover_color=ACCENT_HOVER
        )

        self.deposit_button.pack(side="left", padx=10)
        self.timers_button.pack(side="left", padx=10)
        self.extended_button.pack(side="left", padx=10)
        self.settings_button.pack(side="left", padx=10)

        self.tabs = {
            "deposit": self.deposit_button,
            "timers": self.timers_button,
            "extended": self.extended_button,
            "settings": self.settings_button,
        }

        self.set_active("deposit")

    def set_active(self, tab_name):
        for name, btn in self.tabs.items():
            btn.configure(
                fg_color="transparent",
                text_color=TEXT_MUTED,
                hover_color=ACCENT_HOVER
            )
        active_btn = self.tabs[tab_name]
        active_btn.configure(
            fg_color=ACCENT,
            text_color=TEXT,
        )

    def on_click(self, tab_name):
        self.set_active(tab_name)
        self.on_tab_change(tab_name)