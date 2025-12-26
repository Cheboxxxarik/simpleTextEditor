"""
main.py

Главный модуль текстового редактора.

Содержит класс TextEditor — основное окно приложения,
реализующее:
- ввод и редактирование текста;
- создание, открытие и сохранение текстовых файлов;
- работу с пользовательскими настройками и темами;
- интерфейс на основе PyQt6.

Запуск модуля инициирует создание и отображение главного окна приложения.
"""

from PyQt6 import QtWidgets
from PyQt6.QtGui import QIcon
from os.path import basename, splitext
from settings_gui import SettingsGUI
import config, config_stylesheet


class TextEditor(QtWidgets.QMainWindow):
    def __init__(self):
        super(TextEditor, self).__init__()
        self.setWindowTitle('simpleTextEditor')
        self.resize(800, 600)
        # Создание центрального виджета
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        # Добавление иконки приложения
        self.setWindowIcon(QIcon('simpleTextEditor.ico'))
        # Создание основного слоя
        self.main_layout = QtWidgets.QVBoxLayout(central_widget)
        self.main_layout.setSpacing(15)
        self.main_layout.setContentsMargins(20, 20, 20, 20) 
        # Создание слоя, на котором будут находиться виджеты для работы с текстом
        self.text_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addLayout(self.text_layout)
        # Поле для названия текста
        self.text_title = QtWidgets.QLineEdit(self)
        self.text_title.setPlaceholderText('Введите название файла.txt')
        self.text_title.setCursorPosition(0)
        self.text_title.setStyleSheet(config_stylesheet.LINE_EDITOR_STYLESHEET)
        self.text_title.setMinimumHeight(50)
        # Поле для ввода текста
        self.text_editor = QtWidgets.QTextEdit(self)
        self.text_editor.setPlaceholderText('Введите текст...')
        self.text_editor.setStyleSheet(config_stylesheet.TEXT_EDITOR_STYLESHEET)
        # Кнопка для сохранения текста
        self.save_button = QtWidgets.QPushButton(self)
        self.save_button.setText('Сохранить')
        self.save_button.setMaximumWidth(100)
        self.save_button.clicked.connect(self.save_file)
        self.save_button.setStyleSheet(config_stylesheet.BUTTON_STYLESHEET)
        # Добавление виджетов
        self.text_layout.addWidget(self.text_title)
        self.text_layout.addWidget(self.text_editor) 
        # Создание слоя для кнопок
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()  # Добавляем растягивающее пространство слева
        button_layout.addWidget(self.save_button)
        # Добавление слоя для кнопок
        self.text_layout.addLayout(button_layout)
        # Создание меню-бара
        self.menu_bar = QtWidgets.QMenuBar()
        self.menu_bar.setStyleSheet('')
        self.menu_bar.setStyleSheet(config_stylesheet.MENU_BAR_STYLESHEET)
        self.setMenuBar(self.menu_bar)
        # Создание меню-бара
        file_menu = QtWidgets.QMenu('&Файл', self)
        self.menu_bar.addMenu(file_menu)
        file_menu.addAction('Новый файл', self.new_file)
        file_menu.addAction('Открыть файл', self.open_file)
        file_menu.addAction('Сохранить', self.save_file)
        file_menu.addAction('Сохранить как', self.save_file_as)
        settings_menu = QtWidgets.QMenu('&Настройки', self)
        self.menu_bar.addMenu(settings_menu)
        settings_menu.addAction('Настройки', self.open_settings)

        self.is_something_was_opened = False
        self.is_something_was_saved = False

    # Уведомление об ошибке
    # Аргументы функции: text - текст ошибок
    @staticmethod
    def error_message(text):
        error = QtWidgets.QMessageBox()
        error.setWindowTitle('Ошибка')
        error.setText(text)
        error.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        error.setStyleSheet(config_stylesheet.MESSAGE_BOX_STYLESHEET)
        error.exec()

    # Функция для записи текста
    # Аргументы функции: filepath - путь к файлу, mode - режим записи текста
    def write_text(self, file_path, mode):
        text = self.text_editor.toPlainText()
        with open(file_path, mode, encoding='utf-8') as file:
            file.write(text)

    # Функция для создания нового файла
    def new_file(self):
        self.text_title.setCursorPosition(0)
        self.text_editor.setText('')
        self.is_something_was_opened = False
        self.is_something_was_saved = False
    
    # Функция для открытия файла
    def open_file(self):
        self.file_path = QtWidgets.QFileDialog.getOpenFileName(self, "Открыть файл",
                                                f"{config.DEFAULT_FOLDER}",
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

    # Функция для проверки названия файла на содержание запрещенных символов
    def check_banned_symbols(self):
        banned_symbols = set('@/*#!$%^?\\[]-_+=;`~,<>\'"|')
        if set(self.text_title.text()) & banned_symbols:
            self.error_message('В названии содержатся запрещённые символы')

    # Функция для сохранения файла
    def save_file(self):
        self.check_banned_symbols()
        if self.is_something_was_opened:
            self.write_text(file_path=self.file_path,mode='w')
        else:
            title = self.text_title.text()
            if splitext(title)[1] != '.txt':
                title = f'{title}.txt'
            try:
                if self.is_something_was_saved:
                    self.write_text(file_path=f'{config.DEFAULT_FOLDER}/{title}',
                                    mode='w')
                else:
                    if title != '':
                        self.write_text(file_path=f'{config.DEFAULT_FOLDER}/{title}',
                                        mode='x')
                        self.is_something_was_saved = True
                        self.text_title.setReadOnly(True)
                    else:
                        self.error_message('Пожалуйста, назовите Ваш текстовый документ')
            except FileExistsError:
                self.error_message('Файл с таким именем уже существует. Пожалуйста, переименуйте файл')

    # Функция для сохранения файлов, в директории, выбранной пользователем
    def save_file_as(self):
        self.file_path = QtWidgets.QFileDialog.getSaveFileName(self, 'Сохранить файл', 
                                                f'{config.DEFAULT_FOLDER}/{self.text_title.text()}',
                                                'Текстовые файлы (*.txt)')[0]
        try:
            self.write_text(file_path=self.file_path, mode='w')
            self.is_something_was_opened = True
            self.is_something_was_saved = True
        except FileNotFoundError:
            pass

    # Функция для применения новых настроек
    def apply_settings(self):
        import importlib
        import config
        import config_stylesheet

        # Перезагружаем модули
        importlib.reload(config)
        importlib.reload(config_stylesheet)

        # Применяем стили заново
        app = QtWidgets.QApplication.instance()
        config_stylesheet.theme_applier(app)

        self.text_title.setStyleSheet(config_stylesheet.LINE_EDITOR_STYLESHEET)
        self.text_editor.setStyleSheet(config_stylesheet.TEXT_EDITOR_STYLESHEET)
        self.save_button.setStyleSheet(config_stylesheet.BUTTON_STYLESHEET)
        self.menu_bar.setStyleSheet(config_stylesheet.MENU_BAR_STYLESHEET)
        app.setStyleSheet(config_stylesheet.MENU_BAR_STYLESHEET)

    # Функция для открытия окна настроек
    def open_settings(self):
        settings_window = SettingsGUI()
        settings_window.settings_applied.connect(self.apply_settings)
        settings_window.exec()


# Запуск приложения
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion') 
    app.setStyleSheet(config_stylesheet.MENU_BAR_STYLESHEET)
    config_stylesheet.theme_applier(app)
    window = TextEditor()
    window.show()
    sys.exit(app.exec())