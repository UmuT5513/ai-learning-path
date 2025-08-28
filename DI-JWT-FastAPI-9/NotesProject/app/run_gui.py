#!/usr/bin/env python3
"""
GUI starter script for Note System
This script helps you run both the API and GUI together
"""

import subprocess
import sys
import time
import threading
import os

def run_api():
    """Run FastAPI server"""
    print("🚀 Starting FastAPI server...")
    try:
        subprocess.run([
            sys.executable, "-m", "uvicorn", 
            "main:app", "--host", "127.0.0.1", 
            "--port", "8000", "--reload"
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ FastAPI server failed to start: {e}")
    except KeyboardInterrupt:
        print("🛑 FastAPI server stopped by user")

def run_streamlit():
    """Run Streamlit GUI"""
    print("🎨 Starting Streamlit GUI...")
    time.sleep(3)  # Wait for API to start
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", 
            "run", "gui_app.py", 
            "--server.port", "8501"
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Streamlit GUI failed to start: {e}")
    except KeyboardInterrupt:
        print("🛑 Streamlit GUI stopped by user")

def main():
    print("=" * 50)
    print("📝 Note System - Starting GUI Application")
    print("=" * 50)
    
    # Check if required files exist
    required_files = ["main.py", "gui_app.py", "models.py", "schemas.py", "base.py", "settings.py"]
    missing_files = [f for f in required_files if not os.path.exists(f)]
    
    if missing_files:
        print(f"❌ Missing required files: {', '.join(missing_files)}")
        print("Please make sure all project files are in the current directory.")
        return
    
    print("📋 Instructions:")
    print("1. FastAPI server will start on: http://127.0.0.1:8000")
    print("2. Streamlit GUI will start on: http://localhost:8501")
    print("3. Use Ctrl+C to stop both servers")
    print("-" * 50)
    
    try:
        # Start both servers in separate threads
        api_thread = threading.Thread(target=run_api, daemon=True)
        gui_thread = threading.Thread(target=run_streamlit, daemon=True)
        
        api_thread.start()
        gui_thread.start()
        
        # Keep main thread alive
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n🛑 Shutting down servers...")
        print("✅ Application stopped successfully!")

if __name__ == "__main__":
    main()
