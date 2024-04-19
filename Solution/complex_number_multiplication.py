class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1, imaginary1 = num1.removesuffix("i").split("+")
        real2, imaginary2 = num2.removesuffix("i").split("+")

        real = int(real1) * int(real2) - int(imaginary1) * int(imaginary2)
        imaginary = int(real1) * int(imaginary2) + int(real2) * int(imaginary1)

        return str(real) + "+" + str(imaginary) + "i"