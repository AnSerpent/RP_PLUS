import customtkinter as ctk


class ErrorWindow(ctk.CTkToplevel):
    def __init__(self, master, message):
        super().__init__(master)

        self.title("ошибка")
        self.geometry("350x180")
        self.configure(fg_color="#1e1e1e")
        self.attributes("-topmost", True)

        self.label = ctk.CTkLabel(
            self,
            text=message,                    # ← ВОТ ЗДЕСЬ используем message
            font=("Arial", 14),
            text_color="#ff6666",            # красный, для ошибки
            wraplength=300                   # перенос длинных строк
        )
        self.label.pack(pady=(30, 20))

        self.button = ctk.CTkButton(
            self,
            text="OK", 
            width=100,
            height=40,
            command=self.destroy
        )
        self.button.pack(anchor="center", pady=(0, 30))

        self.after(50, self.center_on_screen)

    def center_on_screen(self):    
        # 1. Отрисовываем окно, чтобы получить реальные размеры
        self.update_idletasks()      
        
        # 2. Узнаём размеры окна
        width = self.winfo_width()                  
        height = self.winfo_height()                 
        
        # 3. Узнаём размеры экрана
        screen_w = self.winfo_screenwidth()               
        screen_h = self.winfo_screenheight()                 
        
        # 4. Считаем координаты левого верхнего угла окна
        x = (screen_w - width) // 2
        y = (screen_h - height) // 2                  
        
        # 5. Устанавливаем окну новые координаты
        self.geometry(f"{width}x{height}+{x}+{y}")           
