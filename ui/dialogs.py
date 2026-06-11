# ui/dialogs.py
import customtkinter as ctk

class ErrorDialog(ctk.CTkToplevel):
    def __init__(self, master, title="Error", message="An error occurred", **kwargs):
        super().__init__(master, **kwargs)
        self.title(title)
        self.geometry("350x180")
        self.resizable(False, False)
        self.transient(master)  # Keeps window pinned on top of main app
        
        self.configure(fg_color="#0B1120")
        
        label = ctk.CTkLabel(
            self, text=message, font=("Segoe UI", 14), 
            text_color="#E5E7EB", wraplength=300
        )
        label.pack(expand=True, fill="both", padx=20, pady=20)
        
        btn = ctk.CTkButton(
            self, text="Dismiss", width=100, fg_color="#3B82F6",
            command=self.destroy
        )
        btn.pack(pady=(0, 20))