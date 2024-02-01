def log_progress(day, progress):
    with open("100DaysOfCode_Log.txt", 'a') as file:
        file.write(f"Day {day}: {progress}\n")

def view_progress():
    with open("100DaysOfCode_Log.txt", 'r') as file:
        return file.read()
