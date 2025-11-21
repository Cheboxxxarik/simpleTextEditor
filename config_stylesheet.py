from PyQt6.QtGui import QPalette, QColor
import config

def theme_applier(app):
    if config.THEME == 'light':
        palette = QPalette()
    
        # Основные цвета
        window_color = QColor(240, 240, 240)        # Фон окон
        window_text_color = QColor(0, 0, 0)         # Текст на фоне окон
        base_color = QColor(255, 255, 255)          # Фон виджетов ввода
        alternate_base_color = QColor(248, 248, 248) # Альтернативный фон
        text_color = QColor(0, 0, 0)                # Основной текст
        button_color = QColor(240, 240, 240)        # Фон кнопок
        button_text_color = QColor(0, 0, 0)         # Текст кнопок
    
        # Акцентные цвета
        highlight_color = QColor(0, 120, 215)       # Цвет выделения
        highlighted_text_color = QColor(255, 255, 255) # Текст выделения
        link_color = QColor(0, 0, 255)              # Цвет ссылок
        link_visited_color = QColor(128, 0, 128)    # Цвет посещенных ссылок
    
        # Дополнительные цвета
        tool_tip_base_color = QColor(255, 255, 220) # Фон подсказок
        tool_tip_text_color = QColor(0, 0, 0)       # Текст подсказок
        placeholder_color = QColor(128, 128, 128)   # Цвет плейсхолдера
        bright_text_color = QColor(255, 255, 255)   # Яркий текст
        mid_color = QColor(160, 160, 160)           # Средний цвет для границ
        dark_color = QColor(96, 96, 96)             # Темный цвет
        shadow_color = QColor(80, 80, 80)           # Цвет тени
        light_color = QColor(255, 255, 255)         # Светлый цвет
    
        # === Установка цветов в палитру ===
    
        # Активные элементы
        palette.setColor(QPalette.ColorRole.Window, window_color)
        palette.setColor(QPalette.ColorRole.WindowText, window_text_color)
        palette.setColor(QPalette.ColorRole.Base, base_color)
        palette.setColor(QPalette.ColorRole.AlternateBase, alternate_base_color)
        palette.setColor(QPalette.ColorRole.Text, text_color)
        palette.setColor(QPalette.ColorRole.Button, button_color)
        palette.setColor(QPalette.ColorRole.ButtonText, button_text_color)
    
        # Акцентные цвета
        palette.setColor(QPalette.ColorRole.Highlight, highlight_color)
        palette.setColor(QPalette.ColorRole.HighlightedText, highlighted_text_color)
        palette.setColor(QPalette.ColorRole.Link, link_color)
        palette.setColor(QPalette.ColorRole.LinkVisited, link_visited_color)
    
        # Дополнительные цвета
        palette.setColor(QPalette.ColorRole.ToolTipBase, tool_tip_base_color)
        palette.setColor(QPalette.ColorRole.ToolTipText, tool_tip_text_color)
        palette.setColor(QPalette.ColorRole.PlaceholderText, placeholder_color)
        palette.setColor(QPalette.ColorRole.BrightText, bright_text_color)
    
        # Цвета для состояний (disabled)
        palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, QColor(128, 128, 128))
        palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, QColor(128, 128, 128))
        palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, QColor(128, 128, 128))
        palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Highlight, QColor(200, 200, 200))
        palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.HighlightedText, QColor(128, 128, 128))
    
        # Цвета границ и теней
        palette.setColor(QPalette.ColorRole.Mid, mid_color)           # Средние элементы
        palette.setColor(QPalette.ColorRole.Dark, dark_color)         # Темные элементы
        palette.setColor(QPalette.ColorRole.Shadow, shadow_color)     # Тени
        palette.setColor(QPalette.ColorRole.Light, light_color) 
    elif config.THEME == 'dark':
        dark_palette = QPalette()
    
        # Базовые цвета для темной темы
        dark_color = QColor(45, 45, 45)
        text_color = QColor(255, 255, 255)
        highlight_color = QColor(42, 130, 218)
        placeholder_color = QColor(161, 161, 161)
    
        # Настройка палитры
        dark_palette.setColor(QPalette.ColorRole.Window, dark_color)
        dark_palette.setColor(QPalette.ColorRole.WindowText, text_color)
        dark_palette.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.ColorRole.AlternateBase, dark_color)
        dark_palette.setColor(QPalette.ColorRole.ToolTipBase, text_color)
        dark_palette.setColor(QPalette.ColorRole.ToolTipText, text_color)
        dark_palette.setColor(QPalette.ColorRole.Text, text_color)
        dark_palette.setColor(QPalette.ColorRole.Button, dark_color)
        dark_palette.setColor(QPalette.ColorRole.ButtonText, text_color)
        dark_palette.setColor(QPalette.ColorRole.BrightText, QColor(255, 0, 0))
        dark_palette.setColor(QPalette.ColorRole.Link, highlight_color)
        dark_palette.setColor(QPalette.ColorRole.Highlight, highlight_color)
        dark_palette.setColor(QPalette.ColorRole.HighlightedText, QColor(0, 0, 0))
        dark_palette.setColor(QPalette.ColorRole.PlaceholderText, placeholder_color)
    
        app.setPalette(dark_palette)            
    else:
        pass

