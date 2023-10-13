def logical_operators():
  #####################logical operators#############################################
  # Logical Operators Practice #1
  # Create three variables (num1, num2, and num3):
  # Inside num1, store the value 36
  num1 = 36
  # Inside num2, stores the result of the operation 72/2
  num2 = 72/2
  # Inside num3, store the value 48
  num3 = 48
  # Check if num1 is greater than num2, and less than num3. Store the result of that  comparison in a variable called my_bool.
  my_bool = num1 > num2 < num3
  print(my_bool)
  
  # Logical Operators Practice #2
  # Create three variables (num1, num2, and num3):  
  # Inside num1, store the value 36
  num1 = 36
  # Inside num2, stores the result of the operation 72/2
  num2 = 72/2
  # Inside num3, store the value 48
  num3= 48
  # Check if num1 is greater than num2, or less than num3. Store the result of that comparison in a variable called my_bool.
  your_bool = num1 > num2 or num1 < num3
  print(your_bool)
  
  #   Logical Operators Practice #3
  # Check if the words:
  word1 = "success"
  # and
  word2 = "technology"
  # are not found in the sentence below, and store the result (a boolean) in a variable called my_bool:
  sentence = ("'When something is important enough, you do it even if the odds are against you' - Elon Musk")
  word1_found = word1 in sentence
  print("The word 'success' was found in the sentence:" ,word1_found)
  word2_found = word2 in sentence
  print("The word 'technology' was found in the sentence:" ,word2_found)
  
  print(" ")