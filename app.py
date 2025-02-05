from flask import Flask, render_template
import serial
import time
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

SERIAL_PORT = "COM3"
BAUD_RATE = 9600

def serial_listener():
    """Mimic test.py's working approach"""
    try:
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
            print(f"Listening to {SERIAL_PORT} at {BAUD_RATE} baud rate...")
            while True:
                if ser.in_waiting > 0:
                    raw_data = ser.readline().decode('utf-8', errors='ignore').strip()
                    
                    # Process exactly like test.py does
                    key_value_pairs = raw_data.split(";")
                    for pair in key_value_pairs[1:]:
                        try:
                            key, value = pair.split(":")
                            key = key.strip()
                            value = float(value.strip())
                            # Emit each value as it's read
                            socketio.emit('data_point', {'key': key, 'value': value})
                        except ValueError:
                            continue
                    time.sleep(0.1)
    except Exception as e:
        print(f"Error: {e}")

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    socketio.start_background_task(serial_listener)
    socketio.run(app, debug=False)  # Disable debug mode
