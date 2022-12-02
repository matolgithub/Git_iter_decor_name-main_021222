def test_name_main():
    print(__name__)


def example_iterator(iterable_object="Simple_string!"):
    iterator = iter(iterable_object)
    iter_list = []
    next_element_exist = True
    while next_element_exist:
        try:
            iter_element = next(iterator)
            iter_list.append(iter_element)
            print(iter_list)
        except StopIteration:
            next_element_exist = False


if __name__ == "__main__":
    # test_name_main()
    example_iterator()
else:
    print(f"It is imported module. And the name of import module is: {__name__}.")
