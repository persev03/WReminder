<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recordatorio de Hidratación</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 50px;
        }

        #waterCounter {
            font-size: 24px;
            margin-bottom: 20px;
        }

        #configForm {
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <h1>Recordatorio de Hidratación</h1>

    <form id="configForm">
        <label for="interval">Intervalo de recordatorio (minutos): </label>
        <input type="number" id="interval" min="1" value="60">
        <button type="button" onclick="startReminders()">Iniciar Recordatorios</button>
    </form>

    <div id="waterCounter">Agua consumida hoy: 0 ml</div>

    <script>
        let intervalId;
        let waterConsumed = 0;

        function startReminders() {
            const intervalMinutes = parseInt(document.getElementById('interval').value, 10);
            if (intervalId) {
                clearInterval(intervalId);
            }
            intervalId = setInterval(showNotification, intervalMinutes * 60 * 1000);
        }

        function showNotification() {
            // Puedes personalizar la notificación según tus necesidades
            alert('¡Es hora de hidratarse!');
        }

        function recordWaterConsumption() {
            waterConsumed += 250; // Ajusta la cantidad según tus necesidades
            updateWaterCounter();
        }

        function updateWaterCounter() {
            const counterElement = document.getElementById('waterCounter');
            counterElement.textContent = `Agua consumida hoy: ${waterConsumed} ml`;
        }
    </script>
</body>
</html>
