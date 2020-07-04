from tkinter import ttk

COLOR_PRIMARY = '#0F1E33'
FONT_PRIMARY = 'Microsoft JhengHei UI'
LIGHT_TEXT_COLOR = '#BFB8B8'
ATTACHMENT_BUTTON_COLOR_PRIMARY = '#616161'
ATTACHMENT_BUTTON_COLOR_SECONDARY = '#474444'
SEND_BUTTON_COLOR_PRIMARY = '#00FF80'
SEND_BUTTON_COLOR_SECONDARY = '#0FC168'
SEND_BUTTON_TEXT_COLOR = '#fff'


class Styles(ttk.Style):
    def __init__(self):
        super().__init__()
        self.theme_use('clam')
        self.set_app_styles()

    def set_app_styles(self):
        self.set_frames_style()
        self.set_labels_style()
        self.set_buttons_style()

    def set_frames_style(self):
        self.configure(
            'EmailFrame.TFrame',
            background=COLOR_PRIMARY
        )

    def set_labels_style(self):
        self.configure(
            'BaseLabel.TLabel',
            background=COLOR_PRIMARY,
            foreground=LIGHT_TEXT_COLOR,
            font=(FONT_PRIMARY, 20)
        )

    def set_buttons_style(self):
        self.configure(
            'AttachmentButton.TButton',
            background=ATTACHMENT_BUTTON_COLOR_PRIMARY,
            foreground=LIGHT_TEXT_COLOR,
            font=(FONT_PRIMARY, 15)
        )
        self.map(
            'AttachmentButton.TButton',
            background=[('active', ATTACHMENT_BUTTON_COLOR_SECONDARY), ('disabled', ATTACHMENT_BUTTON_COLOR_PRIMARY)]
        )
        self.configure(
            'SendButton.TButton',
            background=SEND_BUTTON_COLOR_PRIMARY,
            foreground=SEND_BUTTON_TEXT_COLOR,
            font=(FONT_PRIMARY, 15, 'bold')
        )
        self.map(
            'SendButton.TButton',
            background=[('active', SEND_BUTTON_COLOR_SECONDARY), ('disabled', SEND_BUTTON_COLOR_PRIMARY)]
        )