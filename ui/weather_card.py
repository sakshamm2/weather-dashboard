# ui/weather_card.py
import os
import math
import customtkinter as ctk
from PIL import Image

def create_weather_card(master):
    """Creates the primary weather profile layout card elements."""
    card_frame = ctk.CTkFrame(master, fg_color="#111827", corner_radius=20)
    
    # Hidden sub-container to give the floating icon space to move around
    icon_box = ctk.CTkFrame(card_frame, fg_color="transparent", height=180, width=200)
    icon_box.pack(pady=(10, 0))
    icon_box.pack_propagate(False)
    
    icon_label = ctk.CTkLabel(icon_box, text="")
    icon_label.place(relx=0.5, rely=0.5, anchor="center")
    
    # Text Metrics
    temp_label = ctk.CTkLabel(card_frame, text="--°C", font=("Segoe UI", 52, "bold"), text_color="#E5E7EB")
    temp_label.pack()
    
    city_label = ctk.CTkLabel(card_frame, text="Search City", font=("Segoe UI", 24, "bold"), text_color="#3B82F6")
    city_label.pack(pady=2)
    
    condition_label = ctk.CTkLabel(card_frame, text="Weather Condition", font=("Segoe UI", 18), text_color="#9CA3AF")
    condition_label.pack(pady=(0, 20))
    
    # Set default image placeholder
    if os.path.exists("assets/sunny.png"):
        img = ctk.CTkImage(Image.open("assets/sunny.png"), size=(130, 130))
        icon_label.configure(image=img)
        
    return card_frame, icon_label, temp_label, city_label, condition_label