import serial

SERIAL_PORT = "COM3"  # Replace with your serial port
BAUD_RATE = 9600

def extract_temperature(raw_data):
    """
    Extracts and prints the temperature value from the raw data.
    """

    # Split by spaces to extract potential key-value pairs
    key_value_pairs = raw_data.split(";")
    
    for pair in key_value_pairs[1:]:
        #if pair.startswith("Temp:"):  # Look for the key "Temp:"
        key, value = pair.split(":")
        print(f"{key}: {value}")  # Print only the temperature value
            #return  # Stop after finding the temperature
    

def main():
    try:
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
            print(f"Listening to {SERIAL_PORT} at {BAUD_RATE} baud rate...")
            while True:
                if ser.in_waiting > 0:
                    raw_data = ser.readline().decode('utf-8', errors='ignore').strip()
                    print("Raw Data:", raw_data)  # Print raw data for debugging
                    extract_temperature(raw_data)  # Extract and print only temperature
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()
