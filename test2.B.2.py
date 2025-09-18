def rolling_mean(xs, w):
    if w <= 0 or w > len(xs):
        raise ValueError("Invalid window size")
    sums = []
    for i in range(len(xs) - w + 1):
        window = xs[i:i+w]
        sums.append(sum(window) / w)
    return sums


if __name__ == "__main__":
    # Take input list from user
    xs = list(map(int, input("Enter numbers separated by spaces: ").split()))
    w = int(input("Enter window size: "))

    try:
        result = rolling_mean(xs, w)
        print("Rolling mean values:", result)
    except ValueError as e:
        print("Error:", e)
