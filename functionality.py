from PyQt5 import QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from settings_gui import SettingsGUI
import config

@QtCore.pyqtSlot()
def open_file(Window):
    file_name = QFileDialog.getOpenFileName(Window, "Открыть файл", f"{config.default_folder}",
                                            "Текстовые документы(*.txt)")[0]
    try:
        if file_name != '':
            Window.text_title.setText(file_name)
        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.read()
        Window.text_editor.setText(text)
    except FileNotFoundError:
        pass

@QtCore.pyqtSlot()
def save_file(Window):
    try:
        title = Window.text_title.text()
        if title != '':
            text = Window.text_editor.toPlainText()
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
        file_name = Window.text_title.text()
        text = Window.text_editor.toPlainText()
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(text)


@QtCore.pyqtSlot()
def save_file_as(Window):
    file_name = QFileDialog.getSaveFileName(Window, 'Сохранить файл', f'{config.default_folder}/{Window.text_title.text()}', 'Текстовые файлы (*.txt)')[0]
    text = Window.text_editor.toPlainText()

    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(text)
    except FileNotFoundError:
        pass

def settings():
    settings_window = SettingsGUI()
    settings_window.exec_()