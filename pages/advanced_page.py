import customtkinter as ctk

class AdvancedPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")

        self.placeholder_label = ctk.CTkLabel(
            self,
            text="Эта страница еще не готова, следите за обновлениями!",
            font=("Arial", 20),
            text_color="white"
        )
        self.placeholder_label.pack(anchor="center", expand=True)