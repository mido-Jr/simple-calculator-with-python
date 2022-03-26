# this code written bt ahmad elnassag
import art
def main_function():
    
    print(art.logo)
    
    # main function for calculator
    def add(A,B):
        return A+B
    
    def sub(A,B):
        return A-B
    
    def mul(A,B):
        return A*B
    
    def div(A,B):
        return A/B

    # dictionary for all function
    math_op = {
        '+':add,
        '-':sub,
        '*':mul,
        '/':div
    }
    # inputs from the user
    number_A = float(input('What is your first number ?'))
    
    should_continue = True
    while should_continue :
        # operation from user
        print('Which operation you want make')
        for sympol in math_op:
            print(sympol) 
        operation_sympol = input('What is your math operation ?')
        
        number_B = float(input('What is your second number ?'))
        
        # cal the result
        calculation_function = math_op[operation_sympol]
        result = calculation_function(number_A,number_B)
        
        print(f'{number_A} {operation_sympol} {number_B} = {result}')
        if input("Do you want continue operation type  'y' ") == 'y':
            number_A = result
        else:
            should_continue = False
            print('Thank you , Bye Bye !')    

if __name__ == '__main__':
    main_function()