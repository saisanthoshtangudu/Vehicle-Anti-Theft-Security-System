import serial
import time
import pynmea2

# Match your existing working serial setup


print("Parsing GPS data... (Ctrl+C to stop)")


def getLocation(times):
    try:
        location = "Please Wait While fetching the data from gps"
        ser = serial.Serial('/dev/serial0', baudrate=9600, timeout=1)
        while times >= 0:
            if ser.in_waiting > 0:
                # Read and decode the raw line
                raw_line = ser.readline().decode('utf-8', errors='replace').strip()
                
                # Check if it's a valid NMEA sentence starting with $
                if raw_line.startswith('$'):
                    try:
                        # Parse the raw string into a pynmea object
                        msg = pynmea2.parse(raw_line)
                        
                        # Example: Extracting data from GGA sentences (Fix Data)
                        if isinstance(msg, pynmea2.types.talker.GGA):
                            print(f"--- GGA Fix ---")
                            print(f"Time: {msg.timestamp}")
                            print(f"Lat: {msg.latitude} {msg.lat_dir}")
                            print(f"Lon: {msg.longitude} {msg.lon_dir}")
                            print(f"Sats: {msg.num_sats}")
                            print(f"Altitude: {msg.altitude} {msg.altitude_units}")
                            location = f"Lat: {msg.latitude} {msg.lat_dir}\nLon: {msg.longitude} {msg.lon_dir}"
                        # Example: Extracting data from RMC sentences (Recommended Minimum)
                        elif isinstance(msg, pynmea2.types.talker.RMC):
                            print(f"--- RMC Basic ---")
                            print(f"Speed: {msg.spd_over_grnd} knots")
                            print(f"Status: {'Active' if msg.status == 'A' else 'Void (No Fix)'}")
                        times -=1
                    except pynmea2.ParseError as e:
                        # Ignore occasional garbled lines
                        continue
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nStopping...")
    finally:
        ser.close()
        return(location)
