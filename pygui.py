import sys
import os
import requests
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("JSONPlaceholder Downloader")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.info_label = QLabel("Press the button to download data from JSONPlaceholder.")
        layout.addWidget(self.info_label)

        self.download_button = QPushButton("Download Data")
        self.download_button.clicked.connect(self.download_data)
        layout.addWidget(self.download_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def download_data(self):
        try:
            response = requests.get("https://jsonplaceholder.typicode.com/posts")
            if response.status_code == 200:
                data = response.json()
                self.save_data(data)
                QMessageBox.information(self, "Success", "Data downloaded and saved successfully.")
            else:
                QMessageBox.warning(self, "Error", f"Failed to download data. Status code: {response.status_code}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    def save_data(self, data):
        directory = "json_data"
        if not os.path.exists(directory):
            os.makedirs(directory)

        file_path = os.path.join(directory, "posts.json")
        with open(file_path, "w") as f:
            f.write(str(data))


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
