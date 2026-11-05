import platform
import socket
import os
from datetime import datetime


def generate_health_report():

    environment = os.getenv("APP_ENV", "Development")

    report = {
        "Hostname": socket.gethostname(),
        "Operating System": platform.system(),
        "OS Version": platform.version(),
        "Python Version": platform.python_version(),
        "Environment": environment,
        "Report Generated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return report


def save_report():

    report = generate_health_report()

    with open("health_report.txt", "w") as file:

        file.write("===== SYSTEM HEALTH REPORT =====\n\n")

        for key, value in report.items():
            file.write(f"{key}: {value}\n")

    print("Health report generated successfully!")


if __name__ == "__main__":
    save_report()