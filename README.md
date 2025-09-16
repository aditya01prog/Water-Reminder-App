# Water Reminder App

A simple Python script that reminds you to drink water at regular intervals using system notifications. Staying hydrated is essential for good health, and this lightweight app helps you stay on track throughout the day.

## Features
- Sends hourly desktop notifications reminding you to drink water.
- Runs in the background with minimal setup.
- Works across Windows, macOS, and Linux (with the `plyer` library).
- Easy to customize the interval and message.

## Requirements
- Python 3.x
- `plyer` library

Install the required library using:
    pip install plyer

## How to use
1. Clone or download this repository.
2. Install the `plyer` library if not already installed.
3. Run the script using:
    python water_reminder.py
4. A notification will pop up every hour reminding you to drink water.
5. Press `Ctrl + C` in the terminal to stop the script.

## Customization
You can change the interval or notification message by editing the script:
- `interval_minutes = 60` → Set how often the notification appears (in minutes).
- `message_title` and `message_body` → Edit the title and message text.

## Disclaimer
This is a basic reminder tool and not a medical device. For serious hydration concerns, consult a healthcare professional.

---

Stay hydrated and healthy!
