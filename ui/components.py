# ui/components.py
import customtkinter as ctk

def create_stat_card(master, title, unit=""):
    """Creates and returns a simple, styled container with a title and a value label."""
    frame = ctk.CTkFrame(master, fg_color="#111827", corner_radius=20)
    
    # Title Label
    title_label = ctk.CTkLabel(frame, text=title, font=("Segoe UI", 16, "bold"), text_color="#9CA3AF")
    title_label.pack(pady=(15, 5))
    
    # Value Label (this is what we update later)
    value_label = ctk.CTkLabel(frame, text="--", font=("Segoe UI", 26, "bold"), text_color="#E5E7EB")
    value_label.pack(pady=(0, 15))
    
    # Return both the main frame to place on the window, and the label to change its text later
    return frame, value_label