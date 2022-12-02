import iterator

print("---------------------------")
print(f"Local name is: {__name__}.")
print("---------------------------")

func_counts = 0


def decorator(func):
    def wrapper(*args, **kwargs):
        global func_counts
        func()
        func_counts += 1
        # print(func_counts)

        return func_counts

    return wrapper


@decorator
def fu():
    return func_counts


if __name__ == "__main__":
    for _ in range(100):
        fu()
    print(f"The function called {func_counts} times.")
