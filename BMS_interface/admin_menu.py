from customtkinter import *

class adminMenu(CTk):
    def __init__(self):
        super().__init__()
        self.title("Admin Menu - Bank of Paradise - Secure Portal")
        self.geometry("1920x1080")
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=3)

        self.menu=CTkFrame(self,fg_color="white")
        self.menu.grid(row=0,column=0,sticky="nsew")
        self.menu.grid_columnconfigure(0,weight=1)
        self.menu.grid_rowconfigure((0,1,2,3,4,5,6,7),weight=1)

        self.content=CTkFrame(self,fg_color="black")
        self.content.grid(row=0,column=1,sticky="nsew")
        self.content.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9),weight=1)
        self.content.grid_columnconfigure((0,1),weight=1)

        CTkLabel(self.menu,text="Admin menu",font=("Jokerman",40),text_color="black").grid(row=0,column=0,sticky="nsew")
        button=["Dashboard", "Customers", "Accounts", "KYC", "Transactions", "Reports", "Settings"]
        for item in button:
            btn = CTkButton(
               self.menu,
               text=item,
               font=("Helvetica",18,"bold"),
               height=50,
               hover_color="green",
               width=150,
               corner_radius=25,
               border_color="black",
               text_color="white",
               fg_color="darkblue",
               border_width=5,
               command=lambda page=item: self.menu_clicked(page)
               ).grid(pady=8)

    def menu_clicked(self,page):
        pass

if __name__=="__main__":
    app=adminMenu()
    app.mainloop()
