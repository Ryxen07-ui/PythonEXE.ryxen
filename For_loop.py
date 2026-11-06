# For Exercise 2
# previous_number = 0

# for current_number in range(10):
#     total_sum = current_number + previous_number
#     print(f"Current Number {current_number} Previous Number {previous_number} Sum: {total_sum}")
    
#     previous_number = current_number

# For Exercise 5
# a = 5
# b = 10

# print(f"Before Swap a:{a} b:{b}")
# a,b = b,a
# print(f"After Swap a:{a} b:{b}")

# For Exercise 6
# number = 5
# factorial = 1

# for i in range (1, number + 1):
#    factorial = factorial * i
#    print(f"The factorial of {number} is {factorial} ")

# For Exercise 7
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# fruits.remove("banana")
# fruits.append("fig")
# print(fruits)

# For Exercise Reverse a String
# text = "Python"
# reverse_text = "python"[::-1]
# print(reverse_text)

# For Exercise 9 Vowel Frequency Counter
# sentence = "Learning Python is fun!"
# Vowels = "aeiou"
# count = 0

# for character in sentence.lower():
#     if character in Vowels:
#         count += 1


# print(f"Number Of Vowels: {count}")

# For Exercise 10
# nums = [45, 2, 89, 12, 7]
# use if need to compare largest and smallest max()-largest, min()-smallest
# Largest = max(nums)
# Smallest = min(nums)
# print(f"Largest number:{Largest}\n Smallest number:{Smallest}")

# For Exercise 11
# data = [1, 2, 2, 3, 4, 4, 4, 5]
# # Set(remove duplicated number from the links)
# i = list(set(data)) 
# print(f"Unique Link:{i}")

# Exercise 13: Filter Numbers Divisible by 5[cite: 10]
# num_list = [10, 20, 33, 46, 55]

# print("Divisible by 5:")

# for num in num_list:
#     if num % 5 == 0:
#         print(num)

# For exercise 15 Nested loop(double loops)

# အပြင်ဘက် Loop (Outer Loop) - အတန်း (Rows) တွေကို ထိန်းချုပ်သည်
for i in range(1, 6):
    # အတွင်းဘက် Loop (Inner Loop) - တစ်တန်းချင်းစီအတွင်း ဂဏန်းများကို ဘေးတိုက် ပုံနှိပ်သည်
    for j in range(1, i + 1):
        print(i, end=" ")
    
    # အပြင်ဘက် Loop ရဲ့ အမိန့်အရ အောက်ေလိုင်းသို့ ဆင်းရန်
    print()