import pandas as pd

def main():
    df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    df2 = pd.DataFrame({'A': [5, 6], 'C': [7, 8]})

    print("\n\nDataFrames:\n")
    print("Dataframe 1:")
    print(df1)
    print("\nDataframe 2:")
    print(df2)
    print("-----------------------------------")

    print("Concatenação vertical")
    resultado_v = pd.concat([df1, df2], axis=0)
    print(resultado_v)
    print("-----------------------------------")

    print("Concatenação horizontal")
    resultado_h = pd.concat([df1, df2], axis=1)
    print(resultado_h)
    print("-----------------------------------")

if __name__ == "__main__":
    main()