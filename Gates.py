from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget
import sys
from process.loader import FileLoader

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Moja Aplikacja PyQt")
        self.setGeometry(100, 100, 800, 600)
        self.init_tabs()

    def init_tabs(self):
        # Inicjalizacja QTabWidget
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Dodanie głównego widoku jako pierwszej zakładki
        self.main_view = QWidget()
        self.tabs.addTab(self.main_view, "Main")

        # Dodanie loader_view jako drugiej zakładki
        self.loader_view = FileLoader()
        self.tabs.addTab(self.loader_view, "Loader")

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()