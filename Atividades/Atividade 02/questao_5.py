from random import randint
from faker import Faker

fake = Faker('pt_BR')

def alfabetic_order(list: list[tuple]) -> list[tuple]:
    list_sorted = sorted(list) ## função nativa do python
    return list_sorted

def main():
    list = []
    for i in range(1, 10):
        aux = [fake.name(), randint(1, 30)]
        aux1 = tuple(aux)

        list.append(aux1)

    print("Lista de nomes:")
    for i in list:
        print(i)

    print()
    print("Lista ordenada:")
    sorted = alfabetic_order(list)
    for i in sorted:
        print(i)

    

if __name__ == "__main__":
    main()