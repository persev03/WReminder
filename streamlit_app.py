import tkinter as tk
from tkinter import messagebox
from plyer import notification
from datetime import datetime, timedelta

class HydrationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Recordatorio de Hidratación")
        
        # Variables
        self.intervalo_var = tk.StringVar(value=1)
        self.agua_consumida = 0
        
        # Configuración de la interfaz
        self.configurar_interfaz()

        # Configuración del recordatorio
        self.configurar_recordatorio()

    def configurar_interfaz(self):
        # Etiqueta e input para el intervalo de recordatorio
        tk.Label(self.master, text="Intervalo de recordatorio (horas):").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.master, textvariable=self.intervalo_var, width=5).grid(row=0, column=1, padx=10, pady=10)

        # Botón para iniciar el recordatorio
        tk.Button(self.master, text="Iniciar Recordatorio", command=self.iniciar_recordatorio).grid(row=1, column=0, columnspan=2, pady=10)

        # Etiqueta y contador para el agua consumida
        tk.Label(self.master, text="Agua consumida (ml):").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(self.master, textvariable=self.agua_consumida).grid(row=2, column=1, padx=10, pady=10)

        # Botón para registrar el consumo de agua
        tk.Button(self.master, text="Registrar Agua", command=self.registrar_agua).grid(row=3, column=0, columnspan=2, pady=10)

    def configurar_recordatorio(self):
        self.intervalo = 0  # Se inicializa con 0 para que se configure al iniciar el recordatorio

    def iniciar_recordatorio(self):
        try:
            # Obtener el intervalo desde la entrada del usuario
            intervalo = float(self.intervalo_var.get())
            
            # Configurar el recordatorio
            self.intervalo = timedelta(hours=intervalo)
            
            # Iniciar el bucle de recordatorio
            self.mostrar_recordatorio()
        except ValueError:
            messagebox.showerror("Error", "Ingrese un valor numérico para el intervalo.")

    def mostrar_recordatorio(self):
        # Mostrar notificación
        notification.notify(
            title="¡Hidratación!",
            message="¡Es hora de tomar agua!",
            timeout=10
        )

        # Programar el próximo recordatorio
        self.master.after(int(self.intervalo.total_seconds() * 1000), self.mostrar_recordatorio)

    def registrar_agua(self):
        # Simplemente incrementar el contador de agua consumida
        self.agua_consumida += 250  # Puedes ajustar la cantidad según tus necesidades
        self.actualizar_contador_agua()

    def actualizar_contador_agua(self):
        # Actualizar la etiqueta del contador de agua consumida
        self.agua_consumida.set(self.agua_consumida)


if __name__ == "__main__":
    root = tk.Tk()
    app = HydrationApp(root)
    root.mainloop()

