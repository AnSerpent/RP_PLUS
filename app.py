import customtkinter as ctk

from core.resources import resource_path
from components.navbar import Navbar
from pages.deposit_page import DepositPage
from pages.advanced_page import AdvancedPage
from pages.settings_page import SettingsPage
from pages.timers_page import TimersPage
from core.theme import BG, TEXT_MUTED
from core.settings import Settings
from windows.welcome_window import WelcomeWindow


class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=BG)

        try:
            # Windows
            self.iconbitmap(resource_path("assets/icon_wbg.ico"))
        except Exception:
            try:
                # macOS / Linux
                from PIL import ImageTk
                icon_img = ImageTk.PhotoImage(Image.open(resource_path("assets/icon.png")))
                self.iconphoto(True, icon_img)
            except Exception:
                pass

        self.version = "beta v2.0.0"

        self.settings = Settings()

        self.title("RP+")
        self.geometry("1400x800")
        self.minsize(1200, 700)

        self.navbar = Navbar(
            self,
            on_tab_change=self.handle_tab_change
        )
        self.navbar.pack(
            anchor="n",
            padx=10,
            pady=(15, 0),
            ipady=10
        )

        # Нижняя полоса для версии
        self.footer = ctk.CTkFrame(
            self,
            fg_color="transparent",
            height=12,
            corner_radius=0
        )
        self.footer.pack(
            side="bottom",
            fill="x",
            padx=12,
            pady=(0, 5)
        )
        self.footer.pack_propagate(False)

        self.version_label = ctk.CTkLabel(
            self.footer,
            text=self.version,
            font=("Arial", 11),
            fg_color="transparent",
            text_color=TEXT_MUTED
        )
        self.version_label.pack(
            side="right",
            anchor="center"
        )

        # Контейнер страниц.
        self.content_frame = ctk.CTkFrame(
            self,
            fg_color="transparent",
            corner_radius=0
        )
        self.content_frame.pack(
            fill="both",
            expand=True
        )

        # Страницы
        self.deposit_page = DepositPage(self.content_frame)
        self.timers_page = TimersPage(self.content_frame)
        self.advanced_page = AdvancedPage(self.content_frame)
        self.settings_page = SettingsPage(self.content_frame)

        self.pages = {
            "deposit": self.deposit_page,
            "timers": self.timers_page,
            "extended": self.advanced_page,
            "settings": self.settings_page,
        }

        self.show_page("deposit")

        if self.settings.is_first_run():
            self.after(100, self.show_welcome)

    def handle_tab_change(self, tab_name):
        self.show_page(tab_name)

    def show_page(self, name):
        for page in self.pages.values():
            page.pack_forget()

        self.pages[name].pack(
            fill="both",
            expand=True
        )

    def show_welcome(self):
        WelcomeWindow(self)
        self.settings.mark_first_run_done()