import unittest

import primeno


class TestPrime(unittest.TestCase):
    def test_primenumbers_within_range_of_50(self):
        '''Test for results within range of 50'''
        self.assertEqual(primeno.prime_num(
            50), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
    
    def test_number_is_an_integer(self):
        '''Test that the function accepts only integers'''
        self.assertEqual(primeno.prime_num('str'),
                         'only intergers are allowed')

    def test_content_of_primes_within_range_5(self):
        '''Test that the function tests the content of prime within range 5'''
        self.assertIn(2, primeno.prime_num(5))
        self.assertIn(3, primeno.prime_num(5))
        
    def test_number_two(self):
        '''Test that the function returns 2 only as the only output'''
        self.assertEqual(primeno.prime_num(2), [2])
     

    def test_number_is_negative_number(self):
        '''Test that the function returns an error message given a negative integer'''
        self.assertEqual(primeno.prime_num(-5), 'Negative numbers not allowed')
    

    def test_number_does_not_return_an_empty_list(self):
        '''Test that the function does not return an empty list given a number'''
        self.assertEqual(primeno.prime_num(5), [2, 3, 5])
    

    def test_number_input_is_list(self):
        '''Test that the function does not accept lists'''
        self.assertEqual(primeno.prime_num([]), 'only intergers are allowed')
    

    def test_number_input_is_dictionary(self):
        '''Test that the function does not accept dictionaries'''
        self.assertEqual(primeno.prime_num({}), 'only intergers are allowed')
    

    def test_return_list_length(self):
        '''Test that the function returns the correct list length'''
        self.assertEqual(len(primeno.prime_num(3)), 2)

    def test_return_zero(self):
        '''Test that the function returns an empty list if input is 0'''
        self.assertEqual(primeno.prime_num(0), [])

    def test_number_input_is_float(self):
        '''Test that the function returns an error message if is of type float'''
        self.assertEqual(primeno.prime_num(58.3694),
                         'only intergers are allowed')
