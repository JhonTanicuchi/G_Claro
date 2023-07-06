import tkinter as tk
from tkinter import ttk

class FormFields(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.cedula_pasaporte_label = tk.Label(self, text='Cédula/RUC/Pasaporte:')
        self.cedula_pasaporte_label.pack()
        self.cedula_pasaporte_entry = ttk.Entry(self)
        self.cedula_pasaporte_entry.pack()

        self.nombre_completo_label = tk.Label(self, text='Nombre Completo:')
        self.nombre_completo_label.pack()
        self.nombre_completo_entry = ttk.Entry(self)
        self.nombre_completo_entry.pack()

        self.numero_servicio_label = tk.Label(self, text='Número de Servicio:')
        self.numero_servicio_label.pack()
        self.numero_servicio_entry = ttk.Entry(self)
        self.numero_servicio_entry.pack()

        self.llamada_estado_label = tk.Label(self, text='Estado:')
        self.llamada_estado_label.pack()
        self.llamada_estado_combobox = ttk.Combobox(self, values=[
            'Retenido',
            'No retenido',
            'No retenido NA',
            'Atención cliente',
            'Llamada incompleta',
            'Mala transferencia'
        ], state='readonly')
        self.llamada_estado_combobox.set('Selecciona un estado')
        self.llamada_estado_combobox.pack()
