import config

line_editor_stylesheet = f'''
    QLineEdit {{
        font-family: {config.font_family};
        font-size: {config.label_font_size};
        background-color: rgba({config.background_color_rgba_code});
        border: 1px solid rgba(255, 255, 255, 0.4);
        border-radius: 20px;
        padding: 16px 20px;
        selection-background-color: rgba(59, 130, 246, 0.3);
    }}
    QLineEdit:focus {{
        border: 2.25px solid rgba({config.border_color});
    }}
'''
label_stylesheet = f'''
    QLabel {{
        font-family: {config.font_family};
        font-size: {config.font_size};
        background-color: rgba({config.background_color_rgba_code});
        border: 1px solid rgba(255, 255, 255, 0.4);
        border-radius: 10px;
        padding-top: 5px;
        padding-left: 5px;
        padding-bottom: 5px;
        selection-background-color: rgba(59, 130, 246, 0.3);
    }}
'''
settings_line_editor_stylesheet = f'''
    QLineEdit {{
        font-family: {config.font_family};
        font-size: {config.font_size};
        background-color: rgba({config.background_color_rgba_code});
        border: 1px solid rgba(255, 255, 255, 0.4);
        border-radius: 10px;
        padding-top: 5px;
        padding-left: 5px;
        padding-bottom: 5px;
        selection-background-color: rgba(59, 130, 246, 0.3);
    }}
    QLineEdit:focus {{
        border: 2.25px solid rgba({config.border_color});
    }}
'''
text_editor_stylesheet = f'''
    QTextEdit {{
        font-family: {config.font_family};
        font-size: {config.font_size};
        background-color: rgba({config.background_color_rgba_code});
        border: 1px solid rgba(255, 255, 255, 0.4);
        border-radius: 20px;
        padding: 16px 20px;
    }}
    QTextEdit:focus {{
        border: 2.25px solid rgba({config.border_color});
    }}
'''
glass_button_stylesheet = '''
            QPushButton {
                background: rgba(59, 130, 246, 40);
                border: 1px solid rgba(255, 255, 255, 50);
                color: #1e40af;
                padding: 12px 14px;
                border-radius: 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background: rgba(59, 130, 246, 60);
                border: 1px solid rgba(255, 255, 255, 80);
            }
        '''
gradient_button_stylesheet = '''
            QPushButton {
                background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 #3b82f6, stop: 0.5 #2563eb, stop: 1 #1d4ed8);
                color: white;
                padding: 14px 14px;
                border: none;
                border-radius: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 #2563eb, stop: 0.5 #1d4ed8, stop: 1 #1e40af);
            }
        '''
minimalistic_button_stylesheet = """
            QPushButton {
                background: #eff6ff;
                color: #1d4ed8;
                border: 1px solid #dbeafe;
                padding: 14px 14px;
                border-radius: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background: #dbeafe;
                border: 1px solid #93c5fd;
            }
            QPushButton:pressed {
                background: #bfdbfe;
            }
        """

button_stylesheet = minimalistic_button_stylesheet