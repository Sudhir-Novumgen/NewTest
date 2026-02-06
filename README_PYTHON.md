# 🐍 Flask Attendance Dashboard - Deployment Package

## 📦 What's Included

This package contains all files needed to deploy the **Flask version** of the Attendance Analytics Dashboard with modern UI.

```
flask_deployment_package/
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── templates/
│   └── index.html           # HTML template with modern UI
├── static/
│   ├── css/
│   │   └── style.css        # Modern styling (Inter font, gradients)
│   └── js/
│       └── app.js           # Frontend JavaScript
├── start.sh                 # Linux/Mac startup script
├── start.bat                # Windows startup script
└── README.md               # This file
```

## 🚀 Quick Start (Local)

### Windows:
```batch
start.bat
```

### Linux/Mac:
```bash
chmod +x start.sh
./start.sh
```

### Manual:
```bash
pip install -r requirements.txt
python app.py
```

Then open: **http://localhost:5000**

## 🌐 Deploy Online

### ⚠️ IMPORTANT: Cannot Deploy on Streamlit Cloud!

This is a **Flask app**, not a Streamlit app. You must use different hosting:

### Option 1: Render.com (FREE)

1. **Create account:** https://render.com
2. **New Web Service** → Connect GitHub
3. **Build Command:** `pip install -r requirements.txt`
4. **Start Command:** `gunicorn app:app`
5. **Deploy!**

**Free tier:** 750 hours/month, HTTPS included

### Option 2: Railway.app

1. **Create account:** https://railway.app
2. **New Project** → Deploy from GitHub
3. Railway auto-detects Flask
4. **Deploy!**

**Free trial:** $5 credit

### Option 3: PythonAnywhere (FREE)

1. **Create account:** https://www.pythonanywhere.com
2. Upload files
3. Configure WSGI
4. Run!

**Free tier:** Limited but works

### Option 4: Your Own Server

See `DEPLOYMENT_GUIDE.md` for VPS deployment with custom domain.

## 📋 Requirements

- Python 3.11 or higher
- pip (Python package installer)
- Modern web browser

## 🎨 Features

- ✅ **Modern UI** with Inter font
- ✅ **Gradient backgrounds** (blue/indigo)
- ✅ **Lucide icons**
- ✅ **Smooth animations**
- ✅ **Interactive filters**
- ✅ **Real-time search**
- ✅ **CSV export**
- ✅ **Responsive design**

## 📊 CSV Format

Required CSV columns:

```csv
Date/time,User,Where
2024-01-01 09:00:00,John Doe,Office In
2024-01-01 18:00:00,John Doe,Office Out
```

## 🔧 Configuration

### Change Port
Edit `app.py`, last line:
```python
app.run(debug=True, host='0.0.0.0', port=5000)  # Change port here
```

### Change Target Hours
Edit `app.py`, line 11:
```python
TARGET_WEEKLY_HOURS = 40  # Change to your target
```

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Change port in app.py to 5001 or another port
```

### Module Not Found
```bash
pip install -r requirements.txt
```

### Templates Not Found
```bash
# Ensure templates/ folder is in same directory as app.py
```

## 📦 For Deployment (Add to requirements.txt)

For production deployment, add:
```txt
gunicorn==21.2.0
```

This is required for Render, Railway, and most cloud platforms.

## 🔒 Security

For production:
1. Set `debug=False` in app.py
2. Use environment variables for secrets
3. Enable HTTPS
4. Add authentication if needed

## 📞 Support

Need help?
- Check included documentation files
- Test locally first
- Review deployment guides
- Check platform-specific docs

## ✅ Pre-Deployment Checklist

- [ ] All files present
- [ ] requirements.txt correct
- [ ] Tested locally
- [ ] No syntax errors
- [ ] CSV format matches
- [ ] Port configured
- [ ] Platform chosen

## 🎯 Recommended Deployment

**For beginners:** Use Render.com (free, easy, 15 minutes)
**For advanced:** Use DigitalOcean VPS with custom domain

## 📄 License

Proprietary - Internal company use only

---

**Ready to deploy? Follow the Render.com guide for easiest deployment!**
