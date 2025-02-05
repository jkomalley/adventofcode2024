def main():
    with open("input.txt") as input:
        file = input.read()

    total = 0

    for line in file.splitlines():
        safe = True
        report = [int(value) for value in line.split()]

        print(f"{report=}")

        if report[0] < report[1]:
            for i in range(1, len(report) - 1):
                if report[i] > report[i+1]:
                    safe = False
        else:
            for i in range(1, len(report) - 1):
                if report[i] < report[i+1]:
                    safe = False
        
        if safe:
            total += 1

    print(total)


if __name__ == "__main__":
    main()
