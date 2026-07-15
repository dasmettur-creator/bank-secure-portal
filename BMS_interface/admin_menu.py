from customtkinter import *
set_appearance_mode("dark")
set_default_color_theme("blue")

class adminMenu(CTk):
    def __init__(self):
        super().__init__()
        self.menu=CTkFrame(self)
        self.title("Admin Menu - Bank of Paradise - Secure Portal")
        self.geometry("1920x1080")
        self.menu.grid(row=0,column=0,sticky="nsew")
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)
        self.menu.grid_columnconfigure((0,1),weight=1)

if __name__=="__main__":
    app=adminMenu()
    app.mainloop()
