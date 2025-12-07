# Sovereign Interface - Command Center 

A dynamic, glassmorphism-themed desktop dashboard that transforms your wallpaper into a fully functional command center with real-time system monitoring, developer tools, and integrated web utilities.

![Dashboard Preview](https://images.unsplash.com/photo-1518066000714-58c45f1a2c0a?q=80&w=2560&auto=format&fit=crop)

## 🚀 Features

### Core Dashboard

- **Real-Time Clock & Date** - Always-visible time display
- **Live Weather** - Current conditions and 7-day forecast (Open-Meteo API)
- **System Monitor** - Live CPU, RAM, Disk, and GPU usage stats
- **Calendar Integration** - Google Calendar agenda view
- **RSS Feed** - Live tech news ticker
- **Geospatial Panels** - Radar, Wind, Flight Tracking, Marine Traffic, Cyber Threats
- **Visual Ambience** - YouTube-powered ambient video player with 70+ curated vibes
- **Command Deck** - Organized bookmark launcher with 20+ categories

### Developer Workbench (Dev-Dock)

Slide-out panel accessible via **Alt+D** or the trigger button:

- **Regex101** - Real-time regular expression testing
- **JSONLint** - JSON validation and formatting
- **CyberChef** - Data encoding/decoding Swiss Army knife
- **Carbon** - Beautiful code screenshot generator

### System Integration

- **Local Backend** - Python Flask server for advanced features
- **App Launching** - Launch local applications via backend API
- **Protocol Handlers** - Steam, Spotify, Discord, VS Code integration
- **Zen Mode** - Alt+Z to hide all panels for distraction-free focus

## 📋 Prerequisites

- **Windows 10/11**
- **Python 3.10+**
- **Modern Web Browser** (Chrome, Edge, Firefox)

## 🛠️ Installation

### 1. Install Python Dependencies

```powershell
pip install -r requirements.txt
```

### 2. Configure Your System (Important!)

**Security Warning:** This dashboard runs a local Python server. By default, it is configured to be safe, but you should review `server.py` before running it.

1. **Edit `server.py`**:
   - Update `APP_REGISTRY` to point to your actual application paths (e.g., Notepad++, VS Code).
   - **Note:** The potentially dangerous `cmd` and `powershell` launchers have been disabled by default for security.

2. **Edit `wallpaper_1.html`**:
   - **Weather**: Update the latitude/longitude in the `fetchWeather()` function (Line ~1069) to your location.
   - **Bookmarks**: Customize the `bookmarksData` object (Line ~1157) with your own links.
   - **Local Links**: Update the 'local' category in `bookmarksData` for your city's news and services.

### 3. Launch the Dashboard

**Method A: One-Click Launcher**
Double-click `run_dashboard.bat`.

**Method B: Manual Launch**

```powershell
# Terminal 1: Start the backend
python server.py

# Terminal 2: Open the dashboard
start wallpaper_1.html
```

## 🎮 Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| **Alt+D** | Toggle Developer Workbench |
| **Alt+Z** | Toggle Zen Mode |
| **Alt+R** | Switch to Radar view |
| **Alt+W** | Switch to Wind Map |
| **Alt+M** | Switch to Marine Traffic |
| **Alt+T** | Switch to Traffic Map |
| **Alt+1** | Open Essentials folder |
| **Alt+2** | Open Finance folder |
| **Alt+3** | Open School folder |
| **Alt+4** | Open Tech folder |

## 🔧 Backend API requests

The Python backend (`server.py`) runs on `http://localhost:5000`.

### Endpoints

- **GET /health** - Health check
- **GET /stats** - System statistics (CPU, RAM, Disk, GPU)
- **POST /launch** - Launch local applications
- **GET /apps** - List registered applications

## 🔒 Security & Privacy

- **Local Execution**: The backend runs strictly on `localhost` (127.0.0.1). It is not accessible from the internet.
- **Sandboxed Frames**: All external content (maps, tools) is loaded in sandboxed iframes.
- **Data Privacy**: No personal data is sent to external servers (except for standard API requests to Open-Meteo, RSS feeds, etc.).

**Recommendation**: Do not expose port 5000 to the public internet.

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.

## 🙏 Credits

- **Weather Data**: [Open-Meteo](https://open-meteo.com/)
- **Icons**: [Font Awesome](https://fontawesome.com/)
- **Fonts**: [Google Fonts](https://fonts.google.com/)
