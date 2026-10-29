import customtkinter as ctk
from components.history_card import Card
from core.theme import PANEL, TEXT, TEXT_MUTED


class HistoryPanel(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=PANEL, corner_radius=20, border_width=1, border_color="#1B2940")

        self.header = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        self.header.pack(fill="x", padx=20, pady=(20, 10))  

        self.header_icon = ctk.CTkLabel(
            self.header,
            text="⏱",
            font=("Arial", 20),
            text_color="white"
        )
        self.header_icon.pack(side="left", padx=(0, 10))

        self.header_title = ctk.CTkLabel(
            self.header,
            text="История пополнений",
            font=("Arial", 16, "bold"),
            text_color="white"
        )
        self.header_title.pack(side="left")

        self.filter_btn = ctk.CTkButton(
            self.header,
            text="Все операции ▾",
            width=140,
            height=32,
            fg_color="transparent",       # ← прозрачный фон (как ссылка)
            text_color="#888888",         # ← серый текст
            hover_color="#3a3a3a",        # ← подсветка при наведении
            font=("Arial", 12)
        )
        self.filter_btn.pack(side="right")

        self.cards_container = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )
        self.cards_container.pack(fill="both", expand=True, padx=10, pady=(10, 15))

    def add_card(self, date, reason, amount):
        card = Card(self.cards_container, date, reason, amount)
        card.pack(fill="x", pady=(0,10))
