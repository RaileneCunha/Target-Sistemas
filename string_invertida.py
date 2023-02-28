frase = "Railene é estudante de Análise e Desenvolvimento de Sistemas!"
print(frase[::-1])

# Ou pode ser feito dentro de uma função para ser reutilizada ao longo código.

def inverter(frase):
    return frase[::-1]

print(inverter('Você pode inverter aqui'))
print(inverter('Ou pode inverter aqui, se preferir!'))