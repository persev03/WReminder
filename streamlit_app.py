import streamlit as st
from datetime import datetime, timedelta
import time

class HydrationApp:
    def __init__(self):
        self.intervalo = 0
        self.agua_consumida = 0
        self.tiempo_restante = 0

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

            tiempo_inicial = time.time()
            tiempo_siguiente_recordatorio = tiempo_inicial + self.intervalo * 3600

            # Bucle de recordatorio
            while True:
                tiempo_actual = time.time()
                self.tiempo_restante = int(tiempo_siguiente_recordatorio - tiempo_actual)

                if self.tiempo_restante <= 0:
                    self.mostrar_recordatorio()
                    tiempo_siguiente_recordatorio = tiempo_actual + self.intervalo * 3600

                # Actualizar la interfaz
                st.text("Tiempo restante para el próximo recordatorio: {} segundos".format(self.tiempo_restante))
                time.sleep(1)

        # Botón para registrar el consumo de agua
        if st.button("Registrar Agua"):
            self.registrar_agua()
            st.success("Agua registrada. Total consumido: {} ml".format(self.agua_consumida))


if __name__ == "__main__":
    app = HydrationApp()
    app.run()
