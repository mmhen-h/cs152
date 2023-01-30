# 1.
# 2.
# 3.
# 4. 


#input: a number
#output: the number of even numbers between that number and 0 (including 0 and the number)
def howManyEven(num):
    count = 0
    if num < 0:
        num *= -1
    while(num >= 0):
        if isEven(num):
            count += 1
        num -= 1
    return count
    
#input: a number
#output: true/false depending on whether the number is even or not
def isEven(num):
    return num % 2 == 0
    
#input: a number
#output: true/false depending on whether the number is odd or not
def isOdd(num):
    return num % 2 != 0
  
def noChange(cents):
  #student code here
  return


#input: num–an int of some kind
#output: the positive factorial of num
def oldFactorial(num):
    total = 1
    if num < 0:
        num = num * (-1)
    while(num == num):
        if num <= 0:
            break
        else:
            total = total * num
            num = num - 1
    return total
  
    
def main():
    print(howManyEven(4))
    print(howManyEven(9))
    print(isOdd(12))
    print(isEven(12))
    
if __name__ == "__main__":
    main()