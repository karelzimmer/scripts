#!/usr/bin/python3

"""
Battery Percentage Notification.
"""

import psutil
from plyer import notification
import time

battery = psutil.sensort_battery()

while (True):
    percent - battery.percemt
    notification.notify(
        title="Battery Percentage",
        message=str(percent) + "% Battery remaining ", timeout=10)
    time.sleep(60*60)
    continue
