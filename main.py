import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QTextEdit,
    QPushButton,
    QWidget,
    QLabel,
    QHBoxLayout,
)
from operands import parse_operands
from operators import parse_operator


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ruby Parser")
        self.setMinimumWidth(1000)
        self.setMinimumHeight(800)
        self.text_edit = QTextEdit()
        self.text_edit.resize(100, 10)

        ParseButton = QPushButton("Parse code")
        ParseButton.clicked.connect(self.parse_text)

        DeleteButton = QPushButton("Delete code")
        DeleteButton.clicked.connect(self.delete_text)

        self.operands_label = QLabel("Operands")
        self.operators_label = QLabel("Operators")

        container = QWidget()

        layout = QVBoxLayout()
        results_layout = QHBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(ParseButton)
        layout.addWidget(DeleteButton)
        layout.addWidget(container)

        container.setLayout(results_layout)

        results_layout.addWidget(self.operands_label)
        results_layout.addWidget(self.operators_label)

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

    def parse_text(self):
        text = self.text_edit.toPlainText()
        operands_result = parse_operands(text)
        operators_result = parse_operator(text)

        self.operands_label.clear()
        self.operators_label.clear()

        self.operands_label.setText("Operands\n")
        self.operators_label.setText("Operators\n")

        for item in operands_result.items():
            self.operands_label.setText(self.operands_label.text() + str(item) + "\n")

        for item in operators_result.items():
            self.operators_label.setText(self.operators_label.text() + str(item) + "\n")

    def delete_text(self):
        self.text_edit.clear()
        self.operands_label.clear()
        self.operands_label.setText("Operands\n")

        self.operators_label.clear()
        self.operators_label.setText("Operators\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
