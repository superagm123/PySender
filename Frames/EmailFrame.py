import tkinter as tk
from tkinter import ttk
from Email import Email


class EmailFrame(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self['style'] = 'EmailFrame.TFrame'
        self.columnconfigure(1, weight=1)
        self.labels_style = 'BaseLabel.TLabel'
        self.entries_font = 'Microsoft JhengHei UI'
        self.entries_font_size = 15
        self.from_value = tk.StringVar()
        self.to_value = tk.StringVar()
        self.subject_value = tk.StringVar()
        self.message_body = tk.Text(self)

        self.create_email_wigets()

        for child in self.winfo_children():
            child.grid_configure(padx=20, pady=20)

    def create_email_wigets(self):
        from_label = ttk.Label(self, text='FROM: ', style=self.labels_style)
        from_label.grid(row=0, column=0, sticky='W')

        from_entry = ttk.Entry(self, textvariable=self.from_value, font=(self.entries_font, self.entries_font_size))
        from_entry.grid(row=0, column=1, sticky='EW')

        to_label = ttk.Label(self, text='TO: ', style=self.labels_style)
        to_label.grid(row=1, column=0, sticky='W')

        to_entry = ttk.Entry(self, textvariable=self.to_value, font=(self.entries_font, self.entries_font_size))
        to_entry.grid(row=1, column=1, sticky='EW')

        subject_label = ttk.Label(self, text='SUBJECT: ', style=self.labels_style)
        subject_label.grid(row=2, column=0, sticky='W')

        subject_entry = ttk.Entry(
            self,
            textvariable=self.subject_value,
            font=(self.entries_font, self.entries_font_size)
        )
        subject_entry.grid(row=2, column=1, sticky='EW')

        message_label = ttk.Label(self, text='MESSAGE: ', style=self.labels_style)
        message_label.grid(row=3, column=0, sticky='W')

        attachment_button = ttk.Button(self, text='Attachment', cursor='hand2', style='AttachmentButton.TButton')
        attachment_button.grid(row=3, column=1, sticky='E')

        self.message_body.configure(height=20, font=(self.entries_font, self.entries_font_size))
        self.message_body.grid(row=4, column=0, columnspan=2, sticky='EW')

        scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.message_body.yview)
        scrollbar.grid(row=4, column=1, sticky='NSE')

        self.message_body['yscrollcommand'] = scrollbar.set

        sent_message_button = ttk.Button(
            self,
            text='Send',
            cursor='hand2',
            style='SendButton.TButton',
            command=self.send_email
        )
        sent_message_button.grid(row=5, column=1, sticky='E')

    def send_email(self):
        email = Email()
        email.compose_email(
            self.from_value.get(),
            self.to_value.get(),
            self.subject_value.get(),
            self.message_body.get('1.0', 'end')
        )
        email.send_email()
        self.clean_fields()

    def clean_fields(self):
        self.from_value.set('')
        self.to_value.set('')
        self.subject_value.set('')
        self.message_body.delete('1.0', 'end')
