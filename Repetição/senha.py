'''Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário
mostrando
uma mensagem de erro e voltando a pedir as informações'''

usuario = input("entre com o nome de usuario: ")
senha = input("entre com o senha do usuario: ")

while senha == usuario:
    senha = input(
        "erro. a senha não pode ser igual ao nome do usario. insira novamente: ")

print(f"nome de usuario: {usuario}\nsenha: {senha}")
