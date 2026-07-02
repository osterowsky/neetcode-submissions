class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            calc = digits[i] + carry
            digits[i] = calc % 10
            carry = 1 if calc == 10 else 0

        return [carry] + digits if carry else digits