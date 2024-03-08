import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QLineEdit, QWidget, QMessageBox, QFileDialog

class FileResizer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('File Resizer')
        self.setGeometry(200, 200, 400, 200)

        layout = QVBoxLayout()

        self.label = QLabel('Dosya Yolu:')
        layout.addWidget(self.label)

        self.file_path_input = QLineEdit()
        layout.addWidget(self.file_path_input)

        self.browse_button = QPushButton('Dosya Seç')
        self.browse_button.clicked.connect(self.browse_file)
        layout.addWidget(self.browse_button)

        self.max_size_label = QLabel('Dosyanın büyütüleceği Boyut (MB) not:boyutu büyütülen dosyanın çalışması bozulabilir.:')
        layout.addWidget(self.max_size_label)

        self.max_size_input = QLineEdit()
        layout.addWidget(self.max_size_input)

        self.resize_button = QPushButton('Boyutlandır')
        self.resize_button.clicked.connect(self.resize_file)
        layout.addWidget(self.resize_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Dosya Seç', '', 'Tüm Dosyalar (*)')
        self.file_path_input.setText(file_path)

    def resize_file(self):
        file_path = self.file_path_input.text()
        max_size_mb = float(self.max_size_input.text())

        try:
            current_size_mb = os.path.getsize(file_path) / (1024 * 1024)
            while current_size_mb < max_size_mb:
                with open(file_path, 'ab') as file:
                    file.write(b'\0' * 1024 * 1024)
                current_size_mb = os.path.getsize(file_path) / (1024 * 1024)
            QMessageBox.information(self, 'Başarılı', 'Dosya başarıyla boyutlandırıldı!')
        except Exception as e:
            QMessageBox.warning(self, 'Hata', f'Hata oluştu: {str(e)}')

def main():
    app = QApplication(sys.argv)
    window = FileResizer()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
