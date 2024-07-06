from pynotifier import Notification
import psutil

# Get the battery information
battery = psutil.sensors_battery()
percent = battery.percent

# Print the battery percentage
print(f"Battery percentage: {percent}%")

# Send a notification with the battery percentage
Notification(
    title="Battery Percentage",
    description=f"{percent}% Percent Remaining",
    duration=10
).send()
