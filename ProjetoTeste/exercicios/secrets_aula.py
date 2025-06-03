#secrets gera números aleatórios seguros
import secrets
import string
from random import SystemRandom

print(''.join(SystemRandom().choices(string.ascii_letters + string.digits, k=12)))#gerador de senhas protegidas

random = secrets.SystemRandom()

#r_rang = random.randrange(2,8,1)
#print(r_rang)
