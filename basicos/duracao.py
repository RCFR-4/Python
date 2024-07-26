duracao_segundos = int(input("entre com a duracao em segundos: "))

horas = duracao_segundos // 3600
restante = duracao_segundos % 3600
minutos = restante // 60
segundos = restante % 60

print(f"{horas}:{minutos}:{segundos}")
