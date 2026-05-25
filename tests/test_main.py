import unittest
from main import *

class TestMain(unittest.TestCase):

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
        self.assertTrue(lastDigit(23, 19, 13))
        self.assertFalse(lastDigit(23, 19, 20))
        self.assertTrue(lastDigit(23, 19, 3))

    def test_lessBy10(self):
        self.assertTrue(lessBy10(1, 2, 11))
        self.assertFalse(lessBy10(3, 2, 11))
        self.assertTrue(lessBy10(10, 1, 11))

    def test_withoutDoubles(self):
        self.assertEqual(withoutDoubles(2, 3, True), 5)
        self.assertEqual(withoutDoubles(3, 3, True), 7)
        self.assertEqual(withoutDoubles(3, 3, False), 6)

    def test_maxMod5(self):
        self.assertEqual(maxMod5(2, 3), 3)
        self.assertEqual(maxMod5(6, 2), 6)
        self.assertEqual(maxMod5(3, 2), 3)

    def test_redTicket(self):
        self.assertEqual(redTicket(2, 2, 2), 10)
        self.assertEqual(redTicket(2, 2, 1), 0)
        self.assertEqual(redTicket(0, 0, 0), 5)

    def test_greenTicket(self):
        self.assertEqual(greenTicket(1, 2, 3), 0)
        self.assertEqual(greenTicket(2, 2, 2), 20)
        self.assertEqual(greenTicket(1, 1, 2), 10)

    def test_shareDigit(self):
        self.assertTrue(shareDigit(12, 23))
        self.assertFalse(shareDigit(12, 43))
        self.assertFalse(shareDigit(12, 44))

    def test_sum13(self):
        self.assertEqual(sum13([1, 2, 2, 1]), 6)
        self.assertEqual(sum13([1, 1]), 2)
        self.assertEqual(sum13([1, 2, 2, 1, 13]), 6)
        
    def test_centeredAverage(self):
        self.assertEqual(centeredAverage([1, 2, 3, 4, 100]), 3)
        self.assertEqual(centeredAverage([1, 1, 5, 5, 10, 8, 7]), 5)
        self.assertEqual(centeredAverage([-10, -4, -2, -4, -2, 0]), -3)
    
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
        self.assertEqual(fizzArray(4), [0, 1, 2, 3])
        self.assertEqual(fizzArray(1), [0])
        self.assertEqual(fizzArray(10), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_only14(self):
        self.assertTrue(only14([1, 4, 1, 4]))
        self.assertFalse(only14([1, 4, 2, 4]))
        self.assertTrue(only14([1, 1]))

    def test_fizzArray2(self):
        self.assertEqual(fizzArray2(4), ['0', '1', '2', '3'])
        self.assertEqual(fizzArray2(1), ['0'])
        self.assertEqual(fizzArray2(10), ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

    def test_no14(self):
        self.assertTrue(no14([1, 2, 3]))
        self.assertFalse(no14([1, 2, 3, 4]))
        self.assertTrue(no14([2, 3, 4]))

    def test_isEverywhere(self):
        self.assertTrue(isEverywhere([1, 2, 1, 3], 1))
        self.assertFalse(isEverywhere([1, 2, 1, 3], 2))
        self.assertFalse(isEverywhere([1, 2, 1, 3, 4], 1))
