numbers = [1,2,3,4,5]
weekdays = ['Monday','Tuesday','Wednesday','Thurday','Friday','Saturday','Sunday']
num = [222,100,85,500,300]
for i in range(len(numbers)):
    print(numbers[i])
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1
for i in range(len(weekdays)):
    print(weekdays[i])
i = 0
while i < len(weekdays):
    print(weekdays[i])
    i += 1
sum = 0
for i in range(len(num)):
        sum = sum + num[i];    
print(f"The sum from for loop: {sum}")
i = 0
sum = 0
while i < len(num):
    sum = sum + num[i];
    i += 1
print(f"The sum of while loop: {sum}")
        


