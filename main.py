import sys
from PySide6 import QtWidgets
from GUI import MyWidget

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())