#Lynda Levy
#CS175L
#average from input

def main():
    lines = 0
    nums = 0
    file = open('numbers.txt' , 'r')
    for line in file:
        lines += 1
        nums += float(line)
        print(f"I read in {lines} number(s) Current number is:    {float(line):.2f} Total is:    {nums:.2f}")
    print(f"Average: {nums / lines}")
    pass

if __name__ == "__main__":
    main()
