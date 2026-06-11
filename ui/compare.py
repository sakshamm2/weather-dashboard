# ui/compare.py
import customtkinter as ctk
from modules.weather_api import get_weather

def open_comparison_window(master_window):
    """Launches a secondary top-level window to compare 2 cities side-by-side."""
    comp_win = ctk.CTkToplevel(master_window)
    comp_win.title("Compare Cities")
    comp_win.geometry("700x500")
    comp_win.configure(fg_color="#0F172A")
    comp_win.transient(master_window) # Float on top
    
    # Input Row
    input_frame = ctk.CTkFrame(comp_win, fg_color="transparent")
    input_frame.pack(fill="x", padx=20, pady=20)
    
    entry1 = ctk.CTkEntry(input_frame, placeholder_text="City 1...", width=180, height=35, fg_color="#1F2937")
    entry1.pack(side="left", padx=10)
    
    entry2 = ctk.CTkEntry(input_frame, placeholder_text="City 2...", width=180, height=35, fg_color="#1F2937")
    entry2.pack(side="left", padx=10)
    
    # Display Grid Frames
    result_frame = ctk.CTkFrame(comp_win, fg_color="transparent")
    result_frame.pack(fill="both", expand=True, padx=20, pady=10)
    result_frame.grid_columnconfigure((0, 1), weight=1)
    
    def fetch_and_compare():
        city1, city2 = entry1.get().strip(), entry2.get().strip()
        if not city1 or not city2: return
        
        data1, data2 = get_weather(city1), get_weather(city2)
        if not data1 or not data2: return
        
        # Clear old widgets
        for widget in result_frame.winfo_children(): widget.destroy()
        
        # Render Columns
        for i, data in enumerate([data1["current"], data2["current"]]):
            col_frame = ctk.CTkFrame(result_frame, fg_color="#111827", corner_radius=15, border_width=1, border_color="#1F2937")
            col_frame.grid(row=0, column=i, padx=15, pady=10, sticky="nsew")
            
            ctk.CTkLabel(col_frame, text=data["name"], font=("Segoe UI", 24, "bold"), text_color="#3B82F6").pack(pady=15)
            ctk.CTkLabel(col_frame, text=f"{round(data['main']['temp'])}°C", font=("Segoe UI", 40, "bold")).pack()
            ctk.CTkLabel(col_frame, text=data['weather'][0]['main'], font=("Segoe UI", 16), text_color="#9CA3AF").pack(pady=5)
            
            # Sub-metrics lists
            metrics_txt = f"Humidity: {data['main']['humidity']}%\nWind: {data['wind']['speed']} km/h\nFeels Like: {round(data['main']['feels_like'])}°C"
            ctk.CTkLabel(col_frame, text=metrics_txt, font=("Segoe UI", 14), justify="left").pack(pady=15)

    comp_btn = ctk.CTkButton(input_frame, text="Compare", command=fetch_and_compare, fg_color="#3B82F6", font=("Segoe UI", 14, "bold"))
    comp_btn.pack(side="left", padx=15)