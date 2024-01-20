import streamlit as st
import datetime
import time

# Inicializamos el contador de agua
contador_agua = 0

# Función para mostrar la alerta de hidratación
def mostrar_alerta():
    st.warning("¡Es hora de hidratarse!")

# Función principal de la aplicación
def main():
    global contador_agua

    st.title("Recordatorio de Hidratación")

    # Configuración de recordatorio
    hora_recordatorio = st.time_input("Selecciona la hora del recordatorio:", datetime.time(8, 0))
    recordatorio_intervalo = st.slider("Intervalo de recordatorio (minutos):", 10, 120, 30)

    # Configuración del contador de agua
    st.header("Contador de Agua")
    contador_agua_hoy = st.empty()

    # Verificar si es hora de mostrar la alerta
    while True:
        now = datetime.datetime.now().time()
        if now >= hora_recordatorio:
            mostrar_alerta()
            time.sleep(60 * recordatorio_intervalo)  # Esperar hasta el próximo recordatorio
        else:
            time.sleep(60)  # Esperar un minuto antes de verificar nuevamente

        # Actualizar el contador de agua (simulado con un botón)
        if st.button("Registrar vaso de agua"):
            contador_agua += 1

        # Mostrar el contador actualizado
        contador_agua_hoy.text(f"Vasos de agua hoy: {contador_agua}")

# Ejecutar la aplicación
if __name__ == "__main__":
    main()
