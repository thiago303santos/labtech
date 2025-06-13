import re
class StringCalculator:

    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        delimiter = ",|\n"
        if numbers.startswith("//"):
            parts = numbers.split("\n", 1)
            delimiter = re.escape(parts[0][2:])
            numbers = parts[1]
        nums = re.split(delimiter, numbers)
        return sum(int(n) for n in nums)