# Поле для заголовка
TITLE_EDITOR_STYLESHEET = f'''
    QLineEdit {{
        font-family: {config.FONT_FAMILY};
        font-size: {config.LABEL_FONT_SIZE};
        border: 1px solid rgba(212, 212, 212, 0.8);
        border-radius: 20px;
        padding: 16px 20px;
        selection-background-color: rgba({config.ACCENT_COLOR}, 0.3);
        background-color: rgba({config.BACKGROUND_COLOR_RGBA_CODE});    
    }}
    QLineEdit:hover {{
        border: 1px solid rgba({config.BORDER_COLOR});
    }}
    QLineEdit:focus {{
        border: 2.25px solid rgba({config.BORDER_COLOR});
        padding: 13.75px 18.75px;
    }}
'''
# Поля для ввода настроек
SETTINGS_LINE_EDITOR_STYLESHEET = f'''
    QLineEdit {{
        font-family: {config.FONT_FAMILY};
        font-size: {config.FONT_SIZE};
        background-color: rgba({config.BACKGROUND_COLOR_RGBA_CODE});
        border: 1px solid rgba(212, 212, 212, 0.8);
        border-radius: 10px;
        padding-top: 5px;
        padding-left: 5px;
        padding-bottom: 5px;
        selection-background-color: rgba({config.ACCENT_COLOR}, 0.3);
    }}
    QLineEdit:hover {{
        border: 1px solid rgba({config.BORDER_COLOR});
    }}
    QLineEdit:focus {{
        border: 2.25px solid rgba({config.BORDER_COLOR});
        padding: 2.75px;
    }}
'''
# Поля для ввода текста
TEXT_EDITOR_STYLESHEET = f'''
    QTextEdit {{
        font-family: {config.FONT_FAMILY};
        font-size: {config.FONT_SIZE};
        border: 1px solid rgba(212, 212, 212, 0.7);
        border-radius: 20px;
        padding: 16px 20px;
        background: rgba({config.BACKGROUND_COLOR_RGBA_CODE});
    }}
    QTextEdit:hover {{
        border: 1px solid rgba({config.BORDER_COLOR});
    }}
    QTextEdit:focus {{
        border: 2.25px solid rgba({config.BORDER_COLOR});
        padding: 13.75px 18.75px;
    }}
'''
# Стиль для текста
LABEL_STYLESHEET = f'''
    QLabel {{
        font-family: {config.FONT_FAMILY};
        font-size: {config.FONT_SIZE};
        background-color: rgba({config.BACKGROUND_COLOR_RGBA_CODE});
        border-radius: 10px;
        padding-top: 5px;
        padding-left: 5px;
        padding-bottom: 5px;
        selection-background-color: rgba({config.ACCENT_COLOR}, 0.3);
    }}
'''
# Меню-бар
MENU_BAR_STYLESHEET = f'''
    QMenuBar {{
        border: none;
        padding: 4px 8px;
        font-family: {config.FONT_FAMILY};
        font-size: 13px;
    }}
    
    QMenuBar::item {{
        padding: 6px 12px;
        border-radius: 8px;
        margin: 2px;
    }}
    
    QMenuBar::item:selected {{
        background-color: rgba({config.ACCENT_COLOR}, 0.15);
        color: rgb({config.ACCENT_COLOR});
    }}
    
    QMenuBar::item:pressed {{
        background-color: rgba({config.ACCENT_COLOR}, 0.25);
    }}

    QMenu {{
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 6px;
        font-family: {config.FONT_FAMILY};
        font-size: 13px;
    }}
    
    QMenu::item {{
        outline: none;
        padding: 8px 16px;
        border-radius: 8px;
        margin: 2px 0;
    }}
    
    QMenu::item:selected {{
        background-color: rgba({config.ACCENT_COLOR}, 0.15);
        color: rgb({config.ACCENT_COLOR});
    }}
    
    QMenu::item:pressed {{
        background-color: rgba({config.ACCENT_COLOR}, 0.25);
    }}
    
    /* Индикаторы (галочки) */
    QMenu::indicator {{
        width: 14px;
        height: 14px;
        border-radius: 3px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        margin-right: 8px;
    }}
    
    QMenu::indicator:checked {{
        background-color: rgba({config.ACCENT_COLOR}, 0.8);
        border: 1px solid rgba({config.ACCENT_COLOR}, 0.9);
    }}
'''
# Стиль для кнопок
BUTTON_STYLESHEET = f"""
    QPushButton {{
        font-family: {config.FONT_FAMILY};
        font-size: 12pt;
        font-weight: 500;
        background-color: rgb({config.ACCENT_COLOR});
        color: white;
        border: none;
        border-radius: 6px;
        padding: 8px;
    }}
    QPushButton:hover {{
        background-color: rgba({config.ACCENT_COLOR}, 0.8);
    }}
    QPushButton:pressed {{
        background-color: rgba({config.ACCENT_COLOR}, 0.6);
    }}
"""
# Стиль для выпадающих списков
COMBO_BOX_STYLESHEET = f'''
    QComboBox {{
        font-family: {config.FONT_FAMILY};
        font-size: {config.FONT_SIZE};
        background-color: rgba({config.BACKGROUND_COLOR_RGBA_CODE});
        border: 1px solid rgba(212, 212, 212, 0.8);
        border-radius: 10px;
        padding-top: 5px;
        padding-left: 5px;
        padding-right: 30px; /* Место для стрелки */
        padding-bottom: 5px;
        min-width: 120px;
    }}
    
    QComboBox:hover {{
        border: 1px solid rgba({config.BORDER_COLOR});
    }}
    
    QComboBox:focus {{
        border: 2px solid rgba({config.BORDER_COLOR});
    }}
    
    QComboBox:on {{
        background-color: rgba({config.BACKGROUND_COLOR_RGBA_CODE}, 0.95);
        border-radius: 10px;
    }}
    
    /* Стиль для выпадающего списка */
    QComboBox QAbstractItemView {{
        border: 1px solid rgba(255, 255, 255, 0.4);
        border-radius: 10px;
        padding: 6px;
        outline: none;
        selection-background-color: rgba({config.ACCENT_COLOR}, 0.2);
        selection-color: rgb({config.ACCENT_COLOR});
    }}
    
    QComboBox QAbstractItemView::item {{
        padding: 8px 12px;
        border-radius: 6px;
        margin: 2px;
    }}
    
    QComboBox QAbstractItemView::item:selected {{
        border: 1px solid rgba({config.BORDER_COLOR});
    }}
    
    QComboBox QAbstractItemView::item:hover {{
        background-color: rgba({config.ACCENT_COLOR}, 0.2);
    }}
    
    /* Стиль для стрелки */
    QComboBox::drop-down {{
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 25px;
        border-left: 1px solid rgba(255, 255, 255, 0.2);
        border-top-right-radius: 9px;
        border-bottom-right-radius: 9px;
    }}
    
    QComboBox::down-arrow {{
        image: url('resources/down_arrow.svg');
        color: rgba(148, 147, 146, 0.5);
        width: 12px;
        height: 12px;
        margin-left: 8px;
        margin-right: 8px;
    }}
    
    QComboBox::down-arrow:on {{
        image: url('resources/up_arrow.svg');
        border-top: none;
        border-bottom: 5px solid rgba(255, 255, 255, 0.9);
    }}
    
    /* Стиль для неактивного состояния */
    QComboBox:disabled {{
        color: rgba(255, 255, 255, 0.4);
        background-color: rgba({config.BACKGROUND_COLOR_RGBA_CODE}, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }}
    
    QComboBox::down-arrow:disabled {{
        border-top: 5px solid rgba(255, 255, 255, 0.3);
    }}
'''
# Стиль для всплывающих окон
MESSAGE_BOX_STYLESHEET = f'''
    QMessageBox {{
        font-family: {config.FONT_FAMILY};
        min-width: 200px;
        max-width: 200px;
        min-height: 100px;
    }}

    QMessageBox QLabel {{
        font-family: {config.FONT_FAMILY};
        font-size: {config.FONT_SIZE};
        background-color: transparent;
        border: none;
        padding: 8px;
    }}

    QMessageBox QLabel#qt_msgbox_label {{
        /* Основной текст сообщения */
        font-size: 14px;
        font-weight: bold;
        padding: 10px 12px 5px 12px;
    }}

    QMessageBox QPushButton {{
        font-family: {config.FONT_FAMILY};
        font-size: 11pt;
        font-weight: 500;
        background-color: rgb({config.ACCENT_COLOR});
        color: white;
        border-radius: 8px;
        padding: 6px 12px;
        min-width: 50px;
        margin: 3px;
    }}

    QMessageBox QPushButton:hover {{
        background-color: rgba({config.ACCENT_COLOR}, 0.8);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }}

    QMessageBox QPushButton:pressed {{
        background-color: rgba({config.ACCENT_COLOR}, 0.6);
        padding: 7px 13px;
    }}

    QMessageBox QPushButton:focus {{
        border: 2px solid rgba({config.BORDER_COLOR});
        outline: none;
    }}

    /* Увеличиваем иконку */
    QMessageBox QLabel#qt_msgboxex_icon_label {{
        background-color: transparent;
        border: none;
        padding: 15px;
    }}

    /* Область с кнопками - делаем компактнее */
    QMessageBox QDialogButtonBox {{
        background-color: transparent;
        border: none;
        padding: 8px 12px 12px 12px;
    }}
'''