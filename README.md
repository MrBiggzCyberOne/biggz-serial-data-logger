# The Serial Data Logger

An ESP32-S3 running MicroPython generates a simulated Fahrenheit reading every two seconds and sends it as a line of text over USB serial. On the PC, `logger.py` reads those lines with pySerial, skips nonnumeric and nonfinite values, and adds a local timestamp and device name to each valid reading.

The logger appends readings to `sensor_data.csv` beside `logger.py`. It writes the header when the file is empty and flushes each reading after writing it. The columns are `Timestamp`, `Device_Name`, and `Temperature_F`.

## Requirements

- Python 3 on the PC with the `pyserial` package.
- An ESP32 with a USB data cable and a MicroPython emitter already running on the board. The emitter should print one numeric reading per line.
- The ESP32's serial port. This setup uses `COM7` at 115200 baud. Set `PORT` in `logger.py` to match your computer.

## Run the logger

1. Connect the ESP32 over USB and start the emitter. If it is installed as `main.py`, reset the board to start it automatically.
2. Close Thonny and any other serial monitor so the logger can open the port.
3. Open a terminal in the folder containing `logger.py` and run these commands.

   ```powershell
   python -m pip install pyserial
   python .\logger.py
   ```

4. Watch for timestamped readings in the terminal. Press **Ctrl+C** to stop. The context managers close the serial port and CSV file.
5. Open `sensor_data.csv` beside the script to review the data. Restarting the logger appends readings below the existing rows.

The generated CSV stays on the PC. The MicroPython emitter stays on the board and in the local lab files.

