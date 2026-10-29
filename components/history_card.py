import customtkinter as ctk
from core.theme import (
    PANEL, CARD, ACCENT, ACCENT_HOVER,
    TEXT, TEXT_MUTED
)


class Card(ctk.CTkFrame):
    def __init__(self, master, date, reason, amount):
        super().__init__(master, fg_color=CARD, corner_radius = 20)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)

        self.date_label = ctk.CTkLabel(
            self,
            text=date,
            font=("Arial", 12),           
            text_color=TEXT
        )

        self.reason_label = ctk.CTkLabel(
            self,
            text=reason,
            font=("Arial", 15, "bold"),   
            text_color=TEXT
        )

        self.amount_label = ctk.CTkLabel(
            self,
            text=amount,
            font=("Arial", 15),           
            text_color=TEXT
        )
        
        self.circle_icon = ctk.CTkLabel(
            self, 
            text="◉",
            text_color="#00cc88",
            font=("Arial", 20)
        )
        self.done_label = ctk.CTkLabel(
            self, 
            text="Завершено", 
            fg_color="#1a4d3a", 
            text_color="#00cc88", 
            corner_radius=10, 
            padx=10, 
            pady=2
        )
        self.circle_icon.grid(
            row = 0, column = 0,
            rowspan = 3,
            padx=(15, 10),          # ← отступы слева 15, справа 10
            pady=15    
        )
        
        self.date_label.grid(
            row = 0, column = 1,
            sticky="w",             # ← прижать к левому краю
            pady=(15, 2) 
        )

        self.reason_label.grid(
            row = 1, column = 1,
            sticky="w",
            pady=2
        )

        self.amount_label.grid(
            row = 2, column = 1,
            sticky="w",
            pady=(2, 15) 
        )

        self.done_label.grid(
            row = 1, column = 2,
            padx=(10, 15),          # ← отступ слева 10, справа 15
            sticky="e"              # ← прижать к правому краю
        )
        