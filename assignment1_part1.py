
class ListDivideException(Exception):
    pass

def list_divide(numbers, divide=2):
    count = 0
    for number in numbers:
        if number % divide == 0:
            count += 1
    return count

def test_list_divide():
    try:
        if list_divide([1, 2, 3, 4, 5]) != 2:
            raise ListDivideException("Test 1 failed")
        if list_divide([2, 4, 6, 8, 10]) != 5:
            raise ListDivideException("Test 2 failed")
        if list_divide([30, 54, 63, 98, 100], divide=10) != 2:
            raise ListDivideException("Test 3 failed")
        if list_divide([]) != 0:
            raise ListDivideException("Test 4 failed")
        if list_divide([1, 2, 3, 4, 5], 1) != 5:
            raise ListDivideException("Test 5 failed")
        print("All tests passed!")
    except ListDivideException as e:
        print(f"Error: {e}")

test_list_divide()
