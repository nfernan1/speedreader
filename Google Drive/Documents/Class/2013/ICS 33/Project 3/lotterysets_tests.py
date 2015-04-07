#Nicholas Fernando 12659548

import unittest
from lotterysets import *

class TestLotterySets(unittest.TestCase):
    'Tests the methods in the lotteryset module'
    
    def setUp(self):
        'Creates a make lottery set object to test with'
        self.lot0 = make_lottery_set_type('SuperLotto', 6, (1,50))
        self.lot1 = self.lot0([1,2,3,4,5,6])
        
        self.lot2 = make_lottery_set_type('SuperLotto', 6, (1,50))
        self.lot3 = self.lot2([1,2,3,4,5,6])

        self.lot4 = make_lottery_set_type('PowerBall',7,(1,20))
        self.lot5 = self.lot4([3,4,5,2,6,8,18])

    def test_make_lottery_set_type_makes_lottery_set_object(self):
        'Compares the make lottery set type with the class '
        self.assertEqual(make_lottery_set_type('SuperLotto',6,(1,50))([1,2,3,4,5,6,]), self.lot0([1,2,3,4,5,6]))
        
        
    def test_canonical_representation_of_lotterysets(self):
        'Checks to make sure the unique representation for the lottery set object'
        self.assertEqual(repr(self.lot1), "make_lottery_set_type('SuperLotto', 6, (1, 50))([1, 2, 3, 4, 5, 6])")
        self.assertEqual(repr(self.lot3), "make_lottery_set_type('SuperLotto', 6, (1, 50))([1, 2, 3, 4, 5, 6])")


    def test_length_function_should_return_size_of_list(self):
        'Make sures the length of the list is the same as the set size specified'
        self.assertEqual(len(self.lot1), 6)
        self.assertEqual(len(self.lot3), 6)
        self.assertEqual(len(self.lot5), 7)

        # Raises LotterySetError if the set is greater or less than the specified set size
        x = [1,2,3,4,5]
        with self.assertRaises(LotterySetError):
            self.lot2([x])

    def test_forward_iteration_should_return_elements_in_set(self):
        'Checks to see if the elements in the list are the ones specified when the object is created'
        check = []
        for i in self.lot1:
            check.append(i)

        self.assertEqual(check,[1,2,3,4,5,6])

        check1 = []
        for i in self.lot3:
            check1.append(i)

        self.assertEqual(check1,[1,2,3,4,5,6])

        check2=[]
        for i in self.lot5:
            check2.append(i)

        self.assertEqual(check2,[3,4,5,2,6,8,18])

         
        
    def test_reverse_iteration_should_return_reversed_elements_in_set(self):
        'Checks to see if the elements in the list are put from last to first order'
        check = []
        for i in reversed(self.lot1):
            check.append(i)

        self.assertEqual(check,[6,5,4,3,2,1])

        check1 = []
        for i in reversed(self.lot3):
            check1.append(i)

        self.assertEqual(check1,[6,5,4,3,2,1])

        check2=[]
        for i in reversed(self.lot5):
            check2.append(i)

        self.assertEqual(check2,[18,8,6,2,5,4,3])


        
    def test_contains_special_method_returns_true_if_integer_is_in_set(self):
        'Checks if the integer is within the set of the specified object list'

        self.assertTrue(1 in self.lot1)
        self.assertTrue(5 in self.lot3)
        self.assertTrue(18 in self.lot5)

        self.assertFalse(20 in self.lot1)
        self.assertFalse(15 in self.lot3)
        self.assertFalse(1 in self.lot5)


    def test_returns_true_if_integer_is_not_in_set(self):
        'Checks to see if the integer is not within the specfied objects set list'
        self.assertTrue(20 not in self.lot1)
        self.assertTrue(14 not in self.lot3)
        self.assertTrue(1 not in self.lot5)

        self.assertFalse(1 not in self.lot1)
        self.assertFalse(2 not in self.lot3)
        self.assertFalse(18 not in self.lot5)


    def test_full_match_method_if_lottery_set_objects_are_equivalent_return_true(self):
        'Checks to see if the lottery set objects are equivalent'
        self.assertTrue(self.lot1 == self.lot3)
        self.assertFalse(self.lot1 == self.lot5)
        
    def test_full_match_method_test_if_lottery_set_objects_are_not_equivalent(self):
        'Checks to see if the lottery set object is not equivalent of the other specified lottery set object'
        self.assertTrue(self.lot1 != self.lot5)
        self.assertTrue(self.lot3 != self.lot5)
        
    def test_match_count_method_if_integers_are_in_both_sets_returns_how_many_are_similar(self):
        'Checks if the sets have similar integers and returns the amount of similar integers'
        self.assertEqual(self.lot1.match_count(self.lot3), 6)

        # Raises LotterySetError when the games are not the same
        with self.assertRaises(LotterySetError):
            self.assertEqual(self.lot1.match_count(self.lot5), 5)

    def test_if_set_contains_duplicate_integers(self):
        'Checks to make sure the set of integers are all unique numbers'
        x = [3,3,2,2,1,1]

        # Raises a LotterySetError if the integers in the set are not unique
        with self.assertRaises(LotterySetError):
            self.assertEqual(self.lot0(x))

    def test_if_integers_in_set_are_within_min_and_max_range(self):
        'Checks if the sets integers are within the set minimum and maximum'
        x = [0,12,4,5,2,49]

        # Raises a LotterySetError if an integer is not at least the minimum number
        with self.assertRaises(LotterySetError):
            self.assertEqual(self.lot0(x))

        y = [1,2,3,4,5,51]

        # Raises a LotterySetError if an intger is not at most the maximum number
        with self.assertRaises(LotterySetError):
            self.assertEqual(self.lot0(y))
        




    

if __name__=='__main__':
    unittest.main(exit = False)


