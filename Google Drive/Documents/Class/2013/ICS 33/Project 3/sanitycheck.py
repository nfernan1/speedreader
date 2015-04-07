# lotterysets_sanitycheck_tests.py
#
# ICS 33 Summer 2013
# Project #3: Careful with That Axe, Eugene
#
# This is a set of unit tests that you can use to sanity check that your
# implementation is structurally correct (e.g., functions and classes
# have the right names, the right operations are supported).  Be sure you
# understand that passing all of these tests doesn't necessarily mean
# everything is complete and correct, as none of these tests checks that
# functionality is correct; the goal here is just to be sure that you have
# everything you're supposed to have.  It'll be up to you to write unit
# tests that demonstrate that all the pieces work correctly.
#
# In short, if your "lotterysets" module does not pass all of these tests,
# there is definitely a problem you'll need to solve; but if your "lotterysets"
# module passes all of them, you may still have issues not tested here.
#
# Note that most of these tests don't include any asserts.  What makes them
# work is that the "unittest" module considers any test that raises an
# exception to have failed; most of these tests raise exceptions when
# necessary functionality is missing, and any situation like that would be
# considered a test failure.

from lotterysets import *
import unittest



class LotterySetsSanityCheckTests(unittest.TestCase):
    def test_necessary_exception_exists_and_carries_error_message(self):
        LotterySetError('This is a LotterySetError!')


    def test_make_lottery_set_type_exists_and_takes_three_parameters(self):
        make_lottery_set_type('BooLotto', 6, (1, 50))


    def test_lottery_sets_have_set_size_class_variable(self):
        BooLotto = make_lottery_set_type('BooLotto', 6, (1, 50))
        BooLotto.set_size


    def test_lottery_sets_have_min_set_number_class_variable(self):
        BooLotto = make_lottery_set_type('BooLotto', 6, (1, 50))
        BooLotto.min_set_number


    def test_lottery_sets_have_max_set_number_class_variable(self):
        BooLotto = make_lottery_set_type('BooLotto', 6, (1, 50))
        BooLotto.max_set_number


    def test_lottery_sets_have_constructor_that_takes_one_parameter(self):
        BooLotto = make_lottery_set_type('BooLotto', 6, (1, 50))
        BooLotto([1, 2, 3, 4, 5, 6])


    def test_lottery_sets_have_full_match(self):
        BooLotto = make_lottery_set_type('BooLotto', 6, (1, 50))
        boo1 = BooLotto([1, 2, 3, 4, 5, 6])
        boo2 = BooLotto([2, 3, 4, 5, 6, 7])
        boo1.full_match(boo2)


    def test_lottery_sets_have_match_count(self):
        BooLotto = make_lottery_set_type('BooLotto', 6, (1, 50))
        boo1 = BooLotto([1, 2, 3, 4, 5, 6])
        boo2 = BooLotto([2, 3, 4, 5, 6, 7])
        boo1.match_count(boo2)


    def test_lottery_sets_can_generate_a_custom_repr(self):
        BooLotto = make_lottery_set_type('BooLotto', 6, (1, 50))
        self.assertTrue('__repr__' in BooLotto.__dict__.keys())


    def test_lottery_sets_can_calculate_a_length(self):
        BooLotto = make_lottery_set_type('BooLotto', 6, (1, 50))
        len(BooLotto([1, 2, 3, 4, 5, 6]))


    def test_lottery_sets_can_be_compared_for_equality(self):
        BooLotto = make_lottery_set_type('BooLotto', 6, (1, 50))
        BooLotto([1, 2, 3, 4, 5, 6]) == BooLotto([2, 3, 4, 5, 6, 7])


    def test_lottery_sets_can_be_compared_for_inequality(self):
        BooLotto = make_lottery_set_type('BooLotto', 6, (1, 50))
        BooLotto([1, 2, 3, 4, 5, 6]) != BooLotto([2, 3, 4, 5, 6, 7])


    def test_lottery_sets_can_determine_if_number_is_in_set(self):
        BooLotto = make_lottery_set_type('BooLotto', 6, (1, 50))
        16 in BooLotto([1, 2, 3, 4, 5, 6])


    def test_lottery_sets_can_determine_if_number_is_not_in_set(self):
        BooLotto = make_lottery_set_type('BooLotto', 6, (1, 50))
        16 not in BooLotto([1, 2, 3, 4, 5, 6])


    def test_lottery_sets_can_be_forward_iterated(self):
        BooLotto = make_lottery_set_type('BooLotto', 6, (1, 50))
        for x in BooLotto([1, 2, 3, 4, 5, 6]):
            pass


    def test_lottery_sets_can_be_reverse_iterated(self):
        BooLotto = make_lottery_set_type('BooLotto', 6, (1, 50))
        for x in reversed(BooLotto([1, 2, 3, 4, 5, 6])):
            pass



if __name__ == '__main__':
    unittest.main(exit = False)
