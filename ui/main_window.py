# ui/main_window.py

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QComboBox, QPushButton,
    QHBoxLayout, QVBoxLayout, QGridLayout, QGroupBox, QMessageBox
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import sys
from serial.tools import list_ports

from ui.widgets.battery_cell import BatteryCell
from ui.widgets.plot_display import PlotDisplay
from ui.widgets.stats_panel import StatsPanel
from ui.serial_reader import SerialReader  # <-- your serial reader thread

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ogopogo Solar Telemetry System")
        self.setWindowIcon(QIcon("assets/logo.png"))

        # Placeholder for our reader thread
        self.serial_thread = None

        self.init_ui()
        self.refresh_com_ports()

    def init_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout(central)

        # Top: battery grid / stats / plots
        top_layout = QHBoxLayout()

        # ── Battery Grid ──────────────────────────────────────
        battery_group = QGroupBox("Battery Cells")
        battery_layout = QGridLayout(battery_group)

        self.battery_cells = []
        rows, cols = 4, 5  # 40 cells
        for r in range(rows):
            for c in range(cols):
                idx = r * cols + c
                cell = BatteryCell(cell_id=idx)
                battery_layout.addWidget(cell, r, c)
                self.battery_cells.append(cell)

        top_layout.addWidget(battery_group, stretch=3)

        # ── Stats Panel ──────────────────────────────────────
        self.stats_panel = StatsPanel()
        top_layout.addWidget(self.stats_panel, stretch=1)

        # ── Plots Panel ──────────────────────────────────────
        plot_group = QGroupBox("Telemetry Plots")
        plot_layout = QVBoxLayout(plot_group)

        self.plots = []
        titles = [
            "Speed (mph)",
            "Motor Current (A)",
            "Array Current (A)",
            "Total Battery Voltage (V)"
        ]
        for t in titles:
            p = PlotDisplay(title=t)
            plot_layout.addWidget(p)
            self.plots.append(p)

        top_layout.addWidget(plot_group, stretch=3)

        main_layout.addLayout(top_layout)

        # Bottom: control panel
        control_layout = QHBoxLayout()

        control_layout.addWidget(QLabel("COM Port:"))
        self.com_port_combo = QComboBox()
        control_layout.addWidget(self.com_port_combo)

        self.change_port_btn = QPushButton("Refresh Ports")
        self.change_port_btn.clicked.connect(self.refresh_com_ports)
        control_layout.addWidget(self.change_port_btn)

        self.start_btn = QPushButton("Start Monitor")
        self.start_btn.clicked.connect(self.start_monitor)
        control_layout.addWidget(self.start_btn)

        self.stop_btn = QPushButton("Stop Monitor")
        self.stop_btn.clicked.connect(self.stop_monitor)
        control_layout.addWidget(self.stop_btn)

        self.stop_log_btn = QPushButton("Stop Logging")
        # connect to your logging‑stop logic if needed
        control_layout.addWidget(self.stop_log_btn)

        self.exit_btn = QPushButton("Exit")
        self.exit_btn.clicked.connect(self.close)
        control_layout.addWidget(self.exit_btn)

        main_layout.addLayout(control_layout)

    def refresh_com_ports(self):
        """Rescan and populate available serial ports."""
        self.com_port_combo.clear()
        for port in list_ports.comports():
            self.com_port_combo.addItem(port.device)

    def start_monitor(self):
        """Start reading from the selected COM port."""
        port = self.com_port_combo.currentText()
        if not port:
            QMessageBox.warning(self, "No Port Selected", "Please select a COM port first.")
            return

        # Prevent double‑starting
        if self.serial_thread and self.serial_thread.isRunning():
            return

        # Create and launch the reader thread
        self.serial_thread = SerialReader(port=port, baud=115200)
        self.serial_thread.packet_received.connect(self.handle_packet)
        self.serial_thread.error.connect(lambda msg: QMessageBox.critical(self, "Serial Error", msg))
        self.serial_thread.start()

    def stop_monitor(self):
        """Stop the reader thread cleanly."""
        if self.serial_thread:
            self.serial_thread.stop()
            self.serial_thread = None

    def handle_packet(self, packet: dict):
        """Receive parsed JSON telemetry and update all widgets."""
        # 1) Stats
        self.stats_panel.update_stats(packet)

        # 2) Battery cells
        for cell_data in packet.get("battery_cells", []):
            cid = cell_data.get("id")
            if 0 <= cid < len(self.battery_cells):
                self.battery_cells[cid].update_data(cell_data["temp"], cell_data["voltage"])

        # 3) Plots
        self.plots[0].add_data_point(packet.get("speed", 0))
        self.plots[1].add_data_point(packet.get("current", 0))
        self.plots[2].add_data_point(packet.get("mppt_total", 0))
        # e.g. use first cell voltage for the 4th plot
        if packet.get("battery_cells"):
            self.plots[3].add_data_point(packet["battery_cells"][0]["voltage"])

def launch_app():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.resize(1200, 700)
    w.show()
    sys.exit(app.exec())
