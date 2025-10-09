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

def write_text(self, file_path, mode):
    text = self.text_editor.toPlainText()
    with open(file_path, mode, encoding='utf-8') as file:
        file.write(text)

def save_file(self):
    if self.is_something_was_opened:
        write_text(self, file_path=self.file_path,mode='w')
    else:
        title = self.text_title.text()
        try:
            if self.is_something_was_saved:
                write_text(self, file_path=self.text_title.text(), mode='w')
            if title != '' and self.is_something_was_saved == False:
                if title[-4:] != '.txt':
                    title = f'{title}.txt'
                write_text(self, file_path=self.text_title.text(), mode='x')
                self.is_something_was_saved = True
            if title == '' and self.is_something_was_saved == False:
                error_message(text='Пожалуйста, назовите Ваш текстовый документ')
        except FileExistsError:
            error_message(text='Файл с таким именем уже существует. Пожалуйста, переименуйте файл')

def save_file_as(self):
    file_name = QFileDialog.getSaveFileName(self, 'Сохранить файл', 
                                            self.text_title.text(), 
                                            'Текстовые файлы (*.txt)')[0]
    text = self.text_editor.toPlainText()
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(text)
    except FileNotFoundError:
        pass