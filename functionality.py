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

def error_message(text):
    error = QMessageBox()
    error.setWindowTitle('Ошибка')
    error.setText(text)
    error.setIcon(QMessageBox.Icon.Warning)
    error.exec()

def save_file(self):
    if self.is_something_was_opened:
        text = self.text_editor.toPlainText()
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.write(text)
    else:
        title = self.text_title.text()
        try:
            if title != '':
                if title[-4:] != '.txt':
                    title = f'{title}.txt'
                text = self.text_editor.toPlainText()
                with open(f'{config.default_folder}/{title}', 'x', encoding='utf-8') as file:
                    file.write(text)
            else:
                error_message(text='Пожалуйста, назовите Ваш текстовый документ')
        except FileExistsError:
            error_message(text='Файл с таким именем уже существует. Пожалуйста, переименуйте файл')

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