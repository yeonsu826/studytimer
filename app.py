from flask import Flask, render_template, request, jsonify, send_from_directory
import csv
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/study_cushion')
def study_cushion():
    return render_template('study_cushion.html')

@app.route('/csv_files/data.csv', methods=['GET'])
def download_csv():
    directory = 'D:\YS_D_drive\Website\study_web\csv_files'  
    filename = 'data.csv'
    return send_from_directory(directory, filename, mimetype='text/csv; charset=utf-8')

@app.route('/save_data', methods=['POST'])
def save_data():
    if request.method == 'POST':
        data = request.json

        file_path = 'D:\YS_D_drive\Website\study_web\csv_files/data.csv'
        is_empty = os.stat(file_path).st_size == 0 

        with open(file_path, 'a', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            if is_empty:
                csv_writer.writerow(['Name', 'Time'])
            csv_writer.writerow([data['Name'], data['Time']])

        return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
