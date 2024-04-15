#Lynda Levy
#CS175L
#matplotlib

import matplotlib.pyplot as plt
def main():
    labels = []
    sizes = []
    indexNum = []
    try:
        file = open('expenses.txt' , 'r')
        for line in file:
            line = line.strip("\n")
            stuff = line.split("\t")
            if len(stuff) == 2:
                item, number = stuff
                try:
                    sizes.append(int(number))
                except ValueError:
                    sizes.append(str(number))
                    print(f"{number} is a bad value, will not be using.")
                    indexNum.append(sizes.index(number))
                    sizes.remove(number)
                item, number = stuff
                labels.append(item)
        for i in indexNum:
            labels.remove(labels[i])
    except FileNotFoundError:
            print("The file was not found.")
    print(labels)
    print(sizes)
    plt.pie(sizes, labels = labels)
    plt.show()
    
if __name__ == "__main__":
    main()
