agendas = [
    {"nome": "André", "telefone":"94563332", "cidade":"Lisboa"},
    {"nome": "Rui", "telefone":"91377337", "cidade":"Sintra"},
    {"nome": "Paulo", "telefone":"92563352", "cidade":"Cascais"}
]

def contactos(lista):
    for agenda in lista:
        print(f"{agenda['nome']} - {agenda['telefone']} - {agenda['cidade']} ")


def pesquisa(lista,nome):
    for agenda in lista:
        if agenda ["nome"] == nome:
            print(f"O {nome} na agenda está associado ao número: {agenda['telefone']} e á cidade de:  {agenda['cidade']}")
            break
    else:
        print(f"O {nome} não se encontra na agenda")
    


contactos(agendas)

pesquisa_utilizador = input("Qual é o nome que procuras? ")

pesquisa(agendas,pesquisa_utilizador)