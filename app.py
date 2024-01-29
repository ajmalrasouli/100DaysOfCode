from flask import Flask, render_template, request, redirect

app = Flask(__name__)

def log_progress(day, progress):
    with open("100DaysOfCode_Log.txt", 'a') as file:
        file.write(f"Day {day}: {progress}\n")

def view_progress():
    with open("100DaysOfCode_Log.txt", 'r') as file:
        return file.read()

@app.route('/')
def index():
    return render_template('index.html', progress=view_progress())

@app.route('/log', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        day = request.form['day']
        progress = request.form['progress']
        log_progress(day, progress)
        return redirect('/')
    return render_template('log.html')

if __name__ == "__main__":
    app.run(debug=True)