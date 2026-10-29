import customtkinter as ctk
from windows.error_window import ErrorWindow
from core.theme import (
    PANEL, CARD, ACCENT, ACCENT_HOVER,
    TEXT, TEXT_MUTED
)


class DepositForm(ctk.CTkFrame):
    def __init__(self, master, on_submit):
        super().__init__(master, fg_color=PANEL, corner_radius=20, border_width=1, border_color="#1B2940")
        self.on_submit = on_submit

        self.header = ctk.CTkFrame(self, fg_color="transparent")
        self.header.pack(fill="x", padx=20, pady=(20, 10))

        self.icon_frame = ctk.CTkFrame(
            self.header,
            width=50,
            height=50,
            corner_radius=25,
            fg_color="#1f6aa5"
        )

        self.icon_frame.pack_propagate(False)
        self.icon_frame.pack(side="left", padx=(0, 15))

        self.icon_label = ctk.CTkLabel(
            self.icon_frame,
            text="💳",
            font=("Arial", 24)
        )
        self.icon_label.pack(expand=True)

        self.title_label = ctk.CTkLabel(
            self.header,
            text="Пополнение счёта",
            font=("Arial", 18, "bold"),
            text_color=TEXT
        )

        self.title_label.pack(side="left")

        self.entry_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.entry_frame.pack(fill="both", expand=True, padx=30, pady=(10, 20))

        self.reason_label = ctk.CTkLabel(
            self.entry_frame,
            text="Причина пополнения",
            font=("Arial", 14, "bold"),
            text_color=TEXT
        )

        self.reason_label.pack(anchor="w", pady=(0, 5))

        self.reason_entry = ctk.CTkEntry(
            self.entry_frame,
            placeholder_text="Введите причину",
            placeholder_text_color=TEXT_MUTED,
            height=45,
            corner_radius=10,
            fg_color=CARD,
            border_width=0,
            font=("Arial", 14)
        )

        self.reason_entry.pack(fill="x", pady=(0, 15))

        self.amount_label = ctk.CTkLabel(
            self.entry_frame,
            text="Сумма пополнения",
            font=("Arial", 14, "bold"),
            text_color=TEXT

        )
        self.amount_label.pack(anchor="w", pady=(0, 5))

        self.amount_entry = ctk.CTkEntry(
            self.entry_frame,
            placeholder_text="Введите сумму",
            placeholder_text_color=TEXT_MUTED,
            height=45,
            corner_radius=10,
            fg_color=CARD,
            border_width=0,
            font=("Arial", 14)
        )

        self.amount_entry.pack(fill="x", pady=(0, 20))

        self.refill_button = ctk.CTkButton(
            self.entry_frame,
            text="Пополнить  →",                # ← добавил стрелку
            height=50,
            corner_radius=12,
            fg_color=ACCENT,                 # ← синий фон
            text_color=TEXT,
            hover_color=ACCENT_HOVER,              # ← темнее при наведении
            font=("Arial", 16, "bold"),
            command=self.submit                  
        )
        self.refill_button.pack(fill="x")

    def submit(self):
        reason = self.reason_entry.get().strip()
        amount = self.amount_entry.get().strip()

        if not reason:
            ErrorWindow(self.winfo_toplevel(), "Введите причину!")
            return
        
        if not amount:                          
            ErrorWindow(self.winfo_toplevel(), "Введите сумму!")
            return
        
        if not amount.isdigit():
            ErrorWindow(self.winfo_toplevel(), "Сумма должна быть числом!")        
            return
        
        self.on_submit(reason, amount)
                
        self.reason_entry.delete(0, "end")
        self.amount_entry.delete(0, "end")