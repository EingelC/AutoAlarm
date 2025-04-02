import winsound
import pyautogui
import time
import numpy as np
from PIL import Image
import keyboard
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

Turno = False

def find_color_in_region(color, region, palabra):
    global Turno
    screenshot = pyautogui.screenshot(region=region)
    screenshot_np = np.array(screenshot)
    target_color = np.array(color)
    result = np.where(np.all(screenshot_np[:,:,:3] == target_color,axis=2))
    texto_extraido = pytesseract.image_to_string(screenshot)
    if palabra.lower() in texto_extraido.lower():
        print(f"Lo encontré")
        Turno = True
    if len(result[0]) > 0:
        return result[1][0], result[0][0]
    else:
        return None

region = (0, 700, 500, 1080)
color = (244, 67, 54)
palabra = "uri.gomez" #Turno anterior antes del propio

while True:
    time.sleep(0.3)  # Esperar 0.3 segundos
    position = find_color_in_region(color, region, palabra)

    if position:
        if Turno == True:
            print(f"ALERTA EN: {position}")
            winsound.Beep(1000, 200)  # Frecuencia de 1000 Hz durante 500 ms     
    else:
        print("ESPERANDO...")
        Turno = False

    if keyboard.is_pressed('F1'):
        print("F1 presionado, saliendo del programa.")
        break
