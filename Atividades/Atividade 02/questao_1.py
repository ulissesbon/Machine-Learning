from random import randint

def get_odds(list: list):
    odds = []
    for i in list:
        if i % 2 != 0:
            odds.append(i)

    return odds

def main():
    list = []
    
    for i in range(1,30):
        list.append(randint(1, 100))
    print("Lista:\n")
    print(list)
    print()

    odd_list = get_odds(list)
    print("Lista apenas com os ímpares:\n")
    print(odd_list)
    print()

if __name__ == "__main__":
    main()