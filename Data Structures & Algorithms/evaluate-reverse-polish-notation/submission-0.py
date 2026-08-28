class Solution:
    def evalRPN(self, tokens: List[str]) -> int:


        nums = []

        for char in tokens:

            if char == "+" or char == "-" or char == "*" or char == "/":
                a = int(nums.pop())
                b = int(nums.pop())
                if char == "+":
                    nums.append(a + b)
                elif char == "-":
                    nums.append(b - a)
                elif char == "*":
                    nums.append(a * b)
                elif char == "/":
                    nums.append(b / a)
            else:
                nums.append(char)


                
        return int(float(nums[0]))
                
        