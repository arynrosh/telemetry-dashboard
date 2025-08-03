# ui/widgets/motor_controller.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QGroupBox, QGridLayout
from PyQt6.QtCore import Qt

class MotorController(QGroupBox):
    def __init__(self):
        super().__init__("Motor Controller")

        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()

        # Labels
        self.speed_label = QLabel("Speed (km/h):")
        self.speed_value = QLabel("0.0")

        self.current_label = QLabel("Current (A):")
        self.current_value = QLabel("0.0")

        self.energy_label = QLabel("Energy (kWh):")
        self.energy_value = QLabel("0.0")

        # Add to grid: label on left, value on right
        layout.addWidget(self.speed_label, 0, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.speed_value, 0, 1, alignment=Qt.AlignmentFlag.AlignRight)

        layout.addWidget(self.current_label, 1, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.current_value, 1, 1, alignment=Qt.AlignmentFlag.AlignRight)

        layout.addWidget(self.energy_label, 2, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.energy_value, 2, 1, alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout(layout)

    # Placeholder method to update values
    def update_data(self, speed: float, current: float, energy: float):
        self.speed_value.setText(f"{speed:.1f}")
        self.current_value.setText(f"{current:.2f}")
        self.energy_value.setText(f"{energy:.3f}")
# ui/widgets/motor_controller.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QGroupBox, QGridLayout
from PyQt6.QtCore import Qt

class MotorController(QGroupBox):
    def __init__(self):
        super().__init__("Motor Controller")

        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()

        # Labels
        self.speed_label = QLabel("Speed (km/h):")
        self.speed_value = QLabel("0.0")

        self.current_label = QLabel("Current (A):")
        self.current_value = QLabel("0.0")

        self.energy_label = QLabel("Energy (kWh):")
        self.energy_value = QLabel("0.0")

        # Add to grid: label on left, value on right
        layout.addWidget(self.speed_label, 0, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.speed_value, 0, 1, alignment=Qt.AlignmentFlag.AlignRight)

        layout.addWidget(self.current_label, 1, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.current_value, 1, 1, alignment=Qt.AlignmentFlag.AlignRight)

        layout.addWidget(self.energy_label, 2, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.energy_value, 2, 1, alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout(layout)

    # Placeholder method to update values
    def update_data(self, speed: float, current: float, energy: float):
        self.speed_value.setText(f"{speed:.1f}")
        self.current_value.setText(f"{current:.2f}")
        self.energy_value.setText(f"{energy:.3f}")
