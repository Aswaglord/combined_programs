def dec_to_bin():
  num = int(input("Enter a Decimal Number (0-255): "))
  converted_binary_number = ""
  binary_num_start = 128
  remainder = num

  for index in range(8):
    if remainder / binary_num_start >= 1:
      converted_binary_number += "1"
      remainder = num % binary_num_start
      binary_num_start = binary_num_start/2
    else:
      binary_num_start = binary_num_start/2
      converted_binary_number += "0"

  return converted_binary_number

def bin_to_dec():
  bin_string = input("Enter Binary Number (8-digits): ")
  converted_num = 0
  start_num = 128

  for index in range(8):
    if bin_string[index] == "1":
      converted_num += start_num
      start_num /= 2
    else:
      start_num /= 2

  return int(converted_num)


def bin_add(bin_str_1,bin_str_2):
  
  format_str1 = bin_str_1.zfill(8)
  format_str2 = bin_str_2.zfill(8)
  num_1_list = list(format_str1[::-1])
  num_2_list = list(format_str2[::-1])
  num_total = ""
  carry_num = False

  for index in range(len(num_1_list)):
    if carry_num:
      num_1_list[index] = str(int(num_1_list[index]) + 1)
      carry_num = False
    if int(num_1_list[index]) + int(num_2_list[index]) == 3:
      carry_num = True
      num_total += "1"
    elif int(num_1_list[index]) + int(num_2_list[index]) == 2:
      carry_num = True
      num_total += "0"
    elif int(num_1_list[index]) + int(num_2_list[index]) == 1:
      num_total += "1"
    else:
      num_total += "0"

  return num_total[::-1]


def bin_sub(bin_str_2,bin_str_1):
  
  if int(bin_str_1) > int(bin_str_2):
    return "Error: Negative result"
  else:
    format_str1 = bin_str_1.zfill(8)
    format_str2 = bin_str_2.zfill(8)
    num_1_list = list(format_str1[::-1])
    num_2_list = list(format_str2[::-1])
    num_total = ""
  
    for index in range(len(num_1_list)):
      if int(num_2_list[index]) - int(num_1_list[index]) == -1:
        num_total += "1"
        for num in range(index + 1, len(num_1_list)):
          if num_2_list[num] == "0":
            num_2_list[num] = "1"
          else: 
            num_2_list[num] = "0"
            break
      elif int(num_2_list[index]) - int(num_1_list[index]) == 0:
        num_total += "0"
      else:
        num_total += "1"

  return num_total[::-1]

def bin_mul(bin_str_1,bin_str_2):

  format_str1 = bin_str_1.zfill(8)
  format_str2 = bin_str_2.zfill(8)
  bin_list_1 = list(format_str1)
  bin_list_2 = list(format_str2)
  list_to_add = ['0']

  while len(bin_list_2) > 0:
    next_line = []
    zeros = len(bin_list_1) - len(bin_list_2)
    current = bin_list_2.pop()
    for num in bin_list_1:
      next_line.append(str(int(num) * int(current)))
      print(next_line)
    next_line += ['0'] * zeros
    list_to_add = bin_add("".join(list_to_add), "".join(next_line))

  return list_to_add

def bin_div(bin_str_1,bin_str_2):
  output = ''
  numer_str = ''
  format_str1 = bin_str_1.zfill(8)
  format_str2 = bin_str_2.zfill(8)
  num_1_list = list(format_str1)
  
  if int(bin_str_2) == 0:
    print('Undefined')
  for i in range(len(num_1_list)):
    numer_str += num_1_list[i]
    if int(numer_str) < int(format_str2):
      output += '0'
    else:
      output += '1'
      numer_str = str(int(numer_str)-int(format_str2))
      
  return output

def menu():
  dashes = "-" * 28
  print(f"""*** Binary Calculator ***\n{dashes}
(B)inary to Decimal Conversion
(D)ecimal to Binary Conversion
(A)dd two Binary Numbers
(S)ubtract two Binary Numbers
(M)ultiply two Binary Numbers
D(i)vide two Binary Numbers
(Q)uit""")

program_running = True

while program_running:
  dashes = "-" * 28
  menu()
  user_input = input("").upper()

  if user_input == "B":
    print(f" = {bin_to_dec()}")
  elif user_input == "D":
    print(f" = {dec_to_bin()}")
  elif user_input == "A":
    bin_str_1 = input("Enter the first binary number : ")
    bin_str_2 = input("Enter the Second binary number : ")
    print(f"= {bin_add(bin_str_1,bin_str_2)}")
  elif user_input == "S":
    bin_str_2 = input("Enter the larger binary number: ")
    bin_str_1 = input("Enter the smaller binary number: ") 
    print(f"= {bin_sub(bin_str_2,bin_str_1)}")
  elif user_input == "M":
    bin_str_1 = input("Enter the first binary number : ")
    bin_str_2 = input("Enter the Second binary number : ")
    print(f" = {bin_mul(bin_str_1,bin_str_2)}")
  elif user_input == "I":
    bin_str_1 = input("Enter the first binary number (dividend) : ")
    bin_str_2 = input("Enter the Second binary number (divisor) : ")
    print(f" = {bin_div(bin_str_1, bin_str_2)}")
  elif user_input == "Q":
    quit()
  else:
    print("please choose a character from the list above.")

  input("Press <enter> to continue")
  print(dashes)

