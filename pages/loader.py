from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit

class FileLoader(QWidget):
    def __init__(self, update_console_callback, parent=None):
        super().__init__(parent)
        self.update_console = update_console_callback
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Load logs from gates')
        layout = QVBoxLayout()

        self.header_label_logs = QLabel('Load logs from gates', self)
        layout.addWidget(self.header_label_logs)

        self.path_edit_logs = QLineEdit(self)
        self.path_edit_logs.setPlaceholderText('Enter the file path here or browse to select')
        layout.addWidget(self.path_edit_logs)

        self.browse_button_logs = QPushButton('Browse', self)
        self.browse_button_logs.clicked.connect(self.browse_file_logs)
        layout.addWidget(self.browse_button_logs)

        self.load_button_logs = QPushButton('Load', self)
        self.load_button_logs.clicked.connect(self.load_file_logs)
        layout.addWidget(self.load_button_logs)

        self.header_label_threads = QLabel('Load cars marked as threat', self)
        layout.addWidget(self.header_label_threads)

        self.path_edit_threads = QLineEdit(self)
        self.path_edit_threads.setPlaceholderText('Enter the file path here or browse to select')
        layout.addWidget(self.path_edit_threads)

        self.browse_button_threads = QPushButton('Browse', self)
        self.browse_button_threads.clicked.connect(self.browse_file_threads)
        layout.addWidget(self.browse_button_threads)

        self.load_button_threads = QPushButton('Load', self)
        self.load_button_threads.clicked.connect(self.load_file_threads)
        layout.addWidget(self.load_button_threads)

        self.header_label_database = QLabel('Load data from data from database', self)
        layout.addWidget(self.header_label_database)

        self.database_button = QPushButton('Load from Database', self)
        self.database_button.clicked.connect(self.load_database)
        layout.addWidget(self.database_button)

        self.setLayout(layout)

    def browse_file_logs(self):
        file_namee_logs, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'Text Files (*.txt)')
        if file_namee_logs:
            self.path_edit.setText(file_namee_logs)

    def load_file_logs(self):
        file_path_logs = self.path_edit.text()
        print(f'Loading file from: {file_path_logs}')
        self.update_console("Data loaded successfully.")

    def browse_file_threads(self):
        file_name_threads, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'Text Files (*.txt)')
        if file_name_threads:
            self.path_edit.setText(file_name_threads)

    def load_file_threads(self):
        file_path_threads = self.path_edit.text()
        print(f'Loading file from: {file_path_threads}')
        self.update_console("Data loaded successfully.")

    def load_database(self):
        print(f'Loading file from database')
        self.update_console("Data loaded successfully.")

def main():
    app = QApplication([])
    ex = FileLoader()
    ex.show()
    app.exec()

if __name__ == '__main__':
    main()