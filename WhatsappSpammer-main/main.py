import pyautogui as pg
import time
import webbrowser as web
phone_no="+58"
parsedMessage=" "
web.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+parsedMessage)
time.sleep(100)
for i in range(25):
    pg.write('prueba')
    pg.press('enter')
    print('Mensaje #'+str(i+1)+' enviado')
    pass
pg.alert('Bomba de mensajes finalizada')
