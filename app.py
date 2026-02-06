from flask import Flask, render_template, request, jsonify, send_file
import pandas as pd
import json
from datetime import datetime, timedelta
import io
import base64

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

TARGET_WEEKLY_HOURS = 40

def get_week_start(date):
    """Get Monday of the week for a given date"""
    day = date.weekday()
    monday = date - timedelta(days=day)
    return monday.strftime('%Y-%m-%d')

def process_attendance_data(df):
    """Process attendance CSV data and return analytics"""
    try:
        # Clean and prepare data
        df['Date/time'] = pd.to_datetime(df['Date/time'])
        df['Date'] = df['Date/time'].dt.date
        df['Day'] = df['Date/time'].dt.day_name()
        
        # Filter working days only
        working_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        df = df[df['Day'].isin(working_days)]
        
        # Identify In/Out
        df['IO'] = df['Where'].apply(lambda x: 'In' if 'In' in str(x) else ('Out' if 'Out' in str(x) else None))
        
        # Group by user and date to get daily in/out times
        daily_data = []
        for (user, date), group in df.groupby(['User', 'Date']):
            in_times = group[group['IO'] == 'In']['Date/time']
            out_times = group[group['IO'] == 'Out']['Date/time']
            
            if len(in_times) > 0 and len(out_times) > 0:
                in_time = in_times.min()
                out_time = out_times.max()
                working_hours = (out_time - in_time).total_seconds() / 3600
                
                daily_data.append({
                    'user': user,
                    'date': date,
                    'in_time': in_time,
                    'out_time': out_time,
                    'working_hours': working_hours
                })
        
        daily_df = pd.DataFrame(daily_data)
        
        if daily_df.empty:
            return None
        
        # Calculate week start for each date
        daily_df['week'] = daily_df['date'].apply(lambda x: get_week_start(pd.to_datetime(x)))
        
        # Weekly aggregation
        weekly_data = []
        for (user, week), group in daily_df.groupby(['user', 'week']):
            total_hours = group['working_hours'].sum()
            days_worked = len(group)
            gap_hours = TARGET_WEEKLY_HOURS - total_hours
            gap_percent = (gap_hours / TARGET_WEEKLY_HOURS) * 100
            performance_score = (total_hours / TARGET_WEEKLY_HOURS) * 100
            status = 'met' if total_hours >= TARGET_WEEKLY_HOURS else 'below'
            
            weekly_data.append({
                'user': user,
                'week': week,
                'total_hours': round(total_hours, 2),
                'days_worked': days_worked,
                'target_hours': TARGET_WEEKLY_HOURS,
                'gap_hours': round(gap_hours, 2),
                'gap_percent': round(gap_percent, 2),
                'performance_score': round(performance_score, 2),
                'status': status
            })
        
        return weekly_data
    
    except Exception as e:
        print(f"Error processing data: {str(e)}")
        return None

@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle CSV file upload and processing"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not file.filename.endswith('.csv'):
            return jsonify({'error': 'Only CSV files are allowed'}), 400
        
        # Read CSV file
        df = pd.read_csv(file)
        
        # Validate required columns
        required_columns = ['Date/time', 'User', 'Where']
        if not all(col in df.columns for col in required_columns):
            return jsonify({'error': f'CSV must contain columns: {", ".join(required_columns)}'}), 400
        
        # Process data
        weekly_data = process_attendance_data(df)
        
        if weekly_data is None:
            return jsonify({'error': 'Unable to process attendance data. Please check the file format.'}), 400
        
        # Calculate statistics
        total_actual_hours = sum(record['total_hours'] for record in weekly_data)
        total_target_hours = len(weekly_data) * TARGET_WEEKLY_HOURS
        avg_performance = sum(record['performance_score'] for record in weekly_data) / len(weekly_data)
        compliant_records = sum(1 for record in weekly_data if record['status'] == 'met')
        compliance_rate = (compliant_records / len(weekly_data)) * 100
        
        stats = {
            'total_actual_hours': round(total_actual_hours, 1),
            'total_target_hours': total_target_hours,
            'avg_performance': round(avg_performance, 1),
            'compliant_records': compliant_records,
            'compliance_rate': round(compliance_rate, 1),
            'total_records': len(weekly_data)
        }
        
        # Get unique users and weeks
        all_users = sorted(list(set(record['user'] for record in weekly_data)))
        all_weeks = sorted(list(set(record['week'] for record in weekly_data)))
        
        return jsonify({
            'success': True,
            'data': weekly_data,
            'stats': stats,
            'users': all_users,
            'weeks': all_weeks
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/export', methods=['POST'])
def export_data():
    """Export filtered data to CSV"""
    try:
        data = request.json.get('data', [])
        
        if not data:
            return jsonify({'error': 'No data to export'}), 400
        
        # Convert to DataFrame
        df = pd.DataFrame(data)
        
        # Create CSV in memory
        output = io.StringIO()
        df.to_csv(output, index=False)
        output.seek(0)
        
        # Convert to bytes
        csv_bytes = io.BytesIO(output.getvalue().encode('utf-8'))
        
        return send_file(
            csv_bytes,
            mimetype='text/csv',
            as_attachment=True,
            download_name=f'attendance_report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
        )
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
