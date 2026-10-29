import customtkinter as ctk
from components.deposit_form import DepositForm
from components.history_panel import HistoryPanel
from components.stats_panel import StatsPanel
from core.storage import Storage
from datetime import datetime

class DepositPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")

        self.storage = Storage()

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.history = HistoryPanel(self)
        self.history.grid(row=0, column=1, padx=10, pady=15, sticky="nsew")

        self.stats = StatsPanel(self)
        self.stats.grid(row=0, column=2, padx=(10,20), pady=15, sticky="nsew")

        self.form = DepositForm(self, on_submit=self.handle_submit)
        self.form.grid(row=0, column=0, padx=(20, 10), pady=15, sticky="nsew")

        for record in self.storage.load():
            self.history.add_card(record["date"], record["reason"], record["amount"])
            self.stats.add_recent(record["date"], record["reason"], record["amount"])

        self.stats.update_balance(self.storage.total_balance())
        
    def handle_submit(self, reason, amount):
        date = datetime.now().strftime("%d.%m.%Y")
        self.storage.add(date, reason, amount)
        self.history.add_card(date, reason, amount)
        self.stats.add_recent(date, reason, amount)
        new_total = self.storage.total_balance()
        self.stats.update_balance(new_total)