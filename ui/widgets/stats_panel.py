# ui/widgets/stats_panel.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QGridLayout,
    QPushButton, QGroupBox, QSizePolicy
)
from PyQt6.QtCore import Qt


class StatsPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Main vertical layout: equal stretch for each group
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(8, 8, 8, 8)
        main_layout.setSpacing(10)

        # --- Time Section ---
        time_group = QGroupBox("Time")
        time_group.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        time_layout = QGridLayout()
        time_layout.setContentsMargins(6, 4, 6, 4)
        time_layout.setHorizontalSpacing(8)
        time_layout.setVerticalSpacing(4)
        time_group.setLayout(time_layout)

        self.current_time_label = QLabel("---")
        self.run_time_label     = QLabel("---")
        time_layout.addWidget(QLabel("Current time:"), 0, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        time_layout.addWidget(self.current_time_label, 0, 1, alignment=Qt.AlignmentFlag.AlignRight)
        time_layout.addWidget(QLabel("Run time:"),    1, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        time_layout.addWidget(self.run_time_label,    1, 1, alignment=Qt.AlignmentFlag.AlignRight)

        # --- Motor Controller Section ---
        motor_group = QGroupBox("Motor Controller")
        motor_group.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        motor_layout = QGridLayout()
        motor_layout.setContentsMargins(6, 4, 6, 4)
        motor_layout.setHorizontalSpacing(8)
        motor_layout.setVerticalSpacing(4)
        motor_group.setLayout(motor_layout)

        motor_layout.addWidget(QLabel("Speed:"),       0, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        self.speed_value = QLabel("---")
        motor_layout.addWidget(self.speed_value,        0, 1, alignment=Qt.AlignmentFlag.AlignRight)
        motor_layout.addWidget(QLabel("mph"),           0, 2, alignment=Qt.AlignmentFlag.AlignLeft)

        motor_layout.addWidget(QLabel("Current:"),     1, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        self.current_value = QLabel("---")
        motor_layout.addWidget(self.current_value,      1, 1, alignment=Qt.AlignmentFlag.AlignRight)
        motor_layout.addWidget(QLabel("A"),             1, 2, alignment=Qt.AlignmentFlag.AlignLeft)

        motor_layout.addWidget(QLabel("Energy:"),      2, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        self.energy_value = QLabel("---")
        motor_layout.addWidget(self.energy_value,       2, 1, alignment=Qt.AlignmentFlag.AlignRight)
        motor_layout.addWidget(QLabel("Ah"),            2, 2, alignment=Qt.AlignmentFlag.AlignLeft)
        self.energy_reset_btn = QPushButton("Reset")
        motor_layout.addWidget(self.energy_reset_btn,   2, 3)

        motor_layout.addWidget(QLabel("Av. Speed:"),   3, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        self.av_speed_value = QLabel("---")
        motor_layout.addWidget(self.av_speed_value,     3, 1, alignment=Qt.AlignmentFlag.AlignRight)
        motor_layout.addWidget(QLabel("mph"),           3, 2, alignment=Qt.AlignmentFlag.AlignLeft)
        self.av_speed_reset_btn = QPushButton("Reset")
        motor_layout.addWidget(self.av_speed_reset_btn, 3, 3)

        # --- MPPTs Section ---
        mppt_group = QGroupBox("MPPTs")
        mppt_group.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        mppt_layout = QGridLayout()
        mppt_layout.setContentsMargins(6, 4, 6, 4)
        mppt_layout.setHorizontalSpacing(8)
        mppt_layout.setVerticalSpacing(4)
        mppt_group.setLayout(mppt_layout)

        mppt_layout.addWidget(QLabel("#"),             0, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        mppt_layout.addWidget(QLabel("Out Current"),   0, 1, alignment=Qt.AlignmentFlag.AlignLeft)
        self.mppt_current_labels = []
        for i in range(4):
            idx_label = QLabel(str(i))
            curr_label = QLabel("---")
            amp_label = QLabel("A")
            mppt_layout.addWidget(idx_label,    i+1, 0)
            mppt_layout.addWidget(curr_label,   i+1, 1)
            mppt_layout.addWidget(amp_label,    i+1, 2)
            self.mppt_current_labels.append(curr_label)
        total_label = QLabel("Total")
        total_current_label = QLabel("---")
        total_amp_label = QLabel("A")
        mppt_layout.addWidget(total_label,        5, 0)
        mppt_layout.addWidget(total_current_label,5, 1)
        mppt_layout.addWidget(total_amp_label,    5, 2)
        self.mppt_total_label = total_current_label

        # --- Battery Section (Single) ---
        batt_group = QGroupBox("Battery")
        batt_group.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        batt_layout = QGridLayout()
        batt_layout.setContentsMargins(6, 4, 6, 4)
        batt_layout.setHorizontalSpacing(8)
        batt_layout.setVerticalSpacing(4)
        batt_group.setLayout(batt_layout)

        labels = ["Average:", "High:", "Low:", "Current:"]
        self.battery_values = []
        for i, text in enumerate(labels):
            batt_layout.addWidget(QLabel(text), i, 0, alignment=Qt.AlignmentFlag.AlignLeft)
            val_label = QLabel("---")
            batt_layout.addWidget(val_label, i, 1, alignment=Qt.AlignmentFlag.AlignRight)
            self.battery_values.append(val_label)

        # Add sections equally
        main_layout.addWidget(time_group,  1)
        main_layout.addWidget(motor_group, 1)
        main_layout.addWidget(mppt_group,  1)
        main_layout.addWidget(batt_group,  1)

    def update_stats(self, data: dict):
        # Time
        self.current_time_label.setText(data.get("current_time", "---"))
        self.run_time_label.setText(data.get("run_time",     "---"))

        # Motor Controller
        self.speed_value.setText(f"{data.get('speed', '---')}")
        self.current_value.setText(f"{data.get('current', '---')}")
        self.energy_value.setText(f"{data.get('energy', '---')}")
        self.av_speed_value.setText(f"{data.get('av_speed', '---')}")

        # MPPTs
        for lbl, val in zip(self.mppt_current_labels, data.get("mppt_currents", [])):
            lbl.setText(str(val))
        self.mppt_total_label.setText(str(data.get("mppt_total", '---')))

        # Single Battery summary
        batt = data.get("batman", {}) or {}
        for lbl, key in zip(self.battery_values, ["average", "high", "low", "current"]):
            lbl.setText(str(batt.get(key, "---")))
