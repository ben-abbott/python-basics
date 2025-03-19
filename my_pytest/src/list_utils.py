def count_even_numbers(list_input: list[int]) -> int:
    return len(
        [number for number in list_input if number % 2 == 0]
    )
