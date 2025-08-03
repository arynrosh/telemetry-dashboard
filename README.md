# Telemetry GUI

A modernized, modular, and user-friendly graphical interface for real-time telemetry data visualization.

This project is a personal reimplementation and UI overhaul of the original [Kentucky Solar Car Team's Telemetry GUI](https://github.com/KentuckySolarCar/Telemetry-GUI). It is built to provide better maintainability, a more intuitive interface, and improved adaptability for solar car racing applications and other embedded telemetry systems.

Note: This is a personal project created independently for educational and developmental purposes.

---

## Features

- Real-time telemetry display  
- Serial communication support (configurable via `config.json`)  
- Mock mode for testing without hardware  
- Live charting (voltage, current, speed, temperatures, etc.)  
- Modular UI components (battery info, motor status, alerts)  
- Optional logging of received data to file  
- Clean architecture with separation of core logic and UI  
- Future support planned for theming and CAN integration  

---

## Project Structure

```
Telemetry-GUI/
├── core/               # Serial communication, data parsing, logging
│   ├── serial_reader.py
│   ├── data_parser.py
│   └── logger.py
├── modules/            # Reusable UI widgets (BatteryCell, MotorInfo, etc.)
│   ├── battery_cell.py
│   ├── motor_info.py
│   └── ...
├── ui/                 # Main window and page layout
│   ├── main_window.py
│   ├── home_page.py
│   └── ...
├── config.json         # Settings for serial port, mock mode, etc.
├── main.py             # Application entry point
├── requirements.txt    # Python dependencies
└── README.md           # You're reading it!
```

---

## Technologies Used

- Python 3.11+  
- PyQt6 – Modern GUI framework  
- PySerial – Serial communication  
- matplotlib – Live data charting  

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/KentuckySolarCar/Telemetry-GUI.git
cd Telemetry-GUI
```

### 2. Install Dependencies

Make sure you're using Python 3.11 or higher.

```bash
pip install -r requirements.txt
```

### 3. Configure Serial Settings

Open `config.json` and set the appropriate serial port and baudrate. Example:

```json
{
  "use_mock": false,
  "port": "COM3",
  "baudrate": 115200
}
```

Set `"use_mock": true` if you want to simulate data for testing purposes.

### 4. Run the App

```bash
python main.py
```

---

## Screenshots

<img width="1496" height="991" alt="image" src="https://github.com/user-attachments/assets/b7103400-1529-42a0-980d-8f229c869474" />


---

## Future Improvements

- [ ] Serial settings UI panel  
- [ ] Dark mode toggle  
- [ ] Data export (CSV/JSON)  
- [ ] CAN bus integration  
- [ ] Remote streaming capability  
- [ ] Improved diagnostics and error logging  

---

## FAQ

Q: Can I use this for my own solar car project?  
A: Yes. This is designed to be adaptable. You're free to fork and customize it.

Q: What if I don't have hardware yet?  
A: Enable mock mode in `config.json` to simulate telemetry data and test the interface.

Q: Why PyQt6 instead of Tkinter or Qt5?  
A: PyQt6 provides a more modern look and better long-term support.

---

## Author

Aryan Roshan [@arynrosh]  

---

## License

This project is licensed under the MIT License.  
Original concept and architecture based on [Kentucky Solar Car Team's Telemetry GUI](https://github.com/KentuckySolarCar/Telemetry-GUI).
