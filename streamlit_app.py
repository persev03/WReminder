import streamlit as st
from datetime import datetime, timedelta
import time

class HydrationApp:
    def __init__(self):
        self.intervalo = 0
        self.agua_consumida = 0
        self.recordatorio_activado = False
        self.tiempo_siguiente_recordatorio = 0

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
            self.recordatorio_activado = True
            self.tiempo_siguiente_recordatorio = time.time() + self.intervalo * 3600

        # Mostrar el contador regresivo en formato HH:MM:SS
        tiempo_restante = int(max(0, self.tiempo_siguiente_recordatorio - time.time()))
        tiempo_restante_str = "{:02}:{:02}:{:02}".format(
            tiempo_restante // 3600, (tiempo_restante % 3600) // 60, tiempo_restante % 60)
        contador_text = st.empty()
        contador_text.markdown("Tiempo restante para el próximo recordatorio: {}".format(tiempo_restante_str), unsafe_allow_html=True)

        # Actualizar dinámicamente la página con JavaScript
        st.markdown("""
        <script>
        function refresh() {
            setTimeout(function(){
                window.location.reload();
            }, 1000);
        }
        refresh();
        </script>
        """, unsafe_allow_html=True)

        # Mostrar el mensaje de recordatorio cuando llegue el momento
        if tiempo_restante == 0:
            self.mostrar_recordatorio()
            self.tiempo_siguiente_recordatorio = time.time() + self.intervalo * 3600

        # Botón para detener el recordatorio
        if st.button("Detener Recordatorio"):
            self.recordatorio_activado = False
            st.success("Recordatorio detenido.")

        # Botón para registrar el consumo de agua
        if st.button("Registrar Agua"):
            self.registrar_agua()
            st.success("Agua registrada. Total consumido: {} ml".format(self.agua_consumida))


if __name__ == "__main__":
    app = HydrationApp()
    app.run()
