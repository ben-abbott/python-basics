def assert_equals(val_1, val_2) -> bool:  # -> helps with documentation
    return val_1 == val_2


def assert_true(value) -> bool:
    return bool(value)


def assert_greater_than(val_1: int, val_2: int) -> bool:
    if not isinstance(val_1, int) or not isinstance(val_2, int):
        raise TypeError("At least one value is not and integer")
    return val_1 > val_2


# print(f'Are 2 and 2 equal? {assert_equals(2, 2)}')
# print(f'Are true and false equal? {assert_equals(True, False)}')
# print(f'Are same lists equal? {assert_equals(['one', 2], ['one', 2])}')
# print(f'Are 2 and 2.0 equal? {assert_equals(2, 2.0)}')
# print(f'Are type(2) and type(2.0) equal? {assert_equals(type(2), type(2.0))}')
# print(f'Are 0 and False equal? {assert_equals(0, False)}')
# print(f'Are \'\' and False equal? {assert_equals('', False)}')
# print(f'Are bool(\'\') and False equal? {assert_equals(bool(''), False)}')

print(f'Is 2 == 2 true? {assert_true(2 == 2)}')

print(f'is 20 greater than 10? {assert_greater_than(20, 10)}')

print(f'Is hello greater than 10? {assert_greater_than('hello', 10)}')
