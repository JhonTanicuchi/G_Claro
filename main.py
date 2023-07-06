""" import tkinter as tk
from tkinter import ttk
from tkinter_app.form_window import FormWindow
from ttkthemes import ThemedStyle
from PIL import Image, ImageTk

import os
import sys
import win32api
import win32con
import win32gui
import win32ui

def main_window():
    # Crear la ventana del formulario
    form_window = FormWindow(window)
    form_window.pack()

def show_loading_screen():
    loading_frame = tk.Frame(window, bg='white')
    loading_frame.pack(fill='both', expand=True)

    container_frame = tk.Frame(loading_frame, bg='white')
    container_frame.place(relx=0.5, rely=0.5, anchor='center')

    global logo_image
    image_path  = 'assets/logo_claro.png'
    original_image = Image.open(image_path)
    resized_image = original_image.resize((50, 50), Image.LANCZOS)
    logo_image = ImageTk.PhotoImage(resized_image)
    logo_label = tk.Label(container_frame, image=logo_image, bg='white')
    logo_label.pack()

    loading_label = tk.Label(container_frame, text='Bienvenido a G_Claro', font=('Arial', 15), bg='white')
    loading_label.pack()

    window.update()

    window.after(2000, lambda: loading_frame.pack_forget())
    window.after(2000, main_window)

# Crear la ventana principal de la aplicación
window = tk.Tk()
window.title('G_Claro')
window.configure(bg='white')

# Crear una instancia del estilo temático
style = ThemedStyle(window)
style.set_theme('arc')

# Establecer el logo de la ventana
window.iconbitmap('assets/icon_claro.ico')

# Maximizar la ventana
window.state('zoomed')

# Mostrar la pantalla de carga al iniciar
show_loading_screen()

# Iniciar el bucle de eventos de la ventana
window.mainloop() assets/logo_claro.png
 """





