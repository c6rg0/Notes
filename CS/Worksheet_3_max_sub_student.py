total = 0  
count = 0   

print("This program finds the maximum of sets of three numbers.")
print("Enter three zeroes to finish.")                          
print("Program then outputs the average of the maximums.")      

num1 = int(input("Please enter first number: "))    
num2 = int(input("Please enter second number: "))    
num3 = int(input("Please enter third number: "))

while num1 != 0 and num2 != 0 and num3 != 0:                   

    max_value = num1                                       
    
    if num2 > max_value:                                        
        max_value = num2                                    
    
    if num3 > max_value:                                      
        max_value = num3                                        
    
    print("Maximum is:", max_value)                             
    
    total = total + max_value                                   
    count = count + 1  

    num1 = int(input("Please enter first number: "))    
    num2 = int(input("Please enter second number: "))    
    num3 = int(input("Please enter third number: "))

if count == 0:
    average = 0
else:
    average = total / count   

print("Average of maximums is", average)

