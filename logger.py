import csv
import math
from datetime import datetime
from pathlib import Path

import serial

PORT = "COM7"
BAUD_RATE = 115200
DEVICE_NAME = "ESP32_Node_1"
CSV_PATH = Path(__file__).with_name("sensor_data.csv")


def main():
    try:
        with serial.Serial(PORT, BAUD_RATE, timeout=1) as connection:
            print(f"Listening on {PORT}. Press Ctrl+C to stop.")

            with CSV_PATH.open("a", newline="", encoding="utf-8") as log:
                writer = csv.writer(log)
                if log.tell() == 0:
                    writer.writerow(["Timestamp", "Device_Name", "Temperature_F"])

                while True:
                    reading = connection.readline().decode(
                        "utf-8", errors="replace"
                    ).strip()

                    try:
                        temperature = float(reading)
                    except ValueError:
                        continue  # Skip empty reads and boot messages.

                    if not math.isfinite(temperature):
                        continue

                    timestamp = datetime.now().isoformat(sep=" ", timespec="seconds")
                    writer.writerow([timestamp, DEVICE_NAME, f"{temperature:.2f}"])
                    log.flush()
                    print(f"[{timestamp}] {DEVICE_NAME} {temperature:.2f} F")

    except KeyboardInterrupt:
        print("\nLogging stopped. Serial port closed.")
    except serial.SerialException as error:
        print(f"Serial error on {PORT}: {error}")


if __name__ == "__main__":
    main()