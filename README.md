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


## 3.Data Preparation/Preprocessing

The Data preprocessing would be required to generated pair of "English-Python" to be fed to the transformer model.Special Care is taken for the following:

     1.All the python code in the generated pair out of the raw dataset
      (of course cleaned with the steps mentioned above) is having proper indentations,spaces/tabs,new line characters .

    2.Special care is taken to generate a workable python code by handling indentations,"," , ":", tabs,new line characters.


    3.Python tokenizer is used to generate tokens from the python code.
    Note:Separate tokens are taken for the following:

      a)COMMENT

      b)ENCODING

      c)INDENT

      d)DEDENT

      e)NEWLINE

      f)ENDMARKER 


      The following code is used to consider the above as separate tokens while tokenizing python code into tokens

      try:
        tokens = tokenize.tokenize(io.BytesIO(text.encode('utf-8')).readline)
        for five_tuple in tokens:
            if five_tuple.type == tokenize.COMMENT:
                continue
            elif five_tuple.type == tokenize.ENCODING:
                continue
            elif five_tuple.type == tokenize.INDENT:
                python_token_list.append("INDENT")
            elif five_tuple.type == tokenize.DEDENT:
                python_token_list.append("DEDENT")
            elif five_tuple.type == tokenize.NL or five_tuple.type == tokenize.NEWLINE:
                python_token_list.append("NEWLINE")
            elif five_tuple.type == tokenize.ENDMARKER :
                continue
            else:
                python_token_list.append(five_tuple.string)
    except Exception:
        raised_exception = True


      4.The spacy tokenizer is used to generate tokens for English text

      5.The python tokenizer with special handling of the tokens (explained in Item3 above) is used to generate tokens out of the python 
      code.

      6.A dataframe is formed out of The spacy tokens from English text and python tokens  from Python code.

      7.The dataframe from Item6 above is used as an input to the model

      8.Below is the sample python tokens  generated out of python tokenizer:

      {'English': ['count', 'tuple', 'elements', 'inside', 'list'],
      'Python': ['random',
       '=',
       '[',
       "'a'",
       ',',
       '(',
       "'a'",
       ',',
       "'b'",
       ')',
       ',',
       '(',
       "'a'",
        ',',
       "'b'",
       ')',
       ',',
      '[',
      '3',
      ',',
      '4',
      ']',
      ']',
      'NEWLINE',
      'count',
      '=',
     'random',
      '.',
     'count',
     '(',
     '(',
     "'a'",
     ',',
     "'b'",
     ')',
     ')',
     'NEWLINE',
     'print',
     '(',
        '"The count of (\'a\', \'b\') is:"',
      ',',
      'count',
     ')',
      'NEWLINE']}
      

## 5. Model Architecture

The Model used is **transformers with self-attention, multi-head, and scaled-dot product attention**

The model is implemented from [Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation](https://arxiv.org/abs/1406.1078). This model will achieve improved test perplexity whilst only using a single layer RNN in both the encoder and the decoder.

## Introduction

The general encoder-decoder model.

![](https://github.com/bentrevett/pytorch-seq2seq/blob/master/assets/seq2seq1.png?raw=1)

We use our encoder (green) over the embedded source sequence (yellow) to create a context vector (red). We then use that context vector with the decoder (blue) and a linear layer (purple) to generate the target sentence.

the older models, we used an multi-layered LSTM as the encoder and decoder.

![](https://github.com/bentrevett/pytorch-seq2seq/blob/master/assets/seq2seq4.png?raw=1)

One downside of the previous model is that the decoder is trying to cram lots of information into the hidden states. Whilst decoding, the hidden state will need to contain information about the whole of the source sequence, as well as all of the tokens have been decoded so far. By alleviating some of this information compression, we can create a better model!

We'll also be using a GRU (Gated Recurrent Unit) instead of an LSTM (Long Short-Term Memory). Why? Mainly because that's what they did in the paper (this paper also introduced GRUs) and also because we used LSTMs last time. To understand how GRUs (and LSTMs) differ from standard RNNS, check out [this](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) link. Is a GRU better than an LSTM? [Research](https://arxiv.org/abs/1412.3555) has shown they're pretty much the same, and both are better than standard RNNs. 


## 6. Evaluation Metric
The model is used to acheive the perplexity.The perplexity is used as the evaluation metric.

We acheived a test perplexity of **2.202**


## 7.Model Prediction

Now that the transformer model is trained.We would be using the model to predict the python code generated in case an "English Text" is given as input to the Model

Also the python code generated is in the form of tokens.This has to further formatted to generate appropriate python code.


A python intepreter has to be used to run the generated python code to verify if its working



## 8. Sample Python code generation

  #### Below is the code to predict the python code generated out of the model:
    
    translation, attention = translate_sentence(src, SRC, TRG, model, device)

    print(f'predicted trg = {translation}'
  ####  The python code generated out of prediction for one sample data is:

    Englist text: ['write', 'a', 'function', 'to', 'accept', 'input', 'as', 'feet', 'and', 'inches', 'into', 'centimeters']
    Python Code:['def', 'height_into_cms', '(', 'feet', ',', 'inches', ')', ':', 'NEWLINE', 'INDENT', 'ininches', '=', 'feet', '*', '12', '+', 'inches', 'NEWLINE', 'return', 'ininches', '*', '2.54', 'NEWLINE', 'DEDENT', '<eos>']

## 9. Python code formatter.

     import tokenize
     def format_to_python_code(list_tokens):
        final_list = []
        for i in range(len(list_tokens)):
          print(list_test2_mod[i],list_test2_mod[i] == 'NEWLINE')
          final_list.append(list_test2_mod[i])
          if i > 0:
              if i+1 < len(list_tokens) and list_tokens[i-1] != 'NEWLINE':
              p = i -1
              if list_tokens[i] != 'NEWLINE' and list_tokens[p] != 'NEWLINE' and  list_tokens[i] != 'INDENT' and  list_tokens[p] != 'INDENT':
              if list_tokens[i] == 'ininches':
              print(list_tokens[p],list_tokens[p] == 'INDENT')
              final_list.append(' ')
            if list_tokens[i] == 'INDENT':
                  final_list.append("  ")
            elif list_tokens[i] == 'DEDENT':
                #final_list.append(' ')
                  continue
            elif list_tokens[i] == 'NEWLINE':
                  print("Adding new line")
                  final_list.append("\n")
             elif list_tokens[i] == 'return':
            final_list.append("  "+list_tokens[i])              
         else:
           final_list.append(list_tokens[i])

        
        return final_list
  
   ##### The following code is used to generate output:
  
       file1 = open("/content/gdrive/MyDrive/data/func_test.py","w")   
  
        file1.writelines(format_to_python_code(list_test_mod)) 
       file1.close() #to change file access modes 
  
       file1 = open("/content/gdrive/MyDrive/data/func_test.py","r+")  
  
        print ("Output of Read function is ")
        print (file1.read()) 
        print()

  
  #### The output generated out of the code is:
       defheight_into_cms(feet,inches):
          ininches=feet*12+inches
          return ininches*2.54

## 10. Running it thru python interpreter
   ##### To run the code in python intepreter the following is used:
      import func_test
      func_test.height_into_cms(1,2)

## 11. 25 generated python code is available at(25 .py files) .

https://github.com/sudhakarmlal/End-Capstone/tree/main/25_Python_Generated_Code

## 12.Also output of python intepretor used to run the 25 .py files can be found at

https://github.com/sudhakarmlal/End-Capstone/tree/main/25_Python_Generated_Code_Output





