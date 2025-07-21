from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QMessageBox, QFileDialog
from settings_gui import SettingsGUI
import config


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
        self.text_title.setGeometry(10, 30, 780, 71)
        self.text_title.setAutoFillBackground(False)
        self.text_title.setText('.txt')
        self.text_title.setCursorPosition(0)
        self.text_title.setStyleSheet(f"font: {config.default_label_font_size} \"{config.default_font}\";\n"
                                        f"background-color: {config.default_background_color};\n"
                                        "border: None")
        # Поле для ввода текста
        self.text_editor = QtWidgets.QTextEdit(self)
        self.text_editor.setGeometry(10, 110, 780, 441)
        self.text_editor.setAutoFillBackground(False)
        self.text_editor.setStyleSheet(f"font: {config.default_font_size} \"{config.default_font}\";\n"
                                        f"background-color: {config.default_background_color};\n"
                                        "border: None")
        # Кнопка для сохранения текста
        self.save_button = QtWidgets.QPushButton(self)
        self.save_button.setGeometry(QtCore.QRect(690, 560, 91, 28))
        self.save_button.setText('Сохранить')
        self.save_button.clicked.connect(self.action_clicked)
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
            file_name = QFileDialog.getOpenFileName(self, "Открыть файл", f"{config.default_folder}",
                                            "Текстовые документы(*.txt)")[0]
            try:
                if file_name != '':
                    self.text_title.setText(file_name)
                    with open(file_name, 'r', encoding='utf-8') as file:
                        text = file.read()
                        self.text_editor.setText(text)
            except FileNotFoundError:
                pass
        elif action == 'Сохранить':
            title = self.text_title.text()
            try:
                if title != '':
                    text = self.text_editor.toPlainText()
                    file_name = f'{config.default_folder}/{title}'
                    with open(file_name, 'x', encoding='utf-8') as file:
                        file.write(text)
                else:
                    error = QMessageBox()
                    error.setWindowTitle('Ошибка')
                    error.setText('Пожалуйста, назовите Ваш текстовый документ')
                    error.setIcon(QMessageBox.Warning)
                    error.exec_()
            except FileExistsError:
                file_name = self.text_title.text()
                text = self.text_editor.toPlainText()
                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write(text)
        elif action == 'Сохранить как':
            file_name = QFileDialog.getSaveFileName(self, 'Сохранить файл', f'{config.default_folder}/{self.text_title.text()}', 'Текстовые файлы (*.txt)')[0]
            text = self.text_editor.toPlainText()

            try:
                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write(text)
            except FileNotFoundError:
                pass
        elif action == 'Настройки':
            settings_window = SettingsGUI()
            settings_window.exec_()
        else:
            pass


# Запуск приложения
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())