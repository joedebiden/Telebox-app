import requests
import customtkinter
from app_dashboard import DashboardApp

class LoginApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("400x300")

        self.email_label = customtkinter.CTkLabel(self, text="Email")
        self.email_label.pack(pady=10)
        self.email_entry = customtkinter.CTkEntry(self)
        self.email_entry.pack(pady=10)

        self.password_label = customtkinter.CTkLabel(self, text="Password")
        self.password_label.pack(pady=10)
        self.password_entry = customtkinter.CTkEntry(self, show="*")
        self.password_entry.pack(pady=10)

        self.login_button = customtkinter.CTkButton(self, text="Login", command=self.login)
        self.login_button.pack(pady=20)

        self.response_label = customtkinter.CTkLabel(self, text="")
        self.response_label.pack()



    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not email or not password:
            self.response_label.configure(text="Please fill in all fields", fg_color="red")
            return
        try:
            response = requests.post(
                "http://93.127.202.5:5002",
                json={"email": email, "password": password}
            )
            if response.status_code == 200:
                self.response_label.configure(text="Login successful!", fg_color="green")
                data = response.json()
                user_mail = data.get("email", "Utilisateur")
                self.open_dashboard(user_mail)

                # Proceed to the main application
            else:
                self.response_label.configure(text="Invalid credentials", fg_color="red")
                
        except Exception as e:
            self.response_label.configure(text=f"Error: {e}", fg_color="red")



    def open_dashboard(self, user_email):
        """Ouvre le dashboard après authentification réussie."""
        self.destroy()  # Ferme la fenêtre de login
        dashboard = DashboardApp(user_email)
        dashboard.mainloop()