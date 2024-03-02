
# #print('и операторы и операнды будем делать в своих файликах что бы не было конфликтов и отдельно кути добавим')
#
# code = None
#
# with open("Example.rb", "r") as file:
#     code = file.read()
#
# #parse_operator(code)
# for item in parse_operands(code).items():
#     print(item)
#
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QHBoxLayout
from operands import parse_operands
from operators import parse_operator

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("LR1(Dovnar & Beckman)")
        self.setMinimumWidth(1600)
        self.setMinimumHeight(1200)
        self.text_edit = QTextEdit()
        self.text_edit.resize(100, 10)


        ParseButton = QPushButton("Parse code")
        ParseButton.clicked.connect(self.parse_text)

        DeleteButton = QPushButton("Delete code")
        DeleteButton.clicked.connect(self.delete_text)

        # для вывода результатов
        self.operands_label = QLabel()
        self.operators_label = QLabel()

        self.operands_label.setText("operands")
        self.operators_label.setText('operators')

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
        #layout.addWidget(self.operands_label)

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

    def parse_text(self):
        text = self.text_edit.toPlainText()
        operands_result = parse_operands(text)
        for item in operands_result.items():
            self.operands_label.setText(self.operands_label.text() + str(item) + "\n")



    def delete_text(self):
        self.text_edit.clear()
        self.operands_label.clear()
        self.operators_label.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())