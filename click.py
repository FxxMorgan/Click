import pyautogui
import time

# Coordenadas de las dos partes en la pantalla
coordenada1 = (739, 612)
coordenada2 = (906, 703)

# Intervalo en segundos
intervalo = 60

# Delay de 3 segundos al inicio
time.sleep(3)

while True:
    # Presionar la primera parte
    pyautogui.click(coordenada1)

    # Presionar la segunda parte
    pyautogui.click(coordenada2)

    # Recargar la página web
    pyautogui.press('f5')

    # Esperar el intervalo
    time.sleep(intervalo)
