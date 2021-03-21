# END-Capstone
# Capstone Project- Transformer Based Model to generate  Python code

The project is about  sequence-to-sequence models using PyTorch and TorchText, we'll be implementing the model

## Steps followed to generate Python Code


## Steps followed to generate Python Code

### 1.Understanding Data
The dataset contains **4600+** examples of English text to python code.The dataSet is of the following Format:

#### a)  English Text:
The English text describes what is the program all about.E.g

      i) # write a program to find and print the smallest among three numbers
      ii)# Write a program to check whether a number is prime or not
      iii) # Write a program to find the factorial of a number
     
#### b)  Python code:
The Python code corresponds to whatever described by the English Text  e.g 

Sample python function would look like
    
    def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum

Sample python program would look like

    num1 = 10
    num2 = 12
    num3 = 14
    if (num1 >= num2) and (num1 >= num3):
    largest = num1
    elif (num2 >= num1) and (num2 >= num3):
    largest = num2
    else:
      largest = num3
    print(f'largest:{largest}')
