from threading import Thread
from threading import Lock
from time import sleep


class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def compar(self, quantidade):
        self.lock.acquire()
        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            self.lock.release()
            return

        sleep(1)
        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingresso(s). Ainda temos {self.estoque} em estoque.')
        self.lock.release()


if __name__ == '__main__':
    ingressos = Ingressos(10)
    for i in range(1,20):
        t = Thread(target=ingressos.compar(i))
        t.start()

    print(ingressos.estoque)