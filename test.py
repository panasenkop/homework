from time import time
from main import *


def test_min_elem():
    assert min_elem([4, 3, 1, 2]) == 1
    print("Test min_elem passed")


def test_max_elem():
    assert max_elem([3, 4, 1, 2]) == 4
    print("Test max_elem passed")


def test_get_sum():
    assert get_sum([3, 1, 2, 4]) == 10
    print("Test get_sum passed")


def test_get_prod():
    assert get_prod([4, 3, 2, 1]) == 24
    print("Test get_prod passed")


def test_speed():
    with open("input.txt", "w") as f:
        f.write("999 " * 10000)
    t = time()
    main()
    print("Time needed", time() - t)


def test_read():
    with open("input.txt", "w") as f:
        f.write("1 5 4 3 2")
    assert read() == [1, 5, 4, 3, 2]
    print("Read test passed")


def test():
    test_min_elem()
    test_max_elem()
    test_get_sum()
    test_get_prod()
    test_speed()
    test_read()
    print("All test are passed")


if __name__ == '__main__':
    test()
