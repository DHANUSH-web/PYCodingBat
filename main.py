from dataclasses import dataclass
import requests
import unittest


def concat(a: str, b: str) -> str:
    a_size: int = len(a)
    b_size: int = len(b)

    if a_size == 0:
        return b
    if b_size == 0:
        return a

    return a + b[1:] if a[-1] == b[0] else a + b


def last_two(data: str) -> str:
    if len(data) < 2:
        return ""
    return data[:-2] + data[:-3:-1] if len(data) > 2 else data[::-1]


def see_colors(data: str) -> str:
    if data.startswith("red"):
        return "red"
    elif data.startswith("blue"):
        return "blue"

    return ""


def front_again(data: str) -> bool:
    size: int = len(data)
    return size >= 2 and data[0] == data[size-2] and data[1] == data[size-1]


def min_cat(a: str, b: str) -> str:
    a_size = len(a)
    b_size = len(b)

    if a_size == b_size:
        return a + b

    return a[a_size-b_size:] + b if a_size > b_size else a + b[b_size-a_size:]


def extra_front(data: str) -> str:
    return data * 3 if len(data) < 2 else data[0:2]*3


def near10(num: int) -> bool:
    return num % 10 <= 2 or num % 10 >= 8


def tea_party(tea: int, candy: int) -> int:
    if tea < 5 or candy < 5:
        return 0
    elif tea >= candy*2 or candy >= tea*2:
        return 2
    return 1


def fizz_string(data: str) -> str:
    if data.startswith('f') and data.endswith('b'):
        return "FizzBuzz"
    elif data.startswith('f'):
        return "Fizz"
    elif data.endswith('b'):
        return "Buzz"
    return data


def fizz_string2(n: int) -> str:
    if not n % 3 and not n % 5:
        return "FizzBuzz!"
    if not n % 3:
        return "Fizz!"
    if not n % 5:
        return "Buzz!"
    
    return f"{n}!"


def two_as_one(a: int, b: int, c: int) -> bool:
    return a + b == c or a + c == b or b + c == a


def in_order(a: int, b: int, c: int, b_ok: bool) -> bool:
    return (b_ok or b > a) and c > b


def in_order_equal(a: int, b: int, c: int, equal_ok: bool) -> bool:
    return (equal_ok and a <= b <= c) or (a < b < c)


@dataclass
class JsonDataProps:
    userId: int
    id: int
    title: str
    completed: bool


def fetch_json_data(url: str, params: dict | None = None) -> JsonDataProps:
    response: requests.Response = requests.get(url=url, params=params)

    if response.status_code != 200:
        raise requests.HTTPError(f"Failed to fetch {url}, status code: {response.status_code}")
    
    data: dict = response.json()
    return JsonDataProps(
        userId=data['userId'],
        id=data['id'],
        title=data['title'],
        completed=data['completed'],
    )


def lastDigit(a: int, b: int, c: int) -> bool:
    return a % 10 == b % 10 or a % 10 == c % 10 or b % 10 == c % 10


def lessBy10(a: int, b: int, c: int) -> bool:
    return abs(a - b) >= 10 or abs(a - c) >= 10 or abs(b - c) >= 10


def withoutDoubles(die1: int, die2: int, no_doubles: bool) -> int:
    if no_doubles and die1 == die2:
        die1 = 1 if die1 == 6 else die1 + 1
    return die1 + die2


def maxMod5(a: int, b: int) -> int:
    if a == b:
        return 0
    
    if a % 5 == b % 5:
        return min(a, b)
    
    return max(a, b)


def redTicket(a: int, b: int, c: int) -> int:
    if a == b == c == 2:
        return 10
    
    if a == b == c:
        return 5
    
    if a != b and a != c:
        return 1
    
    return 0


def greenTicket(a: int, b: int, c: int) -> int:
    if a == b == c:
        return 20
    
    if a == b or a == c or b == c:
        return 10
    
    return 0


def shareDigit(a: int, b: int) -> bool:
    return a // 10 == b // 10 or a // 10 == b % 10 or a % 10 == b // 10 or a % 10 == b % 10


def fact(n: int) -> int:
    return 1 if n <= 1 else n * fact(n - 1)


def sum13(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    
    if nums[0] == 13:
        return 0

    return nums[0] + sum13(nums[1:])


def centeredAverage(nums: list[int]) -> int:
    sum, _min, _max = 0, nums[0], nums[0]
    
    for i in range(len(nums)):
        sum += nums[i]
        
        if nums[i] < _min:
            _min = nums[i]
        
        if nums[i] > _max:
            _max = nums[i]

    return (sum - _min - _max) // (len(nums) - 2)


def sum67(nums: list[int]) -> int:
    total = 0
    skip = False

    for n in nums:
        if n == 6:
            skip = True
        elif n == 7 and skip:
            skip = False
        elif not skip:
            total += n
    
    return total


def has22(nums: list[int]) -> bool:
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1] == 2:
            return True
    return False


def lucky13(nums: list[int]) -> bool:
    for n in nums:
        if n == 1 or n == 3:
            return False
    return True


def sum28(nums: list[int]) -> bool:
    total = 0

    for n in nums:
        if n == 2:
            total += n
    
    return total == 8


def more14(nums: list[int]) -> bool:
    count = 0

    for n in nums:
        if n == 1:
            count += 1
        if n == 4:
            count -= 1
    
    return count > 0


def fizzArray(n: int) -> list[int]:
    arr: list[int] = []

    for i in range(n):
        arr.append(i)
    
    return arr


def only14(nums: list[int]) -> bool:
    for n in nums:
        if n != 1 and n != 4:
            return False
    return True


def fizzArray2(n: int) -> list[str]:
    arr: list[str] = []

    for i in range(n):
        arr.append(str(i))
    
    return arr


def no14(nums: list[int]) -> bool:
    has1, has4 = False, False

    for n in nums:
        if n == 1:
            has1 = True
        if n == 4:
            has4 = True
        
        if has1 and has4:
            return False
    
    return not(has1 and has4)


def isEverywhere(nums: list[int], val: int) -> bool:
    for i in range(len(nums) - 1):
        if nums[i] != val and nums[i+1] != val:
            return False
    
    return True


def either24(nums: list[int]) -> bool:
    is2, is4 = False, False

    for i in range(len(nums)-1):
        if is2 and is4:
            break

        if nums[i] == 2 and nums[i+1] == 2:
            is2 = True

        if nums[i] == 4 and nums[i+1] == 4:
            is4 = True

    return is2 != is4


def matchUp(nums1: list[int], nums2: list[int]) -> int:
    count: int = 0

    for i in range(len(nums1)):
        if nums1[i] != nums2[i] and abs(nums1[i] - nums2[i]) <= 2:
            count += 1
    
    return count


def has77(nums: list[int]) -> bool:
    for i in range(0, len(nums)-2):
        if (nums[i] == 7 and (nums[i+1] == 7 or nums[i+2] == 7)) or (nums[i+1] == 7 and nums[i+2] == 7):
            return True
    return False


def has12(nums: list[int]) -> bool:
    found = False

    for n in nums:
        if n == 1 and not found:
            found = True
        if n == 2 and found:
            return True
    return False


if __name__ == "__main__":
    # print("Run test cases with `uv run python unittest -v`")
    print("Running unit tests...")
    # os.system("uv run python -m unittest -v")
    tests = unittest.TestLoader().discover(start_dir="tests", pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(tests)
