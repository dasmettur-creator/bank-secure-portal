from customtkinter import *

class BankApp(CTk):
    set_appearance_mode("dark")
    set_default_color_theme("blue")

    def __init__(self):
        super().__init__()

        self.title("Bank of Paradise - Secure Portal")
        self.geometry("1920x1080")

        # ---------------- Frames ----------------
        self.login = CTkFrame(self)
        self.admin_login = CTkFrame(self)
        self.customer_login = CTkFrame(self)
        for frame in (self.login, self.admin_login, self.customer_login):
            frame.grid(row=0, column=0, sticky="nsew")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.login.grid_columnconfigure((0, 1), weight=1)

        CTkButton(
            self.login,
            text="ADMIN LOGIN",
            font=("Times", 24),
            hover_color="green",
            command=self.admin_page,
            height=50,
            width=400,
            corner_radius=50
        ).grid(row=0, column=0, padx=30, pady=200)

        CTkButton(
            self.login,
            text="CUSTOMER LOGIN",
            font=("Times", 24),
            hover_color="green",
            command=self.cust_page,
            height=50,
            width=400,
            corner_radius=50
        ).grid(row=0, column=1, padx=30, pady=200)

        # ---------------- Admin Login ----------------
        self.admin_login.grid_columnconfigure((0, 1), weight=1)

        CTkLabel(
            self.admin_login,
            text="Admin ID :",
            font=("Helvetica", 15)
        ).grid(row=0, column=0, padx=20, pady=20, sticky="e")

        CTkLabel(
            self.admin_login,
            text="Admin Password :",
            font=("Helvetica", 15)
        ).grid(row=1, column=0, padx=20, pady=20, sticky="e")

        admid = CTkEntry(
            self.admin_login,
            placeholder_text="Enter your admin id",
            width=250,
            height=40
        )
        admid.grid(row=0, column=1, padx=20, pady=20)

        admpwd = CTkEntry(
            self.admin_login,
            placeholder_text="Enter your admin password",
            width=250,
            height=40,
            show="*"
        )
        admpwd.grid(row=1, column=1, padx=20, pady=20)

        CTkButton(
            self.admin_login,
            text="Return Home",
            command=self.login_page,
            font=("Times", 20),
            width=150,
            corner_radius=50
        ).grid(row=2, column=0, pady=30)

        CTkButton(
            self.admin_login,
            text="LOGIN",
            command=self.admin_entry,
            font=("Times", 20),
            width=150,
            corner_radius=50
        ).grid(row=2, column=1, pady=30)

        # ---------------- Customer Login ----------------
        self.customer_login.grid_columnconfigure((0, 1), weight=1)

        CTkLabel(
            self.customer_login,
            text="Customer ID :",
            font=("Helvetica", 15)
        ).grid(row=0, column=0, padx=20, pady=20, sticky="e")

        CTkLabel(
            self.customer_login,
            text="Customer Password :",
            font=("Helvetica", 15)
        ).grid(row=1, column=0, padx=20, pady=20, sticky="e")

        custid = CTkEntry(
            self.customer_login,
            placeholder_text="Enter your customer id",
            width=250,
            height=40
        )
        custid.grid(row=0, column=1, padx=20, pady=20)

        custpwd = CTkEntry(
            self.customer_login,
            placeholder_text="Enter your customer password",
            width=250,
            height=40,
            show="*"
        )
        custpwd.grid(row=1, column=1, padx=20, pady=20)

        CTkButton(
            self.customer_login,
            text="Return Home",
            command=self.login_page,
            font=("Times", 20),
            width=150,
            corner_radius=50
        ).grid(row=2, column=0, pady=30)

        CTkButton(
            self.customer_login,
            text="LOGIN",
            command=self.customer_entry,
            font=("Times", 20),
            width=150,
            corner_radius=50
        ).grid(row=2, column=1, pady=30)
        

        self.login_page()

    def customer_entry(self):
        usrtid=custid.get()
        usrpwd=custpwd.get()
        import api_client
        api_client.customer_entry(usrid,usrpwd)

    def admin_entry(self):
        usrtid=admid.get()
        usrpwd=admpwd.get()
        import api_client
        api_client.admin_entry(usrid,usrpwd)
        
    def login_page(self):
        self.login.tkraise()

    def admin_page(self):
        self.admin_login.tkraise()

    def cust_page(self):
        self.customer_login.tkraise()


if __name__ == "__main__":
    app = BankApp()
    app.mainloop()
