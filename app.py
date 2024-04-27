from flask import Flask, render_template, request, redirect, flash
import datetime
from data_access import log_progress, view_progress, edit_progress, get_progress


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return render_template('index.html', progress=view_progress())

@app.route('/log', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        try:
            day = int(request.form['day'])
            progress = request.form['progress']
            log_progress(day, progress)
            flash('Progress logged successfully!', 'success')
            return redirect('/')
        except ValueError:
            flash('Invalid day number. Please enter a valid integer.', 'error')
        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'error')
    return render_template('log.html')

@app.route('/edit/<int:day>', methods=['POST'])
def edit(day):
    try:
        new_progress = request.json['progress']
        edit_progress(day, new_progress)
        return 'Progress updated successfully!', 200
    except Exception as e:
        return f'An error occurred: {str(e)}', 500

if __name__ == "__main__":
    app.run(debug=True)
