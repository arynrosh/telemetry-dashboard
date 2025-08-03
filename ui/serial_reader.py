# ui/serial_reader.py

from PyQt6.QtCore import QThread, pyqtSignal
import serial
import json

class SerialReader(QThread):
    packet_received = pyqtSignal(dict)
    error = pyqtSignal(str)

    def __init__(self, port: str, baud: int = 115200):
        super().__init__()
        self.port = port
        self.baud = baud
        self._running = True
        self.ser = None

    def run(self):
        try:
            self.ser = serial.Serial(self.port, baudrate=self.baud, timeout=1)
        except Exception as e:
            self.error.emit(f"Cannot open {self.port}: {e}")
            return

        while self._running:
            try:
                line = self.ser.readline().decode('utf-8', errors='ignore').strip()
                if line:
                    try:
                        packet = json.loads(line)
                        self.packet_received.emit(packet)
                    except json.JSONDecodeError:
                        # ignore parse errors
                        pass
            except Exception as e:
                self.error.emit(str(e))
                break

        if self.ser and self.ser.is_open:
            self.ser.close()

    def stop(self):
        self._running = False
        self.wait()
