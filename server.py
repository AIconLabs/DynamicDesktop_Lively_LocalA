"""
Sovereign Interface - Local Backend Server
Bridges the HTML dashboard with the local OS for advanced functionality.
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import subprocess
import psutil
import platform
import os

app = Flask(__name__)
CORS(app)  # Allow requests from local HTML file

# Application Registry - Maps friendly names to executable paths
APP_REGISTRY = {
    'notepad': r'C:\Program Files\Notepad++\notepad++.exe',
    'notepad_basic': r'C:\Windows\System32\notepad.exe',
    # 'vscode': r'%LOCALAPPDATA%\Programs\Microsoft VS Code\Code.exe', # Example path using environment variable
    # Add other safe applications here
}

@app.route('/stats', methods=['GET'])
def get_system_stats():
    """Returns real-time system statistics"""
    try:
        # CPU
        cpu_percent = psutil.cpu_percent(interval=0.5)
        cpu_count = psutil.cpu_count()
        
        # Memory
        mem = psutil.virtual_memory()
        mem_total_gb = round(mem.total / (1024**3), 1)
        mem_used_gb = round(mem.used / (1024**3), 1)
        mem_percent = mem.percent
        
        # Disk
        disk = psutil.disk_usage('C:\\')
        disk_total_gb = round(disk.total / (1024**3), 1)
        disk_used_gb = round(disk.used / (1024**3), 1)
        disk_percent = disk.percent
        
        # GPU (Try to get NVIDIA stats if available)
        gpu_stats = None
        try:
            import GPUtil
            gpus = GPUtil.getGPUs()
            if gpus:
                gpu = gpus[0]
                gpu_stats = {
                    'name': gpu.name,
                    'load': round(gpu.load * 100, 1),
                    'temp': gpu.temperature,
                    'memory_used': round(gpu.memoryUsed / 1024, 1),
                    'memory_total': round(gpu.memoryTotal / 1024, 1)
                }
        except:
            pass
        
        return jsonify({
            'status': 'ok',
            'cpu': {
                'percent': cpu_percent,
                'cores': cpu_count
            },
            'memory': {
                'total_gb': mem_total_gb,
                'used_gb': mem_used_gb,
                'percent': mem_percent
            },
            'disk': {
                'total_gb': disk_total_gb,
                'used_gb': disk_used_gb,
                'percent': disk_percent
            },
            'gpu': gpu_stats,
            'platform': platform.system()
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/launch', methods=['POST'])
def launch_application():
    """Launches a local application by name"""
    try:
        data = request.json
        app_name = data.get('app', '').lower()
        args = data.get('args', [])
        
        if app_name not in APP_REGISTRY:
            return jsonify({
                'status': 'error',
                'message': f'Unknown application: {app_name}'
            }), 400
        
        app_path = APP_REGISTRY[app_name]
        
        # Check if executable exists
        if not os.path.exists(app_path):
            return jsonify({
                'status': 'error',
                'message': f'Application not found at: {app_path}'
            }), 404
        
        # Launch the application
        if args:
            subprocess.Popen([app_path] + args)
        else:
            subprocess.Popen([app_path])
        
        return jsonify({
            'status': 'ok',
            'message': f'Launched {app_name}',
            'path': app_path
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Simple health check endpoint"""
    return jsonify({
        'status': 'ok',
        'service': 'Sovereign Interface Backend',
        'version': '1.0.0'
    })

@app.route('/apps', methods=['GET'])
def list_apps():
    """Returns list of registered applications"""
    return jsonify({
        'status': 'ok',
        'apps': list(APP_REGISTRY.keys())
    })

if __name__ == '__main__':
    print("=" * 60)
    print("SOVEREIGN INTERFACE - LOCAL BACKEND")
    print("=" * 60)
    print(f"Server running on: http://localhost:5000")
    print(f"Platform: {platform.system()}")
    print(f"Registered Apps: {len(APP_REGISTRY)}")
    print("\nEndpoints:")
    print("  GET  /health  - Health check")
    print("  GET  /stats   - System statistics")
    print("  POST /launch  - Launch application")
    print("  GET  /apps    - List registered apps")
    print("\nPress Ctrl+C to stop")
    print("=" * 60)
    
    app.run(host='127.0.0.1', port=5000, debug=False)
