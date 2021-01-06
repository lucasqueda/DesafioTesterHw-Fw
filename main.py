import RPi.GPIO as GPIO
import requests
from signal import pause

#configurando os pinos do raspberry
GPIO.setmode(GPIO.BCM)
led = 4
button = 17

GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)



#corpo


url = 'http://192.168.1.110/current_state.xml'


#liga e desliga led
def led_on():
    GPIO.output(led,1)

def led_off():
    GPIO.output(led,0)

#funçao post state do botao

def botao_pressed():
    params1 = {
        'button': 0,
    }
    response = requests.post(url, params=params1)

    if response.led == 0:
        led_on()
    else:
        led_off()

def botao_unpressed():
    params1 = {
        'button': 1,
    }
    response = requests.post(url, params=params1)

    if response.led == 1:
        led_off()
    else:
        led_on()


button.when_pressed = botao_pressed()
button.when_released = botao_unpressed()

pause()