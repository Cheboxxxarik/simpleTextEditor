from PyQt6.QtWidgets import QMessageBox
import os
import json

CONFIG_DIR = os.path.dirname(__file__)
CONFIG_FILE = os.path.join('config.json')

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return create_default_config()
    
    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as file:
            config_data = json.load(file)
            
            # Преобразуем вашу структуру в совместимую
            return {
                'FONT_FAMILY': config_data['font']['family'],
                'FONT_SIZE': config_data['font']['size'],
                'LABEL_FONT_SIZE': config_data['font']['label_size'],
                'BACKGROUND_COLOR_RGBA_CODE': config_data['colors']['background_rgba'],
                'ACCENT_COLOR': config_data['colors']['accent']
            }
    except Exception as e:
        QMessageBox(f"Error loading config: {e}")
        return create_default_config()

def create_default_config():
    default_config = {
        "font": {
            "family": "Adwaita Sans",
            "size": "14pt",
            "label_size": "18pt"
        },
        "colors": {
            "background_rgba": "255, 255, 255, 0.1",
            "accent": "58, 94, 214",
            "border_opacity": 0.7
        }
    }
    
    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(CONFIG_FILE, 'w', encoding='utf-8') as file:
        json.dump(default_config, file, indent=4)
    
    return {
        'FONT_FAMILY': default_config['font']['family'],
        'FONT_SIZE': default_config['font']['size'],
        'LABEL_FONT_SIZE': default_config['font']['label_size'],
        'BACKGROUND_COLOR_RGBA_CODE': default_config['colors']['background_rgba'],
        'ACCENT_COLOR': default_config['colors']['accent']
    }

# Загружаем конфигурацию
config_data = load_config()

# Экспортируем переменные
DEFAULT_FOLDER = os.path.join(os.path.expanduser("~"), "Documents")
FONT_FAMILY = config_data['FONT_FAMILY']
FONT_SIZE = config_data['FONT_SIZE']
LABEL_FONT_SIZE = config_data['LABEL_FONT_SIZE']
BACKGROUND_COLOR_RGBA_CODE = config_data['BACKGROUND_COLOR_RGBA_CODE']
ACCENT_COLOR = config_data['ACCENT_COLOR']
BORDER_COLOR = f"{ACCENT_COLOR}, 0.7"