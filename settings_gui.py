"""
settings_gui.py

Окно настроек приложения.
Отвечает за:
- отображение текущих параметров
- сохранение изменений
- применение темы в реальном времени
"""

from PyQt6 import QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import pyqtSignal
from pathlib import Path
import json, os
import config, config_stylesheet

class SettingsGUI(QtWidgets.QDialog):
    # Отслеживание изменений в настройках
    settings_applied = pyqtSignal()

    def __init__(self):
        super(SettingsGUI, self).__init__()
        self.setWindowTitle('Настройки')
        # Добавление иконки приложения
        self.setWindowIcon(QIcon('simpleTextEditor.ico'))
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.grid_layout = QtWidgets.QGridLayout()
        self.main_layout.addLayout(self.grid_layout)
        # Выбор семейства шрифтов
        self.font_family_settings = QtWidgets.QLabel(self)
        self.font_family_settings.setText('Шрифт:')
        self.font_family_settings.setStyleSheet(config_stylesheet.LABEL_STYLESHEET)
        self.select_font_family = QtWidgets.QLineEdit(self)
        self.select_font_family.setText(config.FONT_FAMILY)
        self.select_font_family.setStyleSheet(config_stylesheet.SETTINGS_LINE_EDITOR_STYLESHEET)
        # Выбор размера текста
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
        # Настройки темы
        self.theme_label = QtWidgets.QLabel(self)
        self.theme_label.setText('Тема:')
        self.theme_label.setStyleSheet(config_stylesheet.LABEL_STYLESHEET)
        self.choose_theme = QtWidgets.QComboBox(self)
        self.choose_theme.addItems(self.get_themes())
        self.choose_theme.setCurrentIndex(self.get_current_theme())
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
        self.grid_layout.addWidget(self.theme_label, 3, 0)
        self.grid_layout.addWidget(self.choose_theme, 3, 1)
        self.grid_layout.addWidget(self.accent_colour, 4, 0)
        self.grid_layout.addWidget(self.choose_accent_color, 4, 1)

        self.button_layout = QtWidgets.QHBoxLayout()
        self.main_layout.addLayout(self.button_layout)
        self.button_layout.addStretch()
        self.button_layout.addWidget(self.save_settings)
        self.button_layout.addWidget(self.reset_settings)
        self.button_layout.addWidget(self.cancel_changes)

    # Функция получения текущей темы
    def get_current_theme(self):
        index = self.choose_theme.findText(config.THEME)
        return index if index != -1 else 0
    
    # Функция для получения тем
    @staticmethod
    def get_themes():
        return sorted(p.stem for p in Path("themes").glob("*.json"))

    # Уведомление об ошибке
    @staticmethod
    def warning_window(e):
        info = QtWidgets.QMessageBox()
        info.setWindowTitle('Настройки')
        info.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        info.setText(f'Ошибка: {e}')
        info.setStyleSheet(config_stylesheet.MESSAGE_BOX_STYLESHEET)
        info.exec()

    # Функция для проверки правильности формата цвета
    def check_colors(self, new_accent_color):
        try:
            rgb = []
            
            for x in new_accent_color.split(','):
                cleaned = x.strip()
                number = int(cleaned)
                rgb.append(number)

            if len(rgb) != 3:
                raise ValueError("Цвет должен состоять из трёх чисел")

            for value in rgb:
                if not 0 <= value <= 255:
                    raise ValueError("Значения цвета должны быть от 0 до 255")

            return True  # всё ок

        except Exception as e:
            self.warning_window(str(e))
            self.choose_accent_color.setText(config.ACCENT_COLOR)
            return False

    def apply_styles(self):
        import importlib
        import config_stylesheet
    
        importlib.reload(config_stylesheet)
    
        self.setStyleSheet("")  # сброс кеша Qt
    
        for w in self.findChildren(QtWidgets.QWidget):
            w.setStyleSheet("")
    
        # Применяем стили вручную
        self.font_family_settings.setStyleSheet(config_stylesheet.LABEL_STYLESHEET)
        self.font_size_settings.setStyleSheet(config_stylesheet.LABEL_STYLESHEET)
        self.label_font_size_settings.setStyleSheet(config_stylesheet.LABEL_STYLESHEET)
        self.theme_label.setStyleSheet(config_stylesheet.LABEL_STYLESHEET)
        self.accent_colour.setStyleSheet(config_stylesheet.LABEL_STYLESHEET)
    
        self.select_font_family.setStyleSheet(config_stylesheet.SETTINGS_LINE_EDITOR_STYLESHEET)
        self.set_font_size.setStyleSheet(config_stylesheet.SETTINGS_LINE_EDITOR_STYLESHEET)
        self.set_label_font_size.setStyleSheet(config_stylesheet.SETTINGS_LINE_EDITOR_STYLESHEET)
        self.choose_accent_color.setStyleSheet(config_stylesheet.SETTINGS_LINE_EDITOR_STYLESHEET)
    
        self.choose_theme.setStyleSheet(config_stylesheet.COMBO_BOX_STYLESHEET)
    
        self.save_settings.setStyleSheet(config_stylesheet.BUTTON_STYLESHEET)
        self.reset_settings.setStyleSheet(config_stylesheet.BUTTON_STYLESHEET)
        self.cancel_changes.setStyleSheet(config_stylesheet.BUTTON_STYLESHEET)

    # Функция для сохранения изменений в настройках
    def save_changes(self):
        new_theme = self.choose_theme.currentText() # Новая тема
        new_font_family = self.select_font_family.text() # Новый шрифт
        new_font_size = self.set_font_size.text() # Новый размер шрифта обычного текста
        new_label_font_size = self.set_label_font_size.text() # Новый размер шрифта в заголовках
        new_accent_color = self.choose_accent_color.text() # Новый акцентный цвет

        # Проверка корректности формата цвета 
        if self.check_colors(new_accent_color):
            new_config = {
                'font': {
                    'family': new_font_family,
                    'size': new_font_size,
                    'label_size': new_label_font_size
                },
                'colors': {
                    'theme': new_theme,
                    'accent': new_accent_color,
                }
            }

            # Сохраняет конфигурацию в JSON файл
            os.makedirs(config.CONFIG_DIR, exist_ok=True)
            with open(config.CONFIG_FILE, 'w', encoding='utf-8') as file:
                json.dump(new_config, file, indent=4)
        else:
            self.choose_accent_color.setText(config.ACCENT_COLOR)

        # Применение настроек
        config.reload_config()
        self.settings_applied.emit()
        self.apply_styles()
    
    # Функция для сброса настроек
    def reset(self):
        self.select_font_family.setText('Adwaita Sans')
        self.set_font_size.setText('14pt')
        self.set_label_font_size.setText('18pt')
        self.choose_theme.setCurrentText('Dark')
        self.choose_accent_color.setText('58, 94, 214')
        config.create_default_config()
        config.reload_config()
        self.settings_applied.emit()
        self.apply_styles()

    # Функция для отмены настроек (закрытия окна настроек)
    def cancel(self):
        self.close()

# Запуск приложения
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion') 
    config_stylesheet.theme_applier(app)
    window = SettingsGUI()
    window.show()
    sys.exit(app.exec())