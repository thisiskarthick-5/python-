def numbers_to_message(numbers):
    message = ""
    
    
    for number in numbers:
        
        num = int(number)
        
        if 1 <= num <= 26: 
            message += chr(num + 96)  
        else:
            message += '?'  
    
    return message


input_numbers = input("enter the number :")  
secret_message = numbers_to_message(input_numbers)
print(secret_message)  
