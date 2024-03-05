import sys
import math
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
        self.operands_count_label = QLabel()
        self.operators_count_label = QLabel()

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
        results_layout.addWidget(self.operands_count_label)
        results_layout.addWidget(self.operators_count_label)

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

    def parse_text(self):
        text = self.text_edit.toPlainText()
        operands_result,operands_count = parse_operands(text)
        operators_result,operators_count = parse_operator(text)

        self.operands_label.clear()
        self.operators_label.clear()

        self.operands_label.setText("Operands\n")
        self.operators_label.setText("Operators\n")
 
       
        
        dict_operands = len(operands_result)
        dict_operators = len(operators_result)

        self.operands_count_label.setText(f"Operands count: {operands_count}\n\n"
                                          f"Operands dict:{dict_operands}\n\n"
                                          f"The dictionary of the program:{dict_operands+dict_operators}\n\n"
                                          f"Length:{operands_count+operators_count}")
        self.operators_count_label.setText(f"Operators count: {operators_count}\n\n"
                                           f"Operators dict:{dict_operators}\n\n"
                                           f"Volume:{int(operands_count+operators_count)*math.log2(dict_operators+dict_operands)}")

        for item in operands_result.items():
            self.operands_label.setText(self.operands_label.text() + str(item) + "\n")

        for item in operators_result.items():
            self.operators_label.setText(self.operators_label.text() + str(item) + "\n")

    def delete_text(self):
        self.text_edit.clear()
        self.operands_label.clear()
        self.operands_label.setText("Operands count:\n")

        self.operators_label.clear()
        self.operators_label.setText("Operators count:\n")
        self.operands_count_label.clear()
        self.operators_count_label.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
