def min_elem(lst):
    res = lst[0]
    for i in range(lst):
        if lst[i] < res:
            res = lst[i]
    return res


def max_elem(lst):
    res = lst[0]
    for i in range(lst):
        if lst[i] > res:
            res = lst[i]
    return res


def get_sum(lst):
    res = 0
    for i in range(lst):
        try:
            res += lst[i]
        except OverflowError:
            return
    return res


def get_prod(lst):
    res = 1
    for i in range(lst):
        try:
            res *= lst[i]
        except OverflowError:
            return
    return res


def main():
    with open("input.txt", "r") as f:
        lst = list(map(int, f.readline().split()))

    min = min_elem(lst)
    max = max_elem(lst)
    sum = get_sum(lst)
    prod = get_prod(lst)

    print("Minimum elem:", min)
    print("Maximum elem:", max)
    print("Sum:", sum)
    print("Product:", prod)


if __name__ == '__main__':
    main()