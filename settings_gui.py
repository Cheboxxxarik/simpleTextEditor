from PyQt6 import QtWidgets
from PyQt6.QtWidgets import (QDialog, QFileDialog, QVBoxLayout, 
                             QHBoxLayout, QGridLayout, QMessageBox)
from PyQt6.QtGui import QIcon
import json, os
import config as config, config_stylesheet

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
        self.background_color_settings.setText('Фоновый цвет текстовых полей (RGBA):')
        self.background_color_settings.setStyleSheet(config_stylesheet.LABEL_STYLESHEET)
        self.set_background_color = QtWidgets.QLineEdit(self)
        self.set_background_color.setText(config.BACKGROUND_COLOR_RGBA_CODE)
        self.set_background_color.setStyleSheet(config_stylesheet.SETTINGS_LINE_EDITOR_STYLESHEET)
        # Настройки темы
        self.theme_label = QtWidgets.QLabel(self)
        self.theme_label.setText('Тема:')
        self.theme_label.setStyleSheet(config_stylesheet.LABEL_STYLESHEET)
        self.choose_theme = QtWidgets.QComboBox(self)
        self.choose_theme.addItems(['Системная', 'Светлая', 'Тёмная'])
        self.get_current_theme()
        self.choose_theme.setStyleSheet(config_stylesheet.COMBO_BOX_STYLESHEET)
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
        self.grid_layout.addWidget(self.theme_label, 4, 0)
        self.grid_layout.addWidget(self.choose_theme, 4, 1)
        self.grid_layout.addWidget(self.accent_colour, 5, 0)
        self.grid_layout.addWidget(self.choose_accent_color, 5, 1)

        self.button_layout = QHBoxLayout()
        self.main_layout.addLayout(self.button_layout)
        self.button_layout.addStretch()
        self.button_layout.addWidget(self.save_settings)
        self.button_layout.addWidget(self.reset_settings)
        self.button_layout.addWidget(self.cancel_changes)

    def get_current_theme(self):
        if config.THEME == 'light':
            self.choose_theme.setCurrentIndex(1)
        elif config.THEME == 'dark':
            self.choose_theme.setCurrentIndex(2)
        else:
            self.choose_theme.setCurrentIndex(0)

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

    def check_colors(self, new_background_color, new_accent_color):
        try:
            bg_components = new_background_color.split(sep=',')
            acc_components = new_accent_color.split(sep=',')
            bg_color = tuple(float(component) for component in bg_components)
            acc_color = tuple(float(component) for component in acc_components)

            if len(bg_color) != 4 or len(acc_color) != 3:
                self.warning_window('Неверное количество цветовых компонентов!')
                return False
            if bg_color[3] > 1:
                self.warning_window('Вы ввели некорректные цвета')
                return False
            for i, j in zip(bg_color[:3], acc_color):
                if i > 255 or i < 0 or j > 255 or j < 0:
                    self.warning_window('Вы ввели некорректные цвета!')
                    return False
            return True
        except (ValueError, IndexError):
            self.warning_window('Ошибка при обработке цветов!')
            return False

    def save_changes(self):
        new_theme = self.choose_theme.currentIndex()
        new_font_family = self.select_font_family.text()
        new_font_size = self.set_font_size.text()
        new_label_font_size = self.set_label_font_size.text()
        new_background_color = self.set_background_color.text()
        new_accent_color = self.choose_accent_color.text()

        if new_theme == 1:
            new_theme = 'light'
        elif new_theme == 2:
            new_theme = 'dark'
        else:
            new_theme = 'system'

        if self.check_colors(new_background_color, new_accent_color):
            new_config = {
            'font': {
                'family': new_font_family,
                'size': new_font_size,
                'label_size': new_label_font_size
            },
            'colors': {
                'theme': new_theme,
                'background_rgba': new_background_color,
                'accent': new_accent_color,
                'border_opacity': 0.7
            }
            }

            # Сохраняет конфигурацию в JSON файл
            os.makedirs(config.CONFIG_DIR, exist_ok=True)
            with open(config.CONFIG_FILE, 'w', encoding='utf-8') as file:
                json.dump(new_config, file, indent=4)

            SettingsGUI.information_window()
        else:
            self.set_background_color.setText(config.BACKGROUND_COLOR_RGBA_CODE)
            self.choose_accent_color.setText(config.ACCENT_COLOR)
        
   
    def reset(self):
        config.create_default_config()
        self.information_window()

    def cancel(self):
        self.close()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion') 
    config_stylesheet.theme_applier(app)
    window = SettingsGUI()
    window.show()
    sys.exit(app.exec())