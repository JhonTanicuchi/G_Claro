import tkinter as tk
from tkinter_app.form_fields import FormFields

class FormWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.fields = FormFields(self)
        self.fields.pack()

        # Botón para enviar el formulario
        submit_button = tk.Button(self, text='Enviar', command=self.submit_form)
        submit_button.pack()

    def submit_form(self):
        # Obtener los valores de los campos de entrada
        nombre_completo = self.fields.nombre_completo_entry.get()
        cedula_pasaporte = self.fields.cedula_pasaporte_entry.get()
        numero_servicio = self.fields.numero_servicio_entry.get()

        """ # Lógica para enviar a Google Form
        submit_to_google_form(nombre_completo, cedula_pasaporte, numero_servicio)

        # Lógica para enviar a Google Sheets
        submit_to_google_sheets(nombre_completo, cedula_pasaporte, numero_servicio) """
