#Lynda Levy
#CS175L
#average from input

def main():
    lines = 0
    nums = 0
    file = open('numbers.txt' , 'r')
    try:
        for line in file:
            try:
                nums += int(line)
                lines += 1
                print(f'I read in {lines} number(s) Current number is: {float(line):.2f} Total is: {nums:.2f}')
            except ValueError:
                print(f'Bad data: {line.strip()} skipping')
        print(f'Average: {(nums / lines)}')
    except IOError:
        print("File not found: numbers.txt - exiting")

if __name__ == "__main__":
    main()
