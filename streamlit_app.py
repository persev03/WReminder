import streamlit as st
from plyer import notification
from datetime import datetime, timedelta

class HydrationApp:
    def __init__(self):
        self.intervalo = 0
        self.agua_consumida = 0

    def mostrar_recordatorio(self):
        notification.notify(
            title="¡Hidratación!",
            message="¡Es hora de tomar agua!",
            timeout=10
        )

    def registrar_agua(self):
        self.agua_consumida += 250  # Puedes ajustar la cantidad según tus necesidades

    def run(self):
        st.title("Recordatorio de Hidratación")

        # Configurar el recordatorio
        self.intervalo = st.slider("Intervalo de recordatorio (horas):", 0.5, 3.0, 1.0)

        # Botón para iniciar el recordatorio
        if st.button("Iniciar Recordatorio"):
            st.success("Recordatorio iniciado. Puedes cerrar esta pestaña y recibirás notificaciones.")

            # Iniciar el bucle de recordatorio
            while True:
                self.mostrar_recordatorio()
                st.empty()  # Esto evita que la aplicación se bloquee debido al bucle infinito

        # Botón para registrar el consumo de agua
        if st.button("Registrar Agua"):
            self.registrar_agua()
            st.success("Agua registrada. Total consumido: {} ml".format(self.agua_consumida))


if __name__ == "__main__":
    app = HydrationApp()
    app.run()
