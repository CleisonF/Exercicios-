def recursiva(inicio=0, fim=4):
    if inicio >= fim:
        return fim
    inicio += 1
    return recursiva(inicio,fim)


print(recursiva())
