class Calculator :
    # return the sum between 2 operands
    def mysum(self, first_operand, second_operand):
        return first_operand + second_operand


    def min(self, a, b):
        return a if a < b else b

    # return the average between 2 operands
    def myaverage (self, first_operand, second_operand):
        return self.mysum(first_operand, second_operand) / 2