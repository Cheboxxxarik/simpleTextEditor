from PyQt6.QtGui import QPalette, QColor
import config

class Palette:
    def __init__(self, window_color, window_text_color,
                 base_color, alternate_base_color,
                 text_color, highlight_color,
                 link_color, link_visited_color,
                 tool_tip_base_color, tool_tip_text_color,
                 placeholder_color, bright_text_color, mid_color,
                 dark_color, shadow_color, light_color, disabled_window_text_color,
                 disabled_text_color, disabled_highlight_color,
                 disabled_highlighted_text_color):
        self.palette = QPalette()
        self.window_color = window_color
        self.window_text_color = window_text_color
        self.base_color = base_color
        self.alternate_base_color = alternate_base_color
        self.text_color = text_color
        self.highlight_color = highlight_color
        self.highlighted_text_color = QColor(config.ACCENT_COLOR)
        self.link_color = link_color
        self.link_visited_color = link_visited_color
        self.tool_tip_base_color = tool_tip_base_color
        self.tool_tip_base_color = tool_tip_text_color
        self.placeholder_color = placeholder_color
        self.bright_text_color = bright_text_color
        self.mid_color = mid_color
        self.dark_color = dark_color
        self.shadow_color = shadow_color
        self.light_color = light_color
        # Цвета для состояний (disabled)
        self.disabled_window_text_color = disabled_window_text_color # Цвет окна
        self.disabled_text_color = disabled_text_color # Цвет текста
        self.disabled_highlight_color = disabled_highlight_color # Цвет выделения
        self.disabled_highlighted_text_color = disabled_highlighted_text_color # Цвет выделенного текста
    
    def palette_applier(self, app):
        # Активные элементы
        self.palette.setColor(QPalette.ColorRole.Window, self.window_color)
        self.palette.setColor(QPalette.ColorRole.WindowText, self.window_text_color)
        self.palette.setColor(QPalette.ColorRole.Base, self.base_color)
        self.palette.setColor(QPalette.ColorRole.AlternateBase, self.alternate_base_color)
        self.palette.setColor(QPalette.ColorRole.Text, self.text_color)
        self.palette.setColor(QPalette.ColorRole.Button, self.button_color)
        self.palette.setColor(QPalette.ColorRole.ButtonText, self.button_text_color)
        
        # Акцентные цвета
        self.palette.setColor(QPalette.ColorRole.Highlight, self.highlight_color)
        self.palette.setColor(QPalette.ColorRole.HighlightedText, self.highlighted_text_color)
        self.palette.setColor(QPalette.ColorRole.Link, self.link_color)
        self.palette.setColor(QPalette.ColorRole.LinkVisited, self.link_visited_color)

        # Дополнительные цвета
        self.palette.setColor(QPalette.ColorRole.ToolTipBase, self.tool_tip_base_color)
        self.palette.setColor(QPalette.ColorRole.ToolTipText, self.tool_tip_text_color)
        self.palette.setColor(QPalette.ColorRole.PlaceholderText, self.placeholder_color)
        self.palette.setColor(QPalette.ColorRole.BrightText, self.bright_text_color)
    
        # Цвета для состояний (disabled)
        self.palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, self.disabled_window_text_color)
        self.palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, self.disabled_text_color)
        self.palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Highlight, self.disabled_highlight_color)
        self.palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.HighlightedText, self.disabled_highlighted_text_color)

        # Цвета границ и теней
        self.palette.setColor(QPalette.ColorRole.Mid, self.mid_color)           # Средние элементы
        self.palette.setColor(QPalette.ColorRole.Dark, self.dark_color)         # Темные элементы
        self.palette.setColor(QPalette.ColorRole.Shadow, self.shadow_color)     # Тени
        self.palette.setColor(QPalette.ColorRole.Light, self.light_color)

        app.setPalette(self.palette)