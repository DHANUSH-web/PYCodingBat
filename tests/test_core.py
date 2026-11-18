import unittest
from lib.core import (
    concat,
    last_two,
    not_alone,
    see_colors,
    front_again,
    min_cat,
    extra_front,
    near10,
    tea_party,
    fizz_string,
    fizz_string2,
    two_as_one,
    in_order,
    in_order_equal,
    JsonDataProps,
    fetch_json_data,
    last_digit,
    less_by10,
    without_doubles,
    max_mod5,
    red_ticket,
    green_ticket,
    share_digit,
    sum13,
    centered_average,
    sum67,
    has22,
    lucky13,
    sum28,
    more14,
    fizz_array,
    only14,
    fizz_array2,
    no14,
    is_everywhere,
    either24,
    match_up,
    has77,
    has12,
    mod_three,
    have_three,
    two_two,
    same_ends,
    triple_up,
    fizz_array3,
    shift_left,
    pre4,
    post4,
)


class TestCore(unittest.TestCase):

    def test_concat(self):
        self.assertEqual(concat("abc", "cat"), "abcat")
        self.assertEqual(concat("dog", "cat"), "dogcat")
        self.assertEqual(concat("abc", ""), "abc")

    def test_lastTwo(self):
        self.assertEqual(last_two("coding"), "codign")
        self.assertEqual(last_two("cat"), "cta")
        self.assertEqual(last_two("ab"), "ba")

    def test_seeColors(self):
        self.assertEqual(see_colors("redxx"), "red")
        self.assertEqual(see_colors("xxred"), "")
        self.assertEqual(see_colors("blueTimes"), "blue")

    def test_frontAgain(self):
        self.assertTrue(front_again("edited"))
        self.assertFalse(front_again("edit"))
        self.assertTrue(front_again("ed"))

    def test_minCat(self):
        self.assertEqual(min_cat("Hello", "Hi"), "loHi")
        self.assertEqual(min_cat("Hello", "java"), "ellojava")
        self.assertEqual(min_cat("java", "Hello"), "javaello")

    def test_extraFront(self):
        self.assertEqual(extra_front("Hello"), "HeHeHe")
        self.assertEqual(extra_front("ab"), "ababab")
        self.assertEqual(extra_front("H"), "HHH")

    def test_near10(self):
        self.assertTrue(near10(12))
        self.assertFalse(near10(17))
        self.assertTrue(near10(19))

    def test_teaParty(self):
        self.assertEqual(tea_party(6, 8), 1)
        self.assertEqual(tea_party(3, 8), 0)
        self.assertEqual(tea_party(20, 6), 2)

    def test_fizzString(self):
        self.assertEqual(fizz_string("fig"), "Fizz")
        self.assertEqual(fizz_string("dib"), "Buzz")
        self.assertEqual(fizz_string("fib"), "FizzBuzz")
        self.assertEqual(fizz_string("none"), "none")

    def test_fizzString2(self):
        self.assertEqual(fizz_string2(1), "1!")
        self.assertEqual(fizz_string2(2), "2!")
        self.assertEqual(fizz_string2(3), "Fizz!")
        self.assertEqual(fizz_string2(5), "Buzz!")
        self.assertEqual(fizz_string2(15), "FizzBuzz!")

    def test_twoAsOne(self):
        self.assertTrue(two_as_one(1, 2, 3))
        self.assertTrue(two_as_one(3, 1, 2))
        self.assertFalse(two_as_one(3, 2, 2))

    def test_inOrder(self):
        self.assertTrue(in_order(1, 2, 4, False))
        self.assertFalse(in_order(1, 2, 1, False))
        self.assertTrue(in_order(1, 1, 2, True))

    def test_inOrderEqual(self):
        self.assertTrue(in_order_equal(2, 5, 11, False), True)
        self.assertFalse(in_order_equal(5, 7, 6, False), False)
        self.assertTrue(in_order_equal(5, 5, 7, True), True)

    def test_fetchJsonResponse(self):
        url: str = "https://jsonplaceholder.typicode.com/todos/1"
        data: JsonDataProps = fetch_json_data(url=url)

        self.assertEqual(data.userId, 1)
        self.assertEqual(data.id, 1)
        self.assertEqual(data.title, "delectus aut autem")
        self.assertFalse(data.completed)

    def test_lastDigit(self):
        self.assertTrue(last_digit(23, 19, 13))
        self.assertFalse(last_digit(23, 19, 20))
        self.assertTrue(last_digit(23, 19, 3))

    def test_lessBy10(self):
        self.assertTrue(less_by10(1, 2, 11))
        self.assertFalse(less_by10(3, 2, 11))
        self.assertTrue(less_by10(10, 1, 11))

    def test_withoutDoubles(self):
        self.assertEqual(without_doubles(2, 3, True), 5)
        self.assertEqual(without_doubles(3, 3, True), 7)
        self.assertEqual(without_doubles(3, 3, False), 6)

    def test_maxMod5(self):
        self.assertEqual(max_mod5(2, 3), 3)
        self.assertEqual(max_mod5(6, 2), 6)
        self.assertEqual(max_mod5(3, 2), 3)

    def test_redTicket(self):
        self.assertEqual(red_ticket(2, 2, 2), 10)
        self.assertEqual(red_ticket(2, 2, 1), 0)
        self.assertEqual(red_ticket(0, 0, 0), 5)

    def test_greenTicket(self):
        self.assertEqual(green_ticket(1, 2, 3), 0)
        self.assertEqual(green_ticket(2, 2, 2), 20)
        self.assertEqual(green_ticket(1, 1, 2), 10)

    def test_shareDigit(self):
        self.assertTrue(share_digit(12, 23))
        self.assertFalse(share_digit(12, 43))
        self.assertFalse(share_digit(12, 44))

    def test_sum13(self):
        self.assertEqual(sum13([1, 2, 2, 1]), 6)
        self.assertEqual(sum13([1, 1]), 2)
        self.assertEqual(sum13([1, 2, 2, 1, 13]), 6)

    def test_centeredAverage(self):
        self.assertEqual(centered_average([1, 2, 3, 4, 100]), 3)
        self.assertEqual(centered_average([1, 1, 5, 5, 10, 8, 7]), 5)
        self.assertEqual(centered_average([-10, -4, -2, -4, -2, 0]), -3)

    def test_sum67(self):
        self.assertEqual(sum67([1, 2, 2]), 5)
        self.assertEqual(sum67([1, 2, 2, 6, 99, 99, 7]), 5)
        self.assertEqual(sum67([1, 1, 6, 7, 2]), 4)
        self.assertEqual(sum67([6, 7, 2]), 2)
        self.assertEqual(sum67([1, 6, 7, 6, 7]), 1)
        self.assertEqual(sum67([1, 6, 7, 2, 6, 99, 7]), 3)
        self.assertEqual(sum67([1, 6, 99, 7, 7]), 8)
        self.assertEqual(sum67([6, 7, 7]), 7)

    def test_has22(self):
        self.assertTrue(has22([1, 2, 2]))
        self.assertFalse(has22([1, 2, 1, 2]))
        self.assertFalse(has22([1, 1, 2]))

    def test_lucky13(self):
        self.assertTrue(lucky13([0, 2, 4]))
        self.assertFalse(lucky13([1, 2, 3]))
        self.assertFalse(lucky13([1, 2, 4]))

    def test_sum28(self):
        self.assertTrue(sum28([2, 3, 2, 2, 4, 2]))
        self.assertFalse(sum28([2, 3, 2, 2, 4, 2, 2]))
        self.assertFalse(sum28([1, 2, 3, 4]))

    def test_more14(self):
        self.assertTrue(more14([1, 4, 1]))
        self.assertFalse(more14([1, 4, 1, 4]))
        self.assertTrue(more14([1, 1]))

    def test_fizzArray(self):
        self.assertEqual(fizz_array(4), [0, 1, 2, 3])
        self.assertEqual(fizz_array(1), [0])
        self.assertEqual(fizz_array(10), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_only14(self):
        self.assertTrue(only14([1, 4, 1, 4]))
        self.assertFalse(only14([1, 4, 2, 4]))
        self.assertTrue(only14([1, 1]))

    def test_fizzArray2(self):
        self.assertEqual(fizz_array2(4), ['0', '1', '2', '3'])
        self.assertEqual(fizz_array2(1), ['0'])
        self.assertEqual(fizz_array2(10), ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

    def test_no14(self):
        self.assertTrue(no14([1, 2, 3]))
        self.assertFalse(no14([1, 2, 3, 4]))
        self.assertTrue(no14([2, 3, 4]))

    def test_isEverywhere(self):
        self.assertTrue(is_everywhere([1, 2, 1, 3], 1))
        self.assertFalse(is_everywhere([1, 2, 1, 3], 2))
        self.assertFalse(is_everywhere([1, 2, 1, 3, 4], 1))

    def test_either24(self):
        self.assertTrue(either24([1, 2, 2]))
        self.assertTrue(either24([4, 4, 1]))
        self.assertFalse(either24([4, 4, 1, 2, 2]))

    def test_matchUp(self):
        self.assertEqual(match_up([1, 2, 3], [2, 3, 10]), 2)
        self.assertEqual(match_up([1, 2, 3], [2, 3, 5]), 3)
        self.assertEqual(match_up([1, 2, 3], [2, 3, 3]), 2)

    def test_has77(self):
        self.assertTrue(has77([1, 7, 7]))
        self.assertTrue(has77([1, 7, 1, 7]))
        self.assertFalse(has77([1, 7, 1, 1, 7]))

    def test_has12(self):
        self.assertTrue(has12([1, 3, 2]))
        self.assertTrue(has12([1, 7, 2, 7]))
        self.assertTrue(has12([1, 7, 1, 1, 2]))
        self.assertFalse(has12([1]))

    def test_mod_three(self):
        self.assertTrue(mod_three([2, 1, 3, 5]))
        self.assertFalse(mod_three([2, 1, 2, 5]))
        self.assertTrue(mod_three([2, 4, 2, 5]))

    def test_have_three(self):
        self.assertTrue(have_three([3, 1, 3, 1, 3]))
        self.assertFalse(have_three([3, 1, 3, 3]))
        self.assertFalse(have_three([3, 4, 3, 3, 4]))

    def test_two_two(self):
        self.assertTrue(two_two([4, 2, 2, 3]))
        self.assertTrue(two_two([2, 2, 4]))
        self.assertFalse(two_two([2, 2, 4, 2]))

    def test_same_ends(self):
        self.assertFalse(same_ends([5, 6, 45, 99, 13, 5, 6], 1))
        self.assertTrue(same_ends([5, 6, 45, 99, 13, 5, 6], 2))
        self.assertFalse(same_ends([5, 6, 45, 99, 13, 5, 6], 3))

    def test_triple_up(self):
        self.assertTrue(triple_up([1, 4, 5, 6, 2]))
        self.assertTrue(triple_up([1, 2, 3]))
        self.assertFalse(triple_up([1, 2, 5]))

    def test_fizz_array3(self):
        self.assertEqual(fizz_array3(5, 10), [5, 6, 7, 8, 9])
        self.assertEqual(fizz_array3(11, 18), [11, 12, 13, 14, 15, 16, 17])
        self.assertEqual(fizz_array3(1, 3), [1, 2])

    def test_shift_left(self):
        self.assertEqual(shift_left([5, 1, 2, 3, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(shift_left([1, 2]), [2, 1])
        self.assertEqual(shift_left([1]), [1])

    def test_pre4(self):
        self.assertEqual(pre4([1, 2, 4, 1]), [1, 2])
        self.assertEqual(pre4([3, 1, 4]), [3, 1])
        self.assertEqual(pre4([1, 4, 4]), [1])

    def test_post4(self):
        self.assertEqual(post4([2, 4, 1, 2]), [1, 2])
        self.assertEqual(post4([4, 1, 4, 2]), [2])
        self.assertEqual(post4([4, 4, 1, 2, 3]), [1, 2, 3])

    def test_not_alone(self):
        self.assertEqual(not_alone([1, 2, 3], 2), [1, 3, 3])
        self.assertEqual(not_alone([1, 2, 3, 2, 5, 2], 2), [1, 3, 3, 5, 5, 2])
        self.assertEqual(not_alone([3, 4], 3), [3, 4])
