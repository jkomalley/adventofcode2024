from pathlib import Path
from itertools import combinations


def _inc_within_diff(report: list[int]):
    return all(
        report[i] <= report[i + 1] and 1 <= report[i + 1] - report[i] <= 3
        for i in range(len(report) - 1)
    )


def _dec_within_diff(report: list[int]):
    return all(
        report[i] >= report[i + 1] and 1 <= report[i] - report[i + 1] <= 3
        for i in range(len(report) - 1)
    )


def _is_safe(report: list[int]):
    return _inc_within_diff(report) or _dec_within_diff(report)


def main():
    input_path = Path("input.txt")
    safe_count = 0

    with input_path.open() as input_file:
        for line in input_file.readlines():
            report = [int(level) for level in line.split()]

            is_safe = _is_safe(report)

            print(f"{report=} {is_safe=}")

            if is_safe:
                safe_count += 1
            else:
                for perm in combinations(report, len(report) - 1):
                    is_safe = _is_safe(perm)

                    if is_safe:
                        safe_count += 1
                        break

    print(f"{safe_count=}")


if __name__ == "__main__":
    main()
