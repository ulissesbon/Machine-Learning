from random import randint

def find_second_greater(list: list[int]):
    greater = 0

    for i in list:
        if i > greater:
            greater = i
    
    aux = 0
    for i in list:
        if i != greater and aux < i:
            aux = i
    
    return aux

def main():
    list_1 = []
    
    for i in range(1,30):
        list_1.append(randint(1, 100))

    print()
    print("Lista:")
    print(list_1)
    print()
    print("Segundo maior numero da lista: ", find_second_greater(list_1))
    print()


if __name__ == "__main__":
    main()