import datetime

def log_progress(log_file, day, progress):
    with open(log_file, 'a') as file:
        file.write(f"Day {day}: {progress}\n")

def view_progress(log_file):
    with open(log_file, 'r') as file:
        print(file.read())

def main():
    log_file = "100DaysOfCode_Log.txt"

    while True:
        print("1. Log Progress")
        print("2. View Progress")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            day = int(input("Enter the day number: "))
            progress = input("Enter your progress: ")
            log_progress(log_file, day, progress)
            print("Progress logged successfully!")

        elif choice == '2':
            view_progress(log_file)

        elif choice == '3':
            print("Exiting the app. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()