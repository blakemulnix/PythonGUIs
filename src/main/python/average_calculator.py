import sys
from decimal import Decimal

from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QGridLayout
from fbs_runtime.application_context.PyQt5 import ApplicationContext

from arithmetic import calculate_average

# Create QT Application and Widget
appctxt = ApplicationContext()
window = QWidget()

# Set the geometry of the Widget
window.setGeometry(300, 300, 300, 100)
window.setWindowTitle('Average Calculator')

# Create inputs and output
input_a_line_edit = QLineEdit()
input_b_line_edit = QLineEdit()
output_line_edit = QLineEdit()
calculate_button = QPushButton('Calculate')


# Create calculate function and tie it to button
def calc_average_of_input_a_and_input_b_and_display_output():
    average_dec = calculate_average(Decimal(input_a_line_edit.text()), Decimal(input_b_line_edit.text()))
    output_line_edit.setText(str(average_dec))


calculate_button.clicked.connect(calc_average_of_input_a_and_input_b_and_display_output)

# Create grid layout and elements
layout = QGridLayout()
layout.addWidget(QLabel('Input A'), 0, 0, 1, 2)
layout.addWidget(QLabel('Input B'), 1, 0, 1, 2)
layout.addWidget(QLabel('Output:'), 2, 0, 1, 2)
layout.addWidget(input_a_line_edit, 0, 2, 1, 2)
layout.addWidget(input_b_line_edit, 1, 2, 1, 2)
layout.addWidget(output_line_edit, 2, 2, 1, 2)
layout.addWidget(calculate_button, 3, 1, 1, 2)

# Set the layout of the window to the one we created and show the window
window.setLayout(layout)
window.show()

# Execute the app
if __name__ == '__main__':
    exit_code = appctxt.app.exec_()
    sys.exit(exit_code)
