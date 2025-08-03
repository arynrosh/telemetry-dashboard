# # ui/widgets/battery_cell.py

# from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout
# from PyQt6.QtCore import Qt

# class BatteryCell(QFrame):
#     def __init__(self, cell_id=0):
#         super().__init__()
#         self.cell_id = cell_id
#         self.setFrameShape(QFrame.Shape.Box)
#         self.setFixedSize(100, 80)

#         layout = QVBoxLayout()
#         layout.setContentsMargins(5, 5, 5, 5)

#         self.temp_label = QLabel("Temp: -- °C")
#         self.temp_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

#         self.voltage_label = QLabel("Volt: -- V")
#         self.voltage_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

#         self.cell_label = QLabel(f"Cell {self.cell_id}")
#         self.cell_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

#         layout.addWidget(self.cell_label)
#         layout.addWidget(self.temp_label)
#         layout.addWidget(self.voltage_label)

#         self.setLayout(layout)

#     def update_data(self, temp: float, voltage: float):
#         self.temp_label.setText(f"Temp: {temp:.1f} °C")
#         self.voltage_label.setText(f"Volt: {voltage:.2f} V")

# ui/widgets/battery_cell.py

from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout, QProgressBar
from PyQt6.QtCore import Qt

class BatteryCell(QFrame):
    """
    A visually enhanced battery cell widget showing voltage and temperature
    as progress bars with dynamic labels.
    """
    MIN_VOLT = 2.5
    MAX_VOLT = 4.2
    MIN_TEMP = 0
    MAX_TEMP = 60

    def __init__(self, cell_id: int = 0):
        super().__init__()
        self.cell_id = cell_id
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setFixedSize(140, 100)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)

        # Cell identifier
        self.cell_label = QLabel(f"Cell {self.cell_id}")
        self.cell_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = self.cell_label.font()
        font.setBold(True)
        self.cell_label.setFont(font)

        # Voltage progress bar
        self.voltage_bar = QProgressBar()
        self.voltage_bar.setRange(0, 100)
        self.voltage_bar.setTextVisible(True)
        self.voltage_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.voltage_bar.setFormat("--- V")
        self.voltage_bar.setStyleSheet(
            "QProgressBar { border: 1px solid #bbb; border-radius: 3px; text-align: center; }"
            "QProgressBar::chunk { background-color: #3478f6; }"
        )

        # Temperature progress bar
        self.temp_bar = QProgressBar()
        self.temp_bar.setRange(0, 100)
        self.temp_bar.setTextVisible(True)
        self.temp_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.temp_bar.setFormat("--- °C")
        self.temp_bar.setStyleSheet(
            "QProgressBar { border: 1px solid #bbb; border-radius: 3px; text-align: center; }"
            "QProgressBar::chunk { background-color: #f68c34; }"
        )

        # Assemble layout
        layout.addWidget(self.cell_label)
        layout.addWidget(self.voltage_bar)
        layout.addWidget(self.temp_bar)

    def update_data(self, temp: float, voltage: float):
        """
        Update the progress bars and their labels.
        """
        # Voltage
        v_pct = int((voltage - self.MIN_VOLT) / (self.MAX_VOLT - self.MIN_VOLT) * 100)
        v_pct = max(0, min(100, v_pct))
        self.voltage_bar.setValue(v_pct)
        self.voltage_bar.setFormat(f"{voltage:.3f} V")

        # Temperature
        t_pct = int((temp - self.MIN_TEMP) / (self.MAX_TEMP - self.MIN_TEMP) * 100)
        t_pct = max(0, min(100, t_pct))
        self.temp_bar.setValue(t_pct)
        self.temp_bar.setFormat(f"{temp:.1f} °C")
