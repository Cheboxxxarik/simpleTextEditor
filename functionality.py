from PyQt6.QtWidgets import QMessageBox, QFileDialog
from os.path import basename
import config
    
def open_file(self):
    self.file_path = QFileDialog.getOpenFileName(self, "Открыть файл", 
                                            f"{config.default_folder}",
                                            "Текстовые документы(*.txt)")[0]
    try:
        if self.file_path != '':
            with open(self.file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                self.text_editor.setText(text)
            self.file_name = basename(self.file_path)
            self.text_title.setText(self.file_name)
            self.text_title.setReadOnly(True)
            self.is_something_was_opened = True
    except FileNotFoundError:
        pass

def save_file(self):
    if self.is_something_was_opened:
        text = self.text_editor.toPlainText()
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.write(text)
    else:
        title = self.text_title.text()
        if title != '':
            if title[-4:-1] != '.txt':
                title = f'{title}.txt'
            text = self.text_editor.toPlainText()
            with open(title, 'x', encoding='utf-8') as file:
                file.write(text)
        else:
            error = QMessageBox()
            error.setWindowTitle('Ошибка')
            error.setText('Пожалуйста, назовите Ваш текстовый документ')
            error.setIcon(QMessageBox.Warning)
            error.exec()

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