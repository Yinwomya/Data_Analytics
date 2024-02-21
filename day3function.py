# accept 2 numbers from a user

def accept_input():
    num1=int(input('Enter 1st number: '))
    num2=int(input('Enter 2nd number: '))
    return num1, num2

# adds two numbers

def addition(nuro_1, nuro2):
    result = nuro_1 + nuro2
    return result

# substration

def multiplication (nuro_1, nuro2):
    result = nuro_1 * nuro2
    return result

# function calling

def main():
    print("Enter '+' for sum")
    print("Enter '*' for Product")
    op_type= input("WHAT OPERATION DO YOU WANT TO PERFORM? ")
    
    if (op_type== '+'):
        input_1, input_2=accept_input()
        final_answer = addition (input_1, input_2) 
        print('The addition results is: ', final_answer) 
    elif (op_type== '*'):
        input_1, input_2=accept_input()
        final_answer = multiplication(input_1, input_2)
        print('The product is: ', final_answer)   
    else:
        print('Selected option not available')
        print('Thanks for using the program')

main()

