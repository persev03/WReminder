import streamlit as st
import time
from datetime import datetime, timedelta

# Inicializar variables
hydration_interval = 5  # intervalo de hidratación en segundos
start_time = datetime.now()
water_count = 0

# Configuración de la aplicación
st.title("Recordatorio de Hidratación")

# Configuración del intervalo de hidratación
hydration_interval = st.slider("Selecciona el intervalo de hidratación (segundos)", 3, 10, 3)

# Bucle principal de la aplicación
while True:
    current_time = datetime.now()
    elapsed_time = current_time - start_time

    # Verificar si ha pasado el tiempo de hidratación
    if elapsed_time.seconds % hydration_interval == 0:
        st.info("¡Es hora de hidratarse!")

    # Mostrar contador de agua
    st.text(f"Vasos de agua consumidos hoy: {water_count}")

    # Crear un botón único en cada iteración
    register_button = st.button(f"Registrar vaso de agua ({elapsed_time.seconds})")

    # Verificar si se ha presionado el botón
    if register_button:
        water_count += 1

    # Actualizar la página cada segundo
    time.sleep(1)
