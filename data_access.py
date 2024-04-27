def log_progress(day, progress):
    with open("100DaysOfCode_Log.txt", 'a') as file:
        file.write(f"Day {day}: {progress}\n")

def view_progress():
    progress = {}
    with open("100DaysOfCode_Log.txt", 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.split(':')
            if len(parts) >= 2:
                day = parts[0].strip().split(' ')[1]  # Extract day number
                description = ':'.join(parts[1:]).strip()  # Join remaining parts as description
                progress[day] = description
    return progress

def edit_progress(day, new_progress):
    with open("100DaysOfCode_Log.txt", 'r+') as file:
        lines = file.readlines()
        if len(lines) >= day:
            lines[day - 1] = f"Day {day}: {new_progress}\n"
            file.seek(0)
            file.writelines(lines)
        else:
            raise ValueError(f"No progress found for day {day}.")

def get_progress(day):
    with open("100DaysOfCode_Log.txt", 'r') as file:
        lines = file.readlines()
        return lines[day - 1].split(':', 1)[1].strip() if len(lines) >= day else ''
