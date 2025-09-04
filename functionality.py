from PyQt6.QtWidgets import QMessageBox, QFileDialog
from settings_gui import SettingsGUI
import config
    
def open_file(self):
    file_name = QFileDialog.getOpenFileName(self, "Открыть файл", 
                                            f"{config.default_folder}",
                                            "Текстовые документы(*.txt)")[0]
    try:
        if file_name != '':
            self.text_title.setText(file_name)
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read()
                self.text_editor.setText(text)
    except FileNotFoundError:
        pass

def save_file(self):
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
            error.exec()
    except FileExistsError and OSError:
        file_name = self.text_title.text()
        text = self.text_editor.toPlainText()
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(text)

def save_file_as(self):
    file_name = QFileDialog.getSaveFileName(self, 'Сохранить файл', 
                                            f'{config.default_folder}/{self.text_title.text()}', 
                                            'Текстовые файлы (*.txt)')[0]
    text = self.text_editor.toPlainText()
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(text)
    except FileNotFoundError:
        pass

def open_settings():
    settings_window = SettingsGUI()
    settings_window.exec()