# app.py
import os
import math
import customtkinter as ctk
from PIL import Image
from datetime import datetime

from modules.weather_api import get_weather
from modules.recommendations import get_recommendation
from ui.search_bar import create_search_bar
from ui.dashboard import create_dashboard_layout
from ui.charts import update_chart_data
from ui.dialogs import ErrorDialog
from ui.compare import open_comparison_window

# App window config
app = ctk.CTk()
app.title("Smart Weather Dashboard Pro")
app.geometry("1100x980") # Made taller vertically
app.minsize(1000, 800)
app.configure(fg_color="#0F172A") 

# Global state trackers
animation_step = 0
search_history = []

def update_live_clock():
    # Simple formatting string
    now = datetime.now()
    time_str = now.strftime("%A, %B %d, %Y  —  %I:%M:%S %p")
    clock_label.configure(text=time_str)
    app.after(1000, update_live_clock)

def run_floating_animation():
    global animation_step
    animation_step += 0.05
    
    # Smooth hovering effect calculation
    hover_y = math.sin(animation_step) * 8
    target_rely = 0.5 + (hover_y / 180)
    
    ui["icon_label"].place(relx=0.5, rely=target_rely, anchor="center")
    app.after(20, run_floating_animation)

def update_history_sidebar(city_name):
    # Format name nicely
    name = city_name.title()
    
    # Remove duplicates if it already exists
    if name in search_history:
        search_history.remove(name)
        
    # Put newest search at the top
    search_history.insert(0, name)
    
    # Limit history list to 5 items
    if len(search_history) > 5:
        search_history.pop()
    
    # Clear old sidebar buttons
    for child in sidebar_frame.winfo_children():
        is_btn = isinstance(child, ctk.CTkButton)
        if is_btn and child != compare_nav_btn:
            child.destroy()
            
    # Redraw history buttons
    for city in search_history:
        btn = ctk.CTkButton(
            sidebar_frame, 
            text=city, 
            fg_color="#1F2937", 
            hover_color="#3B82F6",
            height=35, 
            font=("Segoe UI", 13),
            command=lambda c=city: [city_dropdown.set(c), search_weather()]
        )
        btn.pack(fill="x", padx=15, pady=5)

def search_weather():
    city = city_dropdown.get().strip()
    if not city: 
        return

    weather_data = get_weather(city)
    if weather_data is None:
        ErrorDialog(app, title="Not Found", message=f"Could not find city: {city}")
        return

    # Add to history
    update_history_sidebar(city)

    # Breakdown metrics into simple variables (Easier to read)
    current = weather_data["current"]
    main_stats = current["main"]
    wind_stats = current["wind"]
    weather_desc = current["weather"][0]

    temp = round(main_stats["temp"])
    humidity = main_stats["humidity"]
    wind = round(wind_stats["speed"], 1)
    feels_like = round(main_stats["feels_like"])
    condition = weather_desc["main"]

    # Basic weather icon selector
    cond_lower = condition.lower()
    if "clear" in cond_lower or "sun" in cond_lower:
        icon_path = "assets/sunny.png"
    elif "rain" in cond_lower or "drizzle" in cond_lower:
        icon_path = "assets/rainy.png"
    elif "thunder" in cond_lower or "storm" in cond_lower:
        icon_path = "assets/storm.png"
    else:
        icon_path = "assets/cloudy.png"

    recommendation = get_recommendation(temp, condition)

    # Push variables to the dashboard UI labels
    ui["city_label"].configure(text=city.title())
    ui["temp_label"].configure(text=f"{temp}°C")
    ui["condition_label"].configure(text=condition)
    
    # Load condition asset image safely
    if os.path.exists(icon_path):
        img = Image.open(icon_path)
        ctk_img = ctk.CTkImage(light_image=img, dark_image=img, size=(130, 130))
        ui["icon_label"].configure(image=ctk_img)

    # Update humidity with basic safety color thresholds
    ui["humidity_label"].configure(text=f"{humidity}%")
    if humidity > 70:
        ui["humidity_label"].configure(text_color="#F59E0B")
    else:
        ui["humidity_label"].configure(text_color="#E5E7EB")
    
    # Update wind metrics
    ui["wind_label"].configure(text=f"{wind} km/h")
    if wind > 25:
        ui["wind_label"].configure(text_color="#EF4444")
    else:
        ui["wind_label"].configure(text_color="#E5E7EB")

    ui["feels_label"].configure(text=f"{feels_like}°C")
    ui["recommendation_label"].configure(text=recommendation)

    # Refresh the matplotlib canvas chart
    days = weather_data["forecast_days"]
    temps = weather_data["forecast_temps"]
    update_chart_data(ui["fig"], ui["ax"], ui["canvas"], days, temps)

# --- Grid Window Setup ---
app.grid_columnconfigure(0, weight=1) # Sidebar lane
app.grid_columnconfigure(1, weight=5) # Main panel lane

# 1. Navigation Sidebar
sidebar_frame = ctk.CTkFrame(app, width=200, fg_color="#111827", corner_radius=0, border_width=1, border_color="#1F2937")
sidebar_frame.grid(row=0, column=0, rowspan=3, sticky="nsew")
sidebar_frame.pack_propagate(False)

sidebar_title = ctk.CTkLabel(sidebar_frame, text="Navigation", font=("Segoe UI", 16, "bold"), text_color="#3B82F6")
sidebar_title.pack(pady=(20, 10))

compare_nav_btn = ctk.CTkButton(
    sidebar_frame, 
    text="📊 Compare Cities", 
    fg_color="#3B82F6", 
    hover_color="#2563EB",
    font=("Segoe UI", 13, "bold"), 
    height=38, 
    command=lambda: open_comparison_window(app)
)
compare_nav_btn.pack(fill="x", padx=15, pady=(0, 20))

history_title = ctk.CTkLabel(sidebar_frame, text="Recent Searches", font=("Segoe UI", 14, "bold"), text_color="#9CA3AF")
history_title.pack(pady=10)

# 2. Main Windows Dashboard Viewport
main_content = ctk.CTkFrame(app, fg_color="transparent")
main_content.grid(row=0, column=1, sticky="nsew", padx=10)

title_label = ctk.CTkLabel(main_content, text="Smart Weather Dashboard", font=("Segoe UI", 32, "bold"), text_color="#E5E7EB")
title_label.pack(pady=(20, 2))

clock_label = ctk.CTkLabel(main_content, text="Loading System Time...", font=("Segoe UI", 15), text_color="#9CA3AF")
clock_label.pack(pady=(0, 15))

# Search Layout Insertion
search_frame, city_dropdown = create_search_bar(main_content, search_command=search_weather)
search_frame.pack(fill="x", padx=20, pady=10)

# Build cards grid elements panel
ui = create_dashboard_layout(main_content)
ui["frame"].pack(fill="both", expand=True)

# Run background loops
update_live_clock()
run_floating_animation()

app.mainloop()