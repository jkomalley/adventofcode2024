from collections import Counter

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

    counts = Counter(right)

    sum = 0
    for value in left:
        sum += value * counts[value]
    
    print(sum)

if __name__ == "__main__":
    main()
