#!/Applications/anaconda/envs/Python3/bin


def main():
    # Test suite
    tests = [
        #[None, None], # Should throw a TypeError
        #[0, False],
        #[1, True],
        [2, True],
        [15, False],
        [16, True],
        [65536, True],
        [65538, False]
    ]

    for item in tests:
        try:
            temp_result = is_power_of_two(item[0])
            if temp_result == item[1]:
                print('PASSED: is_power_of_two({}) returned {}'.format(item[0], temp_result))
            else:
                print('FAILED: is_power_of_two({}) returned {}, should have returned {}'.format(item[0], temp_result, item[1]))

        except TypeError:
            print('PASSED TypeError test')

    return 0


def is_power_of_two(val):
        '''
        Determines if val is a power of two
        Input: val is a positive integer
        Output: Boolean
        '''
        # Check input
        if type(val) is not int:
            raise TypeError('Input must be an integer')

        # Trivial cases
        if val <= 0:
            return False

        if val == 1:
            return True

        # Repeat divisions by 2 until val = 2
        while val > 1:
            if val % 2 == 1:
                return False

            val /= 2

        return True


if __name__ == '__main__':
    main()
