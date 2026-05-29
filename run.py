from gui import QApplication, QFont, MainWindow, sys



if __name__ == "__main__":
    app = QApplication(sys.argv)

    font = QFont("Segoe UI")
    app.setFont(font)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())