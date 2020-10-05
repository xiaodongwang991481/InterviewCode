import sys


def main(argv, expected):
    for index, arg in enumerate(argv):
        if arg == expected:
            print(f"found {expected} in index {index}")
            break
    else:
        print(f"not found {expected}")

if __name__ == "__main__":
    # execute only if run as a script
    main([6, 4, 7, 2], 10)