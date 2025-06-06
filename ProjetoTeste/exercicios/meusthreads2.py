from threading import Thread
from time import sleep


def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)

t = Thread(target=vai_demorar, args=('Olá Mundo', 5))
t.start()

for i in range(20):
    print(i)
    sleep(.5)