from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog

class FileLoader(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Load logs from gates')
        layout = QVBoxLayout()

        self.header_label = QLabel('Load logs from gates', self)
        layout.addWidget(self.header_label)

        self.path_edit = QLineEdit(self)
        self.path_edit.setPlaceholderText('Enter the file path here or browse to select')
        layout.addWidget(self.path_edit)

        self.browse_button = QPushButton('Browse', self)
        self.browse_button.clicked.connect(self.browse_file)
        layout.addWidget(self.browse_button)

        self.load_button = QPushButton('Load', self)
        self.load_button.clicked.connect(self.load_file)
        layout.addWidget(self.load_button)

        self.setLayout(layout)

    def browse_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'Text Files (*.txt)')
        if file_name:
            self.path_edit.setText(file_name)

    def load_file(self):
        file_path = self.path_edit.text()
        print(f'Loading file from: {file_path}')