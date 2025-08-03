# ui/widgets/plot_display.py

from PyQt6.QtWidgets import QGroupBox, QVBoxLayout
from pyqtgraph import PlotWidget

class PlotDisplay(QGroupBox):
    def __init__(self, title="Live Plot"):
        super().__init__(title)
        self.init_ui()
        self.data = []
        self.max_points = 100

    def init_ui(self):
        layout = QVBoxLayout()
        self.plot_widget = PlotWidget()
        self.plot_widget.setBackground('w')
        self.plot = self.plot_widget.plot(pen='b')

        layout.addWidget(self.plot_widget)
        self.setLayout(layout)

    def add_data_point(self, value: float):
        if len(self.data) >= self.max_points:
            self.data.pop(0)
        self.data.append(value)
        self.plot.setData(list(range(len(self.data))), self.data)
