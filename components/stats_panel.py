import customtkinter as ctk
from components.history_card import Card
from core.theme import (
    PANEL, CARD, ACCENT, ACCENT_HOVER,
    TEXT, TEXT_MUTED
)


class StatsPanel(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")

        self.balance_block = ctk.CTkFrame(self, fg_color=PANEL, corner_radius=20, border_width=1, border_color="#1B2940")
        self.balance_block.pack(fill="x", pady=(0, 15))

        self.recent_block = ctk.CTkFrame(self, fg_color=PANEL, corner_radius=20, border_width=1, border_color="#1B2940")
        self.recent_block.pack(
            fill="both",
            expand=True
        )

        self.recent_block_header = ctk.CTkFrame(self.recent_block, fg_color="transparent")
        self.recent_block_header.pack(fill="x", padx=20, pady=(15, 10))

        self.recent_block_container = ctk.CTkScrollableFrame(
            self.recent_block,
            fg_color="transparent",
            corner_radius=12,
            scrollbar_button_color="#555555",
            scrollbar_button_hover_color="#666666"
        )
        self.recent_block_container.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(0, 10)
        )
        self.icon_label = ctk.CTkLabel(
            self.balance_block,
            text="💳",
            font=("Arial", 20),
            text_color="white"
        )
        
        self.current_balance = ctk.CTkLabel(
            self.balance_block,
            text="Текущий баланс",
            font=("Arial", 20),
            text_color=TEXT
        )

        self.current_balance_digit = ctk.CTkLabel(
            self.balance_block,
            text="0",                                              ##ВРЕМЕННАЯ ЗАГЛУШКА
            font=("Arial", 20),
            text_color=TEXT
        )

        self.recent_block_icon = ctk.CTkLabel(
            self.recent_block_header,
            text="📋",
            font=("Arial", 20),
            text_color="white"
        )

        self.recent_block_label = ctk.CTkLabel(
            self.recent_block_header,
            text="Последние действия",
            font=("Arial", 20),
            text_color=TEXT
        )

        self.recent_block_icon.pack(side="left", padx=(0, 10))
        self.recent_block_label.pack(side="left")

        self.balance_block.grid_columnconfigure(0, weight=0)
        self.balance_block.grid_columnconfigure(1, weight=1)
        self.balance_block.grid_columnconfigure(2, weight=0)

        self.icon_label.grid(row=0, column=0, padx=(15,10), pady=15)
        self.current_balance.grid(row=0, column=1, sticky="w")
        self.current_balance_digit.grid(row=0, column=2, padx=(10,15))

    def add_recent(self, date, reason, amount):
        card = Card(self.recent_block_container, date, reason, amount)
        card.pack(fill="x", pady=(0, 10))

    def update_balance(self, total):
        self.current_balance_digit.configure(text=str(total))