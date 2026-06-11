# ui/search_bar.py
import customtkinter as ctk

POPULAR_CITIES = [
    "Delhi", "Mumbai", "Bangalore", "Kolkata", "Chennai", "Gurugram", "Noida",
    "London", "New York", "Tokyo", "Paris", "Dubai", "Singapore", "Sydney"
]

def create_search_bar(master, search_command):
    """Creates an entry bar container using simple stacked code lines."""
    search_frame = ctk.CTkFrame(master, fg_color="#111827", corner_radius=20, border_width=1, border_color="#1F2937")
    
    center_container = ctk.CTkFrame(search_frame, fg_color="transparent")
    center_container.pack(expand=True, pady=15)
    
    city_dropdown = ctk.CTkComboBox(
        center_container, 
        width=400, 
        height=45,
        values=POPULAR_CITIES,
        fg_color="#1F2937", 
        border_color="#374151", 
        text_color="#E5E7EB",
        button_color="#3B82F6", 
        button_hover_color="#2563EB",
        font=("Segoe UI", 14)
    )
    city_dropdown.pack(side="left", padx=(20, 15))
    city_dropdown.set("") 
    
    search_button = ctk.CTkButton(
        center_container, 
        text="Search", 
        command=search_command,
        fg_color="#3B82F6", 
        hover_color="#2563EB", 
        width=120, 
        height=45, 
        font=("Segoe UI", 14, "bold")
    )
    search_button.pack(side="left", padx=(10, 20))
    
    return search_frame, city_dropdown