from PySide6.QtWidgets import QApplication
from controllers.suma_w import SumaWindow



if __name__ == '__main__':
    app = QApplication()
    window = SumaWindow()
    window.show()
    app.exec()

