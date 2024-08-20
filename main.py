# Pastikan nama ini sesuai dengan nama file Python yang dihasilkan
from PyQt6.QtWidgets import QApplication
from connections import MainWindow
import sys
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
