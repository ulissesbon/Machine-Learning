from random import randint

def get_symmetric_difference(list1: list[int], list2: list[int]):
    final: set
    final = set(list1) ^ set(list2)

    return list(final)

def main():
    list_1 = []
    list_2 = []
    
    for i in range(1,30):
        list_1.append(randint(1, 100))

    for i in range(1,30):
        list_2.append(randint(1, 100))
    print("Lista 1:\n", list_1)
    print("Lista 2:\n", list_2)
    print()

    simmetric_difference = get_symmetric_difference(list_1, list_2)
    print("Lista com a Diferença Simétrica:\n")
    print(simmetric_difference)
    print()

if __name__ == "__main__":
    main()