# ui/charts.py
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def create_chart_widget(master):
    """Initializes a simple matplotlib canvas frame container."""
    chart_frame = ctk.CTkFrame(master, fg_color="#111827", corner_radius=20)
    
    # Setup Figure
    fig, ax = plt.subplots(figsize=(5, 3.2), dpi=100)
    fig.patch.set_facecolor('#111827')
    ax.set_facecolor('#111827')
    
    # Display an initial text placeholder
    ax.text(0.5, 0.5, "Search city to load trends", color='#6B7280',
            ha='center', va='center', transform=ax.transAxes, fontsize=12)
    ax.tick_params(colors='#9CA3AF', labelsize=9)
    for spine in ax.spines.values():
        spine.set_color('#374151')
        
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.get_tk_widget().pack(fill="both", expand=True, padx=15, pady=15)
    
    return chart_frame, fig, ax, canvas

def update_chart_data(fig, ax, canvas, days, temps):
    """Clears the graph and plots the real upcoming forecast array values."""
    ax.clear()
    ax.grid(True, color='#1F2937', linestyle='--')
    
    ax.plot(days, temps, color='#3B82F6', marker='o', linewidth=2.5, markersize=6)
    ax.fill_between(days, temps, color='#3B82F6', alpha=0.15)
    
    ax.set_title("5-Day Real Temperature Forecast (°C)", color='#E5E7EB', fontsize=11, weight='bold', pad=10)
    ax.tick_params(colors='#9CA3AF')
    for spine in ax.spines.values():
        spine.set_color('#374151')
        
    canvas.draw()