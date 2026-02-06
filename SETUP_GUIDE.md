# 🐍 Python Flask Attendance Dashboard - Setup Guide

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Web browser (Chrome, Firefox, Safari, Edge)

## 🚀 Quick Start

### 1. Install Python

**Windows:**
- Download from https://www.python.org/downloads/
- Run installer and check "Add Python to PATH"

**Mac:**
```bash
brew install python3
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### 2. Install Dependencies

```bash
# Navigate to project directory
cd attendance-dashboard

# Install required packages
pip install -r requirements.txt
```

### 3. Run the Application

```bash
# Start Flask server
python app.py
```

The application will start at: **http://localhost:5000**

### 4. Access Dashboard

1. Open your web browser
2. Go to `http://localhost:5000`
3. Upload your attendance CSV file
4. Explore the analytics!

## 📁 Project Structure

```
attendance-dashboard/
├── app.py                    # Flask application (main backend)
├── requirements.txt          # Python dependencies
├── templates/
│   └── index.html           # Main HTML template
├── static/
│   ├── css/
│   │   └── style.css        # Modern UI styles
│   └── js/
│       └── app.js           # Frontend JavaScript
└── sample-attendance.csv    # Sample data file
```

## 📊 CSV File Format

Your attendance CSV must have these columns:

```csv
Date/time,User,Where
2024-01-01 09:00:00,John Doe,Office In
2024-01-01 18:00:00,John Doe,Office Out
```

**Column Details:**
- `Date/time`: Format `YYYY-MM-DD HH:MM:SS`
- `User`: Employee name
- `Where`: Must contain "In" or "Out" keyword

## 🎨 Features

### Modern UI Components
- ✅ Inter font (Google Fonts)
- ✅ Lucide icons
- ✅ Gradient backgrounds
- ✅ Smooth animations
- ✅ Responsive design

### Analytics Features
- 📊 5 Key Performance Metrics
- 🔍 Real-time search
- 📅 Week/User filters
- 📈 Performance distribution
- 🏆 Top performers ranking
- 📋 Detailed data table
- 💾 CSV export functionality

## 🔧 Configuration

### Change Target Hours

Edit `app.py`, line 11:
```python
TARGET_WEEKLY_HOURS = 40  # Change to your target
```

### Change Port

Edit `app.py`, last line:
```python
app.run(debug=True, host='0.0.0.0', port=5000)  # Change port here
```

### Upload File Size Limit

Edit `app.py`, line 9:
```python
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB
```

## 🐛 Troubleshooting

### Issue: Module not found

**Solution:**
```bash
pip install -r requirements.txt --upgrade
```

### Issue: Port already in use

**Solution:**
```bash
# Change port in app.py or kill existing process
# On Linux/Mac:
lsof -ti:5000 | xargs kill -9

# On Windows:
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### Issue: CSV upload fails

**Solution:**
- Check CSV format matches requirements
- Ensure file has .csv extension
- Verify Date/time column format
- Check file size (must be under 16MB)

### Issue: Styles not loading

**Solution:**
```bash
# Clear browser cache (Ctrl+Shift+R)
# Or restart Flask server
```

## 🚢 Deployment

### Option 1: Local Network Access

```bash
# Run Flask to allow access from other devices
python app.py
# Access from other devices: http://<your-ip>:5000
```

### Option 2: Production Server (Gunicorn)

```bash
# Install Gunicorn
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Option 3: Docker

Create `Dockerfile`:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

Build and run:
```bash
docker build -t attendance-dashboard .
docker run -p 5000:5000 attendance-dashboard
```

### Option 4: PythonAnywhere (Free Hosting)

1. Create account at https://www.pythonanywhere.com
2. Upload files
3. Create new web app (Flask)
4. Configure WSGI file
5. Reload web app

### Option 5: Heroku

```bash
# Create Procfile
echo "web: gunicorn app:app" > Procfile

# Create runtime.txt
echo "python-3.11.0" > runtime.txt

# Deploy
git init
heroku create
git add .
git commit -m "Deploy"
git push heroku master
```

## 📦 Dependencies Explained

```
Flask==3.0.0           # Web framework
pandas==2.1.4          # Data processing
Werkzeug==3.0.1        # WSGI utilities
openpyxl==3.1.2        # Excel support (future)
python-dateutil==2.8.2 # Date parsing
```

## 🔒 Security Notes

### For Production:
1. Set `debug=False` in app.py
2. Use environment variables for secrets
3. Enable HTTPS
4. Add rate limiting
5. Implement authentication

Example with environment variables:
```python
import os

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')
app.config['DEBUG'] = os.getenv('FLASK_DEBUG', 'False') == 'True'
```

## 🎯 Usage Examples

### Basic Upload
1. Click "Choose File"
2. Select CSV file
3. Wait for processing
4. View analytics

### Filtering Data
1. Click "Filters" button
2. Select/deselect users
3. Select/deselect weeks
4. Data updates automatically

### Searching
1. Type employee name in search box
2. Results filter in real-time

### Exporting
1. Apply desired filters
2. Click "Export Report"
3. CSV downloads automatically

## 🔄 Updates & Maintenance

### Update Dependencies
```bash
pip install --upgrade -r requirements.txt
```

### Check for Security Issues
```bash
pip install safety
safety check
```

### Run Tests (if implemented)
```bash
python -m pytest
```

## 📈 Performance Tips

### For Large Files:
1. Increase chunk size in pandas
2. Use server with more RAM
3. Implement pagination
4. Cache processed data

### Optimize Loading:
```python
# Add caching
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@cache.cached(timeout=300)
def process_data(df):
    # ... processing code
```

## 🤝 Support

For issues:
1. Check this documentation
2. Review error messages in terminal
3. Check browser console (F12)
4. Create issue in repository

## 📝 Version Info

- **Version**: 2.0.0
- **Flask**: 3.0.0
- **Python**: 3.8+
- **Last Updated**: February 2026

---

**Built with ❤️ using Flask, Pandas, and Modern Web Technologies**
