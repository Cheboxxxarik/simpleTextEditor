from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu
import config, functionality


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('simpleTextEditor')
        self.setGeometry(0, 0, 800, 600)
        # Обои
        self.wallpaper = QtWidgets.QLabel(self)
        self.wallpaper.setGeometry(0, 0, 800, 600)
        self.wallpaper.setText('')
        self.wallpaper.setPixmap(QtGui.QPixmap(config.default_wallpaper))

        # Поле для названия текста
        self.text_title = QtWidgets.QLineEdit(self)
        self.text_title.setGeometry(10, 30, 780, 51)
        self.text_title.setAutoFillBackground(False)
        self.text_title.setText('.txt')
        self.text_title.setCursorPosition(0)
        self.text_title.setStyleSheet(f"font: {config.default_label_font_size} \"{config.default_font}\";\n"
                                        f"background-color: {config.default_background_color};\n"
                                        "border: None")
        # Поле для ввода текста
        self.text_editor = QtWidgets.QTextEdit(self)
        self.text_editor.setGeometry(10, 90, 780, 461)
        self.text_editor.setAutoFillBackground(False)
        self.text_editor.setStyleSheet(f"font: {config.default_font_size} \"{config.default_font}\";\n"
                                        f"background-color: {config.default_background_color};\n"
                                        "border: None")
        # Кнопка для сохранения текста
        self.save_button = QtWidgets.QPushButton(self)
        self.save_button.setGeometry(QtCore.QRect(690, 560, 91, 28))
        self.save_button.setText('Сохранить')
        self.save_button.clicked.connect(functionality.save_file)
        # Создание меню-бара
        self.create_menu_bar()

    def create_menu_bar(self):
        self.menu_bar = QMenuBar()
        self.setMenuBar(self.menu_bar)

        file_menu = QMenu('&Файл', self)
        self.menu_bar.addMenu(file_menu)
        file_menu.addAction('Открыть', self.action_clicked)
        file_menu.addAction('Сохранить', self.action_clicked)
        file_menu.addAction('Сохранить как', self.action_clicked)

        settings_menu = QMenu('&Настройки', self)
        self.menu_bar.addMenu(settings_menu)
        settings_menu.addAction('Настройки', self.action_clicked)

    def action_clicked(self):
        action = self.sender().text()
        if action == 'Открыть':
            functionality.open_file(self)
        elif action == 'Сохранить':
            functionality.save_file(self)
        elif action == 'Сохранить как':
            functionality.save_file_as(self)
        elif action == 'Настройки':
            functionality.settings()
        else:
            pass


# Запуск приложения
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())