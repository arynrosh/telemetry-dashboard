# testing/sender_sim.py

import serial
import time
import random
import json
from datetime import datetime

def generate_telemetry(start_ts):
    now = datetime.now()
    elapsed = now - start_ts

    # Stats
    data = {
        "current_time": now.strftime("%H:%M:%S"),
        "run_time": str(elapsed).split('.')[0],  # hh:mm:ss
        "speed": round(random.uniform(0, 80), 1),
        "current": round(random.uniform(-200, 200), 2),
        "energy": round(random.uniform(0, 5), 3),
        "av_speed": round(random.uniform(0, 60), 1),
    }

    # MPPT currents
    mppts = [round(random.uniform(0, 20), 3) for _ in range(4)]
    data["mppt_currents"] = mppts
    data["mppt_total"] = round(sum(mppts), 3)

    # Battery cells: 8×5 grid = 40 cells
    cells = []
    for cell_id in range(40):
        temp = random.uniform(20, 45)
        volt = random.uniform(2.5, 4.2)
        cells.append({"id": cell_id, "temp": round(temp, 1), "voltage": round(volt, 3)})
    data["battery_cells"] = cells

    # Summaries for two packs: Batman (cells 0–19), Robin (20–39)
    def summarize(pack):
        temps = [c["temp"] for c in pack]
        volts = [c["voltage"] for c in pack]
        return {
            "average": round(sum(volts)/len(volts), 3),
            "high": round(max(volts), 3),
            "low": round(min(volts), 3),
            "current": round(random.uniform(0, 50), 2)
        }

    batman = summarize(cells[:20])
    robin  = summarize(cells[20:])
    data["batman"] = batman
    data["robin"]  = robin

    return data

def main():
    port_name = "COM13"   # <-- sender port (paired with COM11)
    baud = 115200
    start_ts = datetime.now()

    print(f"[sender_sim] Sending to {port_name} at {baud} baud…")
    with serial.Serial(port_name, baudrate=baud, timeout=1) as ser:
        while True:
            packet = generate_telemetry(start_ts)
            line = json.dumps(packet)
            ser.write((line + "\n").encode())
            print(f"[sender_sim] → {line}")
            time.sleep(1)

if __name__ == "__main__":
    main()
