def main():
    with open("input.txt") as input:
        file = input.read()
    
    left = []
    right = []

    for line in file.splitlines():
        first, second = line.split()
        left.append(int(first))
        right.append(int(second))
    
    left.sort()
    right.sort()

    sum = 0
    for first, second in zip(left, right):
        sum += abs(first - second)
    
    print(sum)

if __name__ == "__main__":
    main()
