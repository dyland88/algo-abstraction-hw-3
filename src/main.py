from pathlib import Path

def solve_max_subsequence(a: list, b: list, values: dict) -> tuple[int, str]:
    m = len(a)
    n = len(b)

    dp = [[0] * (m + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = values[a[i-1]] + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])


    max_val = dp[n][m]

    subsequence = []
    i, j = n, m
    while i > 0 and j > 0:
        if a[i] == b[j]:
            subsequence.append(a[i])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return max_val, "".join(reversed(subsequence))

def process_file(filepath: Path) -> tuple[str, str, dict[str, int]]:
    with open(filepath) as f:
        values = {}
        alphabet_size = int(f.readline().strip())

        for i in range(alphabet_size):
            letter, value = f.readline().split()
            values[letter] = int(value)

        a = f.readline().strip()
        b = f.readline().strip()

        return a, b, values


if __name__ == "__main__":
    script_dir = Path(__file__).parent
    data_dir = script_dir.parent / "data"
    filepath = data_dir / input("Enter filename: ")
    a, b, values = process_file(filepath)