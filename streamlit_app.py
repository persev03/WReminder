import streamlit as st
import time
from plyer import notification  # Necesitarás instalar plyer: pip install plyer

def main():
    st.title("Recordatorio de Hidratación")

    # Configuración de recordatorio
    reminder_interval = st.number_input("Configurar recordatorio cada (segundos):", min_value=1, value=1800)

    # Contador de agua
    glasses_consumed = st.number_input("Número de vasos de agua consumidos hoy:", min_value=0)

    # Botón para registrar consumo
    if st.button("Registrar vaso de agua"):
        glasses_consumed += 1

    st.write(f"Vasos de agua consumidos hoy: {glasses_consumed}")

    # Iniciar el temporizador de recordatorio
    start_reminder(reminder_interval)

def start_reminder(interval):
    while True:
        time.sleep(interval)
        show_notification("Hidratación", "¡Es hora de tomar agua!")

def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,  # Puedes proporcionar el path a un icono personalizado
        timeout=10,  # Tiempo en segundos para que la notificación desaparezca
    )

if __name__ == "__main__":
    main()
