import pyautogui, webbrowser
from time import sleep

lucia = "+xxxxxxxxx-xxxx"
luca = "+xxxxxxxxx-xxxx"
webbrowser.open('http://web.whatsapp.com/send?phone=+xxxxxxxxxxxxx')

sleep(5)

pyautogui.typewrite("Prueba mensaje automático creado con Python")
pyautogui.press("enter")

""""
with open('message.txt','r') as file:
    for line in file:
        pyautogui.typewrite(line)
        pyautogui.press("enter")


"""

"""
# Importamos el ModuMódulo

import pywhatkit 

# Usamos Un try-except
try: 

  # Enviamos el mensaje

  pywhatkit.sendwhatmsg("+52xxxxxxxxxx",  
                        "Mensaje De Prueba",
                        15,34) 

  print("Mensaje Enviado") 

  

except: 

  print("Ocurrio Un Error")
  """
