import json
import pandas as pd
from datetime import datetime
import requests
import openpyxl
# print(openpyxl.__version__)

import json
import pandas as pd
from datetime import datetime
import requests


class Notification:
    def __init__(self, event_id, event_type, timestamp, message):
        self.event_id = event_id
        self.event_type = event_type
        self.timestamp = timestamp
        self.message = message

    def to_dict(self):
        return {
            "Event ID": self.event_id,
            "Event Type": self.event_type,
            "Timestamp": self.timestamp,
            "Message": self.message,
        }


class Task:
    def __init__(self, task_id, task_name, assigned_to, due_date, status):
        self.task_id = task_id
        self.task_name = task_name
        self.assigned_to = assigned_to
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "Task ID": self.task_id,
            "Task Name": self.task_name,
            "Assigned To": self.assigned_to,
            "Due Date": self.due_date,
            "Status": self.status,
        }


def fetch_event_notifications():
    url = "https://api.adp.com/event-notifications"
    headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return []


def generate_notifications():
    notifications = [
        Notification("N001", "Task Assigned", datetime.now().isoformat(), "You have been assigned a new task."),
        Notification("N002", "Task Completed", datetime.now().isoformat(), "Your task has been marked as completed."),
        Notification("N003", "New Event", datetime.now().isoformat(), "An event has been scheduled."),
        Notification("N004", "Policy Update", datetime.now().isoformat(), "Company policies have been updated."),
        Notification("N005", "System Alert", datetime.now().isoformat(), "System maintenance scheduled."),
        Notification("N006", "Approval Required", datetime.now().isoformat(),
                     "Your approval is required for a request."),
        Notification("N007", "Reminder", datetime.now().isoformat(), "Upcoming deadline for your task."),
        Notification("N008", "HR Notification", datetime.now().isoformat(), "HR has updated employee benefits."),
        Notification("N009", "Project Update", datetime.now().isoformat(), "Your project has new updates."),
        Notification("N010", "Meeting Scheduled", datetime.now().isoformat(), "A meeting has been scheduled for you."),
    ]
    return notifications


def generate_tasks():
    tasks = [
        Task("T001", "Review Payroll", "John Doe", "2025-02-25", "Pending"),
        Task("T002", "Approve Benefits", "Jane Smith", "2025-03-01", "In Progress"),
        Task("T003", "Update Employee Records", "Alice Johnson", "2025-03-05", "Completed"),
        Task("T004", "Schedule Meeting", "Robert Brown", "2025-03-10", "Pending"),
        Task("T005", "Audit Financial Reports", "Emily Davis", "2025-03-15", "In Progress"),
        Task("T006", "Conduct Training", "Michael Wilson", "2025-03-20", "Pending"),
        Task("T007", "Implement Security Policies", "Sarah Lee", "2025-03-25", "Completed"),
        Task("T008", "Generate Monthly Report", "Chris Martin", "2025-03-30", "Pending"),
        Task("T009", "Optimize HR Process", "Emma White", "2025-04-05", "In Progress"),
        Task("T010", "Review Compliance", "David Clark", "2025-04-10", "Pending"),
    ]
    return tasks


def save_to_excel(notifications, tasks, filename="notification_task_data.xlsx"):
    notifications_df = pd.DataFrame([n.to_dict() for n in notifications])
    tasks_df = pd.DataFrame([t.to_dict() for t in tasks])

    with pd.ExcelWriter(filename) as writer:
        notifications_df.to_excel(writer, sheet_name="Notifications", index=False)
        tasks_df.to_excel(writer, sheet_name="Tasks", index=False)

    print(f"Data saved to {filename}")


if __name__ == "__main__":
    notifications = generate_notifications()
    tasks = generate_tasks()
    save_to_excel(notifications, tasks)
