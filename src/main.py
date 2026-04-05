from pathlib import Path

def solve_max_subsequence(a: str, b: str, values: dict) -> tuple[int, str]:
    m = len(b)
    n = len(a)

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
        if a[i-1] == b[j-1]:
            subsequence.append(a[i-1])
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
    # commented out code was used to create the output files programmatically
    # for i in list(range(1, 11)) + ["example"]:
        script_dir = Path(__file__).parent
        data_dir = script_dir.parent / "data"
        filepath = data_dir / input("Enter filename: ")
        # filepath = data_dir / f"../data/{i}.in"
        a, b, values = process_file(filepath)
        (max_val, subsequence) = solve_max_subsequence(a, b, values)
        output_path = data_dir / f"{i}.out"

        print(f"Max value: {max_val}\n")
        print(f"Subsequence: {subsequence}\n")
        # with open(output_path, "w", encoding="utf-8") as f:
        #     f.write(f"Max value: {max_val}\n")
        #     f.write(f"Subsequence: {subsequence}\n")