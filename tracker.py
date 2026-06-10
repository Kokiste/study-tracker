import datetime
import csv

def log_session():
    date = datetime.date.today()
    topic = input("What did you study? ")
    duration = input("How many minutes did you study? ")
    with open("sessions.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, topic, duration])
        print("Session Logged!")

log_session()