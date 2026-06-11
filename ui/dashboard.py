# ui/dashboard.py
import customtkinter as ctk
from ui.weather_card import create_weather_card
from ui.charts import create_chart_widget
from ui.components import create_stat_card

def create_dashboard_layout(master):
    """Creates a stacked dashboard layout with expanded vertical spacing."""
    dashboard_frame = ctk.CTkFrame(master, fg_color="transparent")
    
    # 2-Column setup
    dashboard_frame.grid_columnconfigure(0, weight=2)
    dashboard_frame.grid_columnconfigure(1, weight=3)
    
    # 1. Left Card: Main City Condition Panel (Expanded vertical padding)
    card_frame, icon_lbl, temp_lbl, city_lbl, cond_lbl = create_weather_card(dashboard_frame)
    card_frame.configure(border_width=1, border_color="#1F2937", height=420) # Made taller
    card_frame.grid(row=0, column=0, padx=(20, 15), pady=25, sticky="nsew")
    
    # 2. Right Card: Forecast Graph Panel
    chart_frame, chart_fig, chart_ax, chart_canvas = create_chart_widget(dashboard_frame)
    chart_frame.configure(border_width=1, border_color="#1F2937", height=420) # Made taller
    chart_frame.grid(row=0, column=1, padx=(15, 20), pady=25, sticky="nsew")
    
    # 3. Bottom Row: Horizontal Stats Row Frame
    stats_row = ctk.CTkFrame(dashboard_frame, fg_color="transparent")
    stats_row.grid(row=1, column=0, columnspan=2, padx=20, pady=15, sticky="ew")
    stats_row.grid_columnconfigure((0, 1, 2), weight=1)
    
    # Humidity Card
    humidity_frame, humidity_val = create_stat_card(stats_row, "Humidity")
    humidity_frame.configure(border_width=1, border_color="#1F2937", height=120)
    humidity_frame.grid(row=0, column=0, padx=(0, 15), sticky="nsew")
    
    # Wind Speed Card
    wind_frame, wind_val = create_stat_card(stats_row, "Wind Speed")
    wind_frame.configure(border_width=1, border_color="#1F2937", height=120)
    wind_frame.grid(row=0, column=1, padx=15, sticky="nsew")
    
    # Feels Like Card
    feels_frame, feels_val = create_stat_card(stats_row, "Feels Like")
    feels_frame.configure(border_width=1, border_color="#1F2937", height=120)
    feels_frame.grid(row=0, column=2, padx=(15, 0), sticky="nsew")
    
    # 4. Bottom Banner: Recommendation Box Panel
    rec_frame = ctk.CTkFrame(
        dashboard_frame, 
        fg_color="#111827", 
        corner_radius=20, 
        border_width=1, 
        border_color="#1F2937"
    )
    rec_frame.grid(row=2, column=0, columnspan=2, padx=20, pady=(20, 30), sticky="ew")
    
    rec_title = ctk.CTkLabel(rec_frame, text="Smart Recommendation", font=("Segoe UI", 18, "bold"), text_color="#3B82F6")
    rec_title.pack(pady=(15, 5))
    
    rec_lbl = ctk.CTkLabel(
        rec_frame, 
        text="Search a city to get weather details.", 
        font=("Segoe UI", 15), 
        text_color="#E5E7EB", 
        wraplength=900
    )
    rec_lbl.pack(pady=(5, 20))
    
    # Map all ui variables out for app.py reference reads
    ui_elements = {
        "frame": dashboard_frame,
        "icon_label": icon_lbl, 
        "temp_label": temp_lbl, 
        "city_label": city_lbl, 
        "condition_label": cond_lbl,
        "fig": chart_fig, 
        "ax": chart_ax, 
        "canvas": chart_canvas,
        "humidity_label": humidity_val, 
        "wind_label": wind_val, 
        "feels_label": feels_val,
        "recommendation_label": rec_lbl
    }
    return ui_elements