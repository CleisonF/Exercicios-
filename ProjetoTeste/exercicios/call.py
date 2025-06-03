class Callme:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'Chamando', self.phone)
        return 2134
call1 = Callme('21321213')
retorno = call1('Janbra')
print(retorno)