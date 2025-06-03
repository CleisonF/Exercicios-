from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: ...

class NotificacaoEmail(Notificacao):
    def enviar(self):
        print('E-mail: enviando - ', self.mensagem)
        return True

class NotificacaoSMS(Notificacao):
    def enviar(self):
        print('SMS: enviando - ', self.mensagem)
        return False
def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada')
    else:
        print('Notificação não enviada')

notificacao_email = NotificacaoEmail('Testanto e-mail')
notificar(notificacao_email)
notificacao_sms = NotificacaoSMS('Testando sms')
notificar(notificacao_sms)
