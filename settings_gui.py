from PyQt6 import QtWidgets
from PyQt6.QtWidgets import (QDialog, QFileDialog, QVBoxLayout, 
                             QHBoxLayout, QGridLayout, QMessageBox)
from PyQt6.QtGui import QIcon
import config, config_stylesheet


class SettingsGUI(QDialog):
    def __init__(self):
        super(SettingsGUI, self).__init__()
        self.setWindowTitle('Настройки')
        # Добавление иконки приложения
        self.setWindowIcon(QIcon('simpleTextEditor.ico'))
        self.main_layout = QVBoxLayout(self)
        self.grid_layout = QGridLayout()
        self.main_layout.addLayout(self.grid_layout)
        # Выбор семейства шрифтов
        self.font_family_settings = QtWidgets.QLabel(self)
        self.font_family_settings.setText('Шрифт:')
        self.font_family_settings.setStyleSheet(config_stylesheet.LABEL_STYLESHEET)
        self.select_font_family = QtWidgets.QLineEdit(self)
        self.select_font_family.setText(config.FONT_FAMILY)
        self.select_font_family.setStyleSheet(config_stylesheet.SETTINGS_LINE_EDITOR_STYLESHEET)
        # Выбор размера шрифта
        self.font_size_settings = QtWidgets.QLabel(self)
        self.font_size_settings.setText('Размер шрифта обычного текста:')
        self.font_size_settings.setStyleSheet(config_stylesheet.LABEL_STYLESHEET)
        self.set_font_size = QtWidgets.QLineEdit(self)
        self.set_font_size.setText(config.FONT_SIZE)
        self.set_font_size.setStyleSheet(config_stylesheet.SETTINGS_LINE_EDITOR_STYLESHEET)
        # Выбор размера шрифта заголовка
        self.label_font_size_settings = QtWidgets.QLabel(self)
        self.label_font_size_settings.setText('Размер шрифта заголовка:')
        self.label_font_size_settings.setStyleSheet(config_stylesheet.LABEL_STYLESHEET)
        self.set_label_font_size = QtWidgets.QLineEdit(self)
        self.set_label_font_size.setText(config.LABEL_FONT_SIZE)
        self.set_label_font_size.setStyleSheet(config_stylesheet.SETTINGS_LINE_EDITOR_STYLESHEET)
        # Выбор фонового цвета
        self.background_color_settings = QtWidgets.QLabel(self)
        self.background_color_settings.setText('Фоновый цвет текстовых полей (rgba):')
        self.background_color_settings.setStyleSheet(config_stylesheet.LABEL_STYLESHEET)
        self.set_background_color = QtWidgets.QLineEdit(self)
        self.set_background_color.setText(config.BACKGROUND_COLOR_RGBA_CODE)
        self.set_background_color.setStyleSheet(config_stylesheet.SETTINGS_LINE_EDITOR_STYLESHEET)
        # Папка для сохранения текстовых документов по умолчанию
        self.default_folder_settings = QtWidgets.QLabel(self)
        self.default_folder_settings.setText('Папка по умолчанию:')
        self.default_folder_settings.setStyleSheet(config_stylesheet.LABEL_STYLESHEET)
        self.default_directory = QtWidgets.QLineEdit(self)
        self.default_directory.setText(config.DEFAULT_FOLDER)
        self.default_directory.setStyleSheet(config_stylesheet.SETTINGS_LINE_EDITOR_STYLESHEET)
        self.select_default_folder = QtWidgets.QPushButton(self)
        self.select_default_folder.setText('Выбрать')
        self.select_default_folder.clicked.connect(self.select_folder)
        self.select_default_folder.setStyleSheet(config_stylesheet.BUTTON_STYLESHEET)
        # Настройки акцентного цвета
        self.accent_colour = QtWidgets.QLabel(self)
        self.accent_colour.setText('Акцентный цвет (RGB):')
        self.accent_colour.setStyleSheet(config_stylesheet.LABEL_STYLESHEET)
        self.choose_accent_color = QtWidgets.QLineEdit(self)
        self.choose_accent_color.setText(config.ACCENT_COLOR)
        self.choose_accent_color.setStyleSheet(config_stylesheet.SETTINGS_LINE_EDITOR_STYLESHEET)
        # Кнопка сохранения настроек
        self.save_settings = QtWidgets.QPushButton(self)
        self.save_settings.setText('Сохранить')
        self.save_settings.clicked.connect(self.save_changes)
        self.save_settings.setStyleSheet(config_stylesheet.BUTTON_STYLESHEET)
        # Кнопка сброса настроек
        self.reset_settings = QtWidgets.QPushButton(self)
        self.reset_settings.setText('Сброс настроек')
        self.reset_settings.clicked.connect(self.reset)
        self.reset_settings.setStyleSheet(config_stylesheet.BUTTON_STYLESHEET)
        # Кнопка отмены изменений
        self.cancel_changes = QtWidgets.QPushButton(self)
        self.cancel_changes.setText('Отмена')
        self.cancel_changes.clicked.connect(self.cancel)
        self.cancel_changes.setStyleSheet(config_stylesheet.BUTTON_STYLESHEET)

        self.grid_layout.addWidget(self.font_family_settings, 0, 0)
        self.grid_layout.addWidget(self.select_font_family, 0, 1)
        self.grid_layout.addWidget(self.font_size_settings, 1, 0)
        self.grid_layout.addWidget(self.set_font_size, 1, 1)
        self.grid_layout.addWidget(self.label_font_size_settings, 2, 0)
        self.grid_layout.addWidget(self.set_label_font_size, 2, 1)
        self.grid_layout.addWidget(self.background_color_settings, 3, 0)
        self.grid_layout.addWidget(self.set_background_color, 3, 1)
        self.grid_layout.addWidget(self.default_folder_settings, 4, 0)
        self.grid_layout.addWidget(self.default_directory, 4, 1)
        self.grid_layout.addWidget(self.select_default_folder, 4, 2)
        self.grid_layout.addWidget(self.accent_colour, 5, 0)
        self.grid_layout.addWidget(self.choose_accent_color, 5, 1)

        self.button_layout = QHBoxLayout()
        self.main_layout.addLayout(self.button_layout)
        self.button_layout.addStretch()
        self.button_layout.addWidget(self.save_settings)
        self.button_layout.addWidget(self.reset_settings)
        self.button_layout.addWidget(self.cancel_changes)

    def select_folder(self):
        folder_name = QFileDialog.getExistingDirectory(self)
        if folder_name != '':
            self.default_directory.setText(folder_name)

    @staticmethod
    def information_window():
        info = QMessageBox()
        info.setWindowTitle('Настройки')
        info.setIcon(QMessageBox.Icon.Information)
        info.setText('Для применения изменений перезапустите приложение.')
        info.setStyleSheet(config_stylesheet.MESSAGE_BOX_STYLESHEET)
        info.exec()

    @staticmethod
    def warning_window(e):
        info = QMessageBox()
        info.setWindowTitle('Настройки')
        info.setIcon(QMessageBox.Icon.Warning)
        info.setText(f'Ошибка: {e}')
        info.setStyleSheet(config_stylesheet.MESSAGE_BOX_STYLESHEET)
        info.exec()

    def save_changes(self):
        new_default_directory = self.default_directory.text().replace('\\', '/')
        new_font_family = self.select_font_family.text()
        new_font_size = self.set_font_size.text()
        new_label_font_size = self.set_label_font_size.text()
        new_background_color = self.set_background_color.text()
        new_accent_color = self.choose_accent_color.text()

        changes_list = ("import os \n\n"
                        "# Папка для сохранения текстовых документов по умолчанию\n",
                        f"DEFAULT_FOLDER = '{new_default_directory}'\n\n",
                        "# Шрифт по умолчанию\n",
                        f"FONT_FAMILY = '{new_font_family}'\n",
                        "# Размер основного текста по умолчанию\n",
                        f"FONT_SIZE = '{new_font_size}'\n",
                        "# Размер заголовка по умолчанию\n",
                        f"LABEL_FONT_SIZE = '{new_label_font_size}'\n",
                        "# Фоновый цвет текстового поля по умолчанию\n",
                        f"BACKGROUND_COLOR_RGBA_CODE = '{new_background_color}'\n",
                        "# Акцентный цвет\n"
                        f"ACCENT_COLOR = '{new_accent_color}'\n",
                        "# Цвет обводки полей\n"
                        "BORDER_COLOR = f'{ACCENT_COLOR}, 0.7'\n")

        with open('config.py', 'w', encoding='utf-8') as configuration:
            configuration.writelines(changes_list)

        SettingsGUI.information_window()

    @staticmethod
    def reset():
        with open('default_config.py') as default_configuration:
            default_conf = default_configuration.read()
        with open('config.py', 'w') as configuration:
            configuration.write(default_conf)
        SettingsGUI.information_window()

    def cancel(self):
        self.close()

if __name__ == '__main__':
    import sys
    application = QtWidgets.QApplication(sys.argv)
    settings_window = SettingsGUI()
    settings_window.show()
    sys.exit(application.exec())