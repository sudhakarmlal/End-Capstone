# END-Capstone
# Capstone Project- Transformer Based Model to generate  Python code

The project is about  sequence-to-sequence models using PyTorch and TorchText, we'll be implementing the model


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

## 2. Data Cleaning

As a part of data preparation,data cleaning is pretty important.The cleaned data would later be preprocessed and fed to the transformer model. 

####  **Data Cleaning Strategy:**
The DataCleaning procedure was **manual** for the following Strategy is followed for data cleaning

    1.The complete Engilsh Text that describes the python code is kept in one line.
    In case in some of the english texts in the dataset if it is in two lines it is brought to one line.

    This has to be done to identify English text of the pair of English-Python to be fed to the transformer model 

    2.The python code is placed in the very next line.
     For any of the python code if there is a space in between the
    "English text" and the "Python code" the space is removed.
    This space is removed.

    Again this has to be done to identify the Python code of the pair of   
    English-Python code to be fed to the transformer model

    3.The in between spaces and comments in the python code has to be 
      removed so that the model doesn't learn any unncessary stuff e.g 
      redundant new lines or #comments(in between code)  for the python 
      code generated   


