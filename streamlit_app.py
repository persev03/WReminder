import streamlit as st
from datetime import datetime, timedelta
import time

class HydrationApp:
    def __init__(self):
        self.intervalo = 0
        self.agua_consumida = 0

    def mostrar_recordatorio(self):
        st.success("¡Es hora de tomar agua!")

    def registrar_agua(self):
        self.agua_consumida += 250  # Puedes ajustar la cantidad según tus necesidades

    def run(self):
        st.title("Recordatorio de Hidratación")

        # Configurar el recordatorio
        self.intervalo = st.slider("Intervalo de recordatorio (horas):", 0.5, 3.0, 1.0)

        # Botón para iniciar el recordatorio
        if st.button("Iniciar Recordatorio"):
            st.success("Recordatorio iniciado. Puedes cerrar esta pestaña y revisar aquí.")

            # Iniciar el bucle de recordatorio
            while True:
                self.mostrar_recordatorio()
                time.sleep(self.intervalo * 3600)  # Convertir el intervalo a segundos

        # Botón para registrar el consumo de agua
        if st.button("Registrar Agua"):
            self.registrar_agua()
            st.success("Agua registrada. Total consumido: {} ml".f
