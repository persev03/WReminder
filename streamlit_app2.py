import streamlit as st
import datetime
import time
import threading

# Definir variables globales
current_time = datetime.datetime.now()
reminder_interval = 60  # Minutos
water_count = 0

# Código para la interfaz de usuario de Streamlit

st.title("Recordatorios de hidratación")

# Intervalo de recordatorios
intervalo_recordatorios = st.slider("Intervalo de recordatorios (minutos)", 1, 60, 60)

# Botón para configurar los recordatorios
if st.button("Configurar recordatorios"):
    # Actualizar el intervalo de recordatorios
    reminder_interval = intervalo_recordatorios

    # Configurar los recordatorios
    def set_reminders():
        global current_time
        global reminder_interval

        # Obtener la hora del siguiente recordatorio
        next_reminder = current_time + datetime.timedelta(minutes=reminder_interval)

        # Iniciar un hilo para mostrar la alerta
        threading.Timer(next_reminder - current_time, show_reminder).start()

    set_reminders()

# Contador de agua
st.write("Vasos de agua consumidos hoy:", water_count)

# Botón para aumentar el contador de agua
if st.button("Beber un vaso de agua"):
    # Actualizar el contador de agua
    water_count += 1

    # Configurar los recordatorios
    set_reminders()

# Función para mostrar la alerta
def show_reminder():
    global water_count

    # Mostrar la alerta
    st.write(f"¡Es hora de hidratarse! Llevas {water_count} vasos de agua consumidos hoy.")

    # Actualizar el contador de agua
    water_count += 1

    # Configurar el siguiente recordatorio
    set_reminders()
