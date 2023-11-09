from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QTextEdit, QLabel
import sys
from pages.loader import FileLoader

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gates Manager")
        self.setGeometry(100, 100, 800, 600)
        self.init_ui()

    def init_ui(self):
        
        main_layout = QVBoxLayout()

        # Inicialization of tabs
        self.tabs = QTabWidget()
        main_layout.addWidget(self.tabs)

        # Add main view as a start window
        self.main_view = QWidget()
        self.tabs.addTab(self.main_view, "Main")

        # Add Loader tab
        self.loader_view = FileLoader(self.update_console)  
        self.tabs.addTab(self.loader_view, "Loader")

        # Add message log
        self.console_label = QLabel("Message log:")
        main_layout.addWidget(self.console_label)

        self.console = QTextEdit()
        self.console.setReadOnly(True)
        self.console.setFixedHeight(100)
        main_layout.addWidget(self.console)

        # Set main widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def update_console(self, message):
        # Update console to all tabs
        self.console.append(message)

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()