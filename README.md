 🌤️ Weather Dashboard Pro

A sleek, modern desktop weather intelligence hub built using Python. This application features a highly responsive vertical dashboard design built with **CustomTkinter**, interactive trend analytics via **Matplotlib**, a historical search logger, and a dedicated side-by-side multi-city comparison engine.



✨ Features

* **Real-Time Weather Metrics:** Instantly fetches current temperature, humidity levels, wind speeds, and "feels like" indicators for any global city.
* **Auto-Suggest Search Bar:** Built-in city drop-down selection system that filters popular cities smoothly as you type.
* **Recent Searches Sidebar:** A dedicated left-hand navigation frame that automatically tracks unique history inputs for quick, one-click weather lookups.
* **Side-by-Side Comparison Window:** A custom pop-up layout module allowing users to input and compare two global cities side-by-side instantly.
* **Interactive 5-Day Forecast Chart:** Plots real upcoming daily temperature shifts dynamically on a clean Matplotlib line graph canvas.
* **Fluid Micro-Animations:** Uses mathematical sine-wave loops to float the weather condition profile asset smoothly on the dashboard interface.
* **Smart Health Recommendations:** Delivers context-aware outdoor activity advice based on matching temperature and climate severity thresholds.
* **Live Date & Timepiece:** Features an auto-updating sub-header clock tracking dates and ticking seconds in real-time.



🛠️ Tech Stack & Dependencies

The application relies on a solid stack of modern Python libraries for data processing, network requests, and user interface design:

* **Python 3.12+**: Core programming language runtime.
* **CustomTkinter**: A modern, high-contrast, dark-themed UI widget toolkit wrapped over native Tkinter.
* **Matplotlib**: Advanced plotting engine used to render the 5-day forecast analytics trends.
* **Pillow (PIL)**: High-performance image processing library used to parse and display crisp weather condition icons.
* **Requests**: A clean HTTP network library used to query and fetch live JSON payloads from remote weather APIs.

---

## 📂 Project Architecture

The project workspace is organized into modular, single-purpose components making it incredibly easy to read, manage, and scale:

```text
WEATHER RECOMMENDATION/
│
├── app.py                     # Main execution script and window event loop loader
├── .gitignore                 # Excludes local environments, caches, and system files
├── README.md                  # Complete documentation manual
├── requirements.txt           # Listed dependencies snapshot
│
├── assets/                    # Graphic iconography (sunny.png, cloudy.png, etc.)
│
├── modules/                   # Back-end functional engine core logic
│   ├── weather_api.py         # Network fetch rules querying live weather data APIs
│   └── recommendations.py     # Threshold calculation engine handling activity feedback
│
└── ui/                        # Front-end design layout modules
    ├── search_bar.py          # Auto-suggest drop-down combo box implementation
    ├── dashboard.py           # Stacked, vertically optimized master grid layout
    ├── components.py          # Small modular data tracking container cards
    ├── weather_card.py        # Central condition and main icon container template
    ├── charts.py              # Matplotlib canvas and line rendering configuration
    ├── dialogs.py             # Error and modal popup tracking alerts
    └── compare.py             # Dedicated pop-up screen for side-by-side city metrics