import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="CustomTkinter", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("CTkTabview")
        self.tabview.add("Tab 2")
        self.tabview.add("Tab 3")
        self.tabview.tab("CTkTabview").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)

        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("CTkTabview"), dynamic_resizing=False,
                                                        values=["Value 1", "Value 2", "Value Long Long Long"])
        self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("CTkTabview"),
                                                    values=["Value 1", "Value 2", "Value Long....."])
        self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("CTkTabview"), text="Open CTkInputDialog",
                                                           command=self.open_input_dialog_event)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Tab 2"), text="CTkLabel on Tab 2")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

        # create radiobutton frame
        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="CTkRadioButton Group:")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1)
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=2)
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        # create slider and progressbar frame
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        self.seg_button_1 = customtkinter.CTkSegmentedButton(self.slider_progressbar_frame)
        self.seg_button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.progressbar_2 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_2.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.slider_1 = customtkinter.CTkSlider(self.slider_progressbar_frame, from_=0, to=1, number_of_steps=4)
        self.slider_1.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.slider_2 = customtkinter.CTkSlider(self.slider_progressbar_frame, orientation="vertical")
        self.slider_2.grid(row=0, column=1, rowspan=5, padx=(10, 10), pady=(10, 10), sticky="ns")
        self.progressbar_3 = customtkinter.CTkProgressBar(self.slider_progressbar_frame, orientation="vertical")
        self.progressbar_3.grid(row=0, column=2, rowspan=5, padx=(10, 20), pady=(10, 10), sticky="ns")

        # create scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="CTkScrollableFrame")
        self.scrollable_frame.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_switches = []
        for i in range(100):
            switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"CTkSwitch {i}")
            switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_switches.append(switch)

        # create checkbox and switch frame
        self.checkbox_slider_frame = customtkinter.CTkFrame(self)
        self.checkbox_slider_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.checkbox_1 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_1.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="n")
        self.checkbox_2 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_2.grid(row=2, column=0, pady=(20, 0), padx=20, sticky="n")
        self.checkbox_3 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_3.grid(row=3, column=0, pady=20, padx=20, sticky="n")

        # set default values
        self.sidebar_button_3.configure(state="disabled", text="Disabled CTkButton")
        self.checkbox_3.configure(state="disabled")
        self.checkbox_1.select()
        self.scrollable_frame_switches[0].select()
        self.scrollable_frame_switches[4].select()
        self.radio_button_3.configure(state="disabled")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.optionmenu_1.set("CTkOptionmenu")
        self.combobox_1.set("CTkComboBox")
        self.slider_1.configure(command=self.progressbar_2.set)
        self.slider_2.configure(command=self.progressbar_3.set)
        self.progressbar_1.configure(mode="indeterminnate")
        self.progressbar_1.start()
        self.textbox.insert("0.0", "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)
        self.seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3"])
        self.seg_button_1.set("Value 2")

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

if __name__ == "__main__":
    app = App()
    app.mainloop()



""" from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


# Configuración del controlador del navegador
options = Options()
options.add_argument('--headless')

# Inicializar el controlador de Chrome WebDriver
driver = webdriver.Chrome(options=options)

# Navegar a la página del formulario de Google
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSeVvy5WPNc2JwQl5lX5gU8bcq5agjw7Q4l-ElMIs7clxrUzEw/viewform')

# Encontrar los campos del formulario y enviar datos
nombre_completo_del_cliente = 'John Doe'
cedula_pasaporte = '123456789'
numero_servicio = '987654321'
tarifa_basica = '25'
site = 'UIO'

# Encontrar el campo de nombres utilizando el XPath completo
NOMBRE_COMPLETO_DEL_CLIENTE = driver.find_element(By.XPATH, '//div[contains(@data-params, "NOMBRE COMPLETO DEL CLIENTE")]//input')
CÉDULA_PASAPORTE = driver.find_element(By.XPATH, '//div[contains(@data-params, "CÉDULA/PASAPORTE")]//input')
NÚMERO_DE_SERVICIO = driver.find_element(By.XPATH, '//div[contains(@data-params, "NÚMERO DE SERVICIO")]//input')

# Desplazarse al elemento
actions = ActionChains(driver)

actions.move_to_element(NOMBRE_COMPLETO_DEL_CLIENTE).perform()
NOMBRE_COMPLETO_DEL_CLIENTE.send_keys(nombre_completo_del_cliente)

actions.move_to_element(CÉDULA_PASAPORTE).perform()
CÉDULA_PASAPORTE.send_keys(cedula_pasaporte)

actions.move_to_element(NÚMERO_DE_SERVICIO).perform()
NÚMERO_DE_SERVICIO.send_keys(numero_servicio)


 """


""" import tkinter as tk
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def submit_form():
    # Obtener los valores de los campos de entrada
    nombre_completo = nombre_completo_entry.get()
    cedula_pasaporte = cedula_pasaporte_entry.get()
    numero_servicio = numero_servicio_entry.get()

    # Configuración del controlador del navegador
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    # Navegar a la página del formulario de Google
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSeVvy5WPNc2JwQl5lX5gU8bcq5agjw7Q4l-ElMIs7clxrUzEw/viewform')

    # Encontrar los campos del formulario y enviar datos
    NOMBRE_COMPLETO_DEL_CLIENTE = driver.find_element(By.XPATH, '//div[contains(@data-params, "NOMBRE COMPLETO DEL CLIENTE")]//input')
    CÉDULA_PASAPORTE = driver.find_element(By.XPATH, '//div[contains(@data-params, "CÉDULA/PASAPORTE")]//input')
    NÚMERO_DE_SERVICIO = driver.find_element(By.XPATH, '//div[contains(@data-params, "NÚMERO DE SERVICIO")]//input')

    actions = ActionChains(driver)

    actions.move_to_element(NOMBRE_COMPLETO_DEL_CLIENTE).perform()
    NOMBRE_COMPLETO_DEL_CLIENTE.send_keys(nombre_completo)

    actions.move_to_element(CÉDULA_PASAPORTE).perform()
    CÉDULA_PASAPORTE.send_keys(cedula_pasaporte)

    actions.move_to_element(NÚMERO_DE_SERVICIO).perform()
    NÚMERO_DE_SERVICIO.send_keys(numero_servicio)

    # Cerrar el controlador
    driver.quit()

# Crear la ventana principal de la aplicación
window = tk.Tk()
window.title('Ingreso de Datos')
window.geometry('400x300')

# Crear etiquetas y campos de entrada para los datos
nombre_completo_label = tk.Label(window, text='Nombre Completo:')
nombre_completo_label.pack()
nombre_completo_entry = tk.Entry(window)
nombre_completo_entry.pack()

cedula_pasaporte_label = tk.Label(window, text='Cédula/Pasaporte:')
cedula_pasaporte_label.pack()
cedula_pasaporte_entry = tk.Entry(window)
cedula_pasaporte_entry.pack()

numero_servicio_label = tk.Label(window, text='Número de Servicio:')
numero_servicio_label.pack()
numero_servicio_entry = tk.Entry(window)
numero_servicio_entry.pack()

# Botón para enviar el formulario
submit_button = tk.Button(window, text='Enviar', command=submit_form)
submit_button.pack()

# Iniciar el bucle de eventos de la ventana
window.mainloop()
 """