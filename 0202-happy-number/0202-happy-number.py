class Solution:
    def isHappy(self, n: int) -> bool:

        def sum_of_squares(number):
            total_sum = 0

            while number > 0:
                last_digit = number % 10
                number = number // 10

                total_sum += last_digit**2
            return total_sum

    # sum_of_squares(n)

        slow_pointer = n
        fast_pointer = sum_of_squares(n)

        while fast_pointer!= slow_pointer and fast_pointer !=1:
            slow_pointer = sum_of_squares(slow_pointer)
            fast_pointer = sum_of_squares(sum_of_squares(fast_pointer))

        if fast_pointer == 1:
            return True
        return False
        