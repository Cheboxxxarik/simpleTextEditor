"""
config.py

Модуль конфигурации приложения.

Этот файл отвечает за:
- загрузку пользовательских настроек из config.json;
- инициализацию цветовой схемы и шрифтов;
- применение цветовой темы;
- централизованное хранение визуальных параметров интерфейса;
- помощь при генерации QSS-стилей для всех основных виджетов Qt.

Поддерживаемые возможности:
- автоматическое создание конфигурационного файла при отсутствии;
- поддержка пользовательских тем (JSON);

Структура:
- load_config()            — загружает конфигурацию и тему
- create_default_config()  — создаёт config.json по умолчанию
- theme_applier()          — применяет палитру Qt
- глобальные QSS-строки    — стили для основных UI-компонентов

Назначение:
Этот модуль должен использоваться как единый источник настроек внешнего вида.
"""

from PyQt6.QtWidgets import QMessageBox, QApplication
import json, os, sys

CONFIG_DIR = os.path.dirname(__file__)
CONFIG_FILE = os.path.join('config.json')

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return create_default_config()
    
    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as file:
            config_data = json.load(file)
            configuration = {
                            'FONT_FAMILY': config_data['font']['family'],
                            'FONT_SIZE': config_data['font']['size'],
                            'LABEL_FONT_SIZE': config_data['font']['label_size'],
                            'THEME': config_data['colors']['theme'],
                            'ACCENT_COLOR': config_data['colors']['accent'],
                            }
            theme_name = f'themes/{configuration['THEME']}.json'

        with open(theme_name) as theme:
            t = json.load(theme)
            configuration['BACKGROUND_COLOR'] = t.get('background_color', '#ffffff')
            configuration['BORDER_COLOR'] = t.get('border_color', "#9fa0a0")
            configuration['WINDOW_COLOR'] = t.get('window_color')
        
        return configuration
    except Exception as e:
        app = QApplication(sys.argv)
        QMessageBox.critical(None, "Error", f"Error loading config: {e}")
        sys.exit(app.exec())
        return create_default_config()
        
def reload_config():
    return load_config()

def create_default_config():
    default_config = {
        "font": {
            "family": "Adwaita Sans",
            "size": "14pt",
            "label_size": "18pt"
        },
        "colors": {
            "theme": "Dark",
            "accent": "58, 94, 214",
        }
    }
    
    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(CONFIG_FILE, 'w', encoding='utf-8') as file:
        json.dump(default_config, file, indent=4)
    
    return {
        'FONT_FAMILY': default_config['font']['family'],
        'FONT_SIZE': default_config['font']['size'],
        'LABEL_FONT_SIZE': default_config['font']['label_size'],
        'THEME': default_config['colors']['theme'],
        'ACCENT_COLOR': default_config['colors']['accent'],
        'BACKGROUND_COLOR': '#333637',
        'BORDER_COLOR': '#9fa0a0',
        'WINDOW_COLOR': '#1e1e1e'
    }

def get_documents_folder():
    documents = os.path.join(os.path.expanduser("~"), "Documents")
    if not os.path.isdir(documents):
        os.mkdir(documents)
    return documents

# Загружаем конфигурацию
config_data = load_config()

# Экспортируем переменные
DEFAULT_FOLDER = get_documents_folder()
FONT_FAMILY = config_data['FONT_FAMILY']
FONT_SIZE = config_data['FONT_SIZE']
LABEL_FONT_SIZE = config_data['LABEL_FONT_SIZE']
THEME = config_data['THEME']
ACCENT_COLOR = config_data['ACCENT_COLOR']
BACKGROUND_COLOR = config_data['BACKGROUND_COLOR']
BORDER_COLOR = config_data['BORDER_COLOR']
WINDOW_COLOR = config_data['WINDOW_COLOR']