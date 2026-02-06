# 🐍 Attendance Analytics Dashboard - Python Flask Edition

Modern, professional attendance analytics dashboard built with Flask, featuring the same sleek UI design with Inter font, gradient backgrounds, and smooth animations.

![Version](https://img.shields.io/badge/version-2.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![Flask](https://img.shields.io/badge/flask-3.0.0-red)
![License](https://img.shields.io/badge/license-Proprietary-yellow)

## ✨ Features

### 🎨 Modern UI Design
- **Inter Font** - Professional Google Fonts typography
- **Lucide Icons** - Beautiful, consistent iconography
- **Gradient Backgrounds** - Slate-to-blue modern gradients
- **Smooth Animations** - CSS transitions and hover effects
- **Responsive Layout** - Mobile-first design
- **Glass Morphism** - Modern translucent card effects

### 📊 Analytics Features
- **Real-time CSV Processing** - Instant data analysis
- **5 KPI Metrics** - Key performance indicators at a glance
- **Interactive Filters** - Multi-select users and weeks
- **Live Search** - Real-time employee search
- **Performance Tracking** - Individual & team metrics
- **Compliance Monitoring** - Target achievement tracking
- **Data Export** - Download filtered reports as CSV

### 🎯 Dashboard Views
1. **Overview** - Performance distribution & top performers
2. **Weekly Analysis** - Week-by-week breakdown
3. **User Comparison** - Employee performance ranking
4. **Detailed Data** - Complete data table with sorting

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

**Option 1: Automatic (Recommended)**

**On Linux/Mac:**
```bash
chmod +x start.sh
./start.sh
```

**On Windows:**
```batch
start.bat
```

**Option 2: Manual**

```bash
# Install dependencies
pip install -r requirements.txt

# Start application
python app.py
```

### Access Dashboard
Open browser and navigate to: **http://localhost:5000**

## 📁 Project Structure

```
attendance-dashboard/
├── app.py                    # Flask backend (API & routing)
├── requirements.txt          # Python dependencies
├── templates/
│   └── index.html           # Main HTML template
├── static/
│   ├── css/
│   │   └── style.css        # Modern UI styles (Inter font, gradients)
│   └── js/
│       └── app.js           # Frontend JavaScript (filters, charts)
├── start.sh                 # Linux/Mac startup script
├── start.bat                # Windows startup script
├── SETUP_GUIDE.md          # Detailed setup instructions
└── sample-attendance.csv    # Sample data for testing
```

## 📊 CSV Format

Required columns in your CSV file:

```csv
Date/time,User,Where
2024-01-01 09:00:00,John Doe,Office In
2024-01-01 18:00:00,John Doe,Office Out
2024-01-02 09:15:00,Jane Smith,Office In
2024-01-02 17:45:00,Jane Smith,Office Out
```

**Column Requirements:**
- `Date/time`: Format `YYYY-MM-DD HH:MM:SS`
- `User`: Employee name (string)
- `Where`: Must contain "In" or "Out" keyword

## 🎨 UI Components

### Stats Cards
- Total Hours Worked
- Target Hours
- Average Performance
- Compliance Rate
- Total Records

### Interactive Elements
- Search bar with real-time filtering
- Checkbox filters for users and weeks
- Tab navigation (4 views)
- Export button for CSV download
- Loading overlay with spinner

### Color Scheme
- **Primary Blue**: #3B82F6
- **Indigo**: #6366F1
- **Success Green**: #10B981
- **Warning Amber**: #F59E0B
- **Danger Red**: #EF4444
- **Slate Grays**: #F8FAFC - #0F172A

## ⚙️ Configuration

### Change Target Weekly Hours
Edit `app.py`, line 11:
```python
TARGET_WEEKLY_HOURS = 40  # Modify as needed
```

### Change Server Port
Edit `app.py`, last line:
```python
app.run(debug=True, host='0.0.0.0', port=5000)  # Change port
```

### Adjust Upload File Size
Edit `app.py`, line 9:
```python
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit
```

## 📦 Dependencies

```
Flask==3.0.0           # Web framework
pandas==2.1.4          # Data processing & analysis
Werkzeug==3.0.1        # WSGI utilities
openpyxl==3.1.2        # Excel support (optional)
python-dateutil==2.8.2 # Date parsing utilities
```

Install all:
```bash
pip install -r requirements.txt
```

## 🚢 Deployment Options

### 1. Local Development
```bash
python app.py
# Access at http://localhost:5000
```

### 2. Production with Gunicorn
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### 3. Docker
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

```bash
docker build -t attendance-dashboard .
docker run -p 5000:5000 attendance-dashboard
```

### 4. PythonAnywhere (Free Hosting)
1. Upload files to PythonAnywhere
2. Create web app (Flask)
3. Configure WSGI
4. Reload app

### 5. Heroku
```bash
# Create Procfile
echo "web: gunicorn app:app" > Procfile

# Deploy
heroku create attendance-dashboard
git push heroku master
```

## 🐛 Troubleshooting

### Issue: Port already in use
```bash
# Linux/Mac
lsof -ti:5000 | xargs kill -9

# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### Issue: Module not found
```bash
pip install -r requirements.txt --upgrade
```

### Issue: CSV upload fails
- Verify CSV format matches requirements
- Check file size (< 16MB)
- Ensure Date/time format is correct
- Confirm 'In' or 'Out' keywords in Where column

### Issue: Styles not loading
- Clear browser cache (Ctrl+Shift+R)
- Check browser console for errors (F12)
- Restart Flask server

## 🔒 Security (Production)

```python
# In app.py
import os

# Use environment variables
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'change-in-production')

# Disable debug mode
app.run(debug=False, host='0.0.0.0', port=5000)
```

Additional recommendations:
- Enable HTTPS
- Add authentication
- Implement rate limiting
- Use environment variables for secrets
- Regular dependency updates

## 📈 Performance Tips

### For Large CSV Files:
```python
# Add chunking in pandas
chunks = pd.read_csv(file, chunksize=1000)
for chunk in chunks:
    process_chunk(chunk)
```

### Add Caching:
```python
from flask_caching import Cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@cache.cached(timeout=300)
def process_data(df):
    # Processing logic
```

### Database Integration (Future):
```python
# Replace CSV with SQLite/PostgreSQL
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance.db'
```

## 🎯 Usage Guide

### 1. Upload Data
- Click "Choose File" button
- Select attendance CSV file
- Wait for processing (loading overlay)

### 2. View Analytics
- Automatic stats calculation
- 5 KPI cards at top
- Multiple tab views

### 3. Filter Data
- Click "Filters" button
- Select/deselect users
- Select/deselect weeks
- Live updates

### 4. Search Employees
- Type name in search box
- Real-time filtering
- Works with filters

### 5. Export Report
- Apply desired filters
- Click "Export Report"
- CSV downloads automatically

## 🔄 Updates

### Check for Updates
```bash
pip list --outdated
```

### Update Dependencies
```bash
pip install --upgrade -r requirements.txt
```

### Security Audit
```bash
pip install safety
safety check
```

## 📊 API Endpoints

### POST /upload
Upload and process CSV file
- **Input**: multipart/form-data with CSV file
- **Output**: JSON with processed data and stats

### POST /export
Export filtered data to CSV
- **Input**: JSON with filtered data array
- **Output**: CSV file download

## 🤝 Support

For issues or questions:
1. Check SETUP_GUIDE.md
2. Review error messages in terminal
3. Check browser console (F12)
4. Contact development team

## 📝 Changelog

### Version 2.0.0 (2026-02-06)
- ✨ Complete UI redesign with Inter font
- 🎨 Modern gradient backgrounds
- 📊 Enhanced analytics views
- 🔍 Real-time search and filtering
- 💾 CSV export functionality
- 📱 Fully responsive design
- ⚡ Performance optimizations

### Version 1.0.0
- Initial release
- Basic CSV processing
- Simple table view

## 📄 License

Proprietary - Internal company use only

## 🙏 Credits

- **Flask** - Web framework
- **Pandas** - Data processing
- **Inter Font** - Google Fonts
- **Lucide** - Icon library
- **Tailwind CSS** - Design inspiration

---

**Built with ❤️ using Flask, Pandas, and Modern Web Technologies**

**Version**: 2.0.0  
**Last Updated**: February 2026  
**Python**: 3.8+  
**Flask**: 3.0.0
