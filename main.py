# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

counter = 0
total = 0

for count in range(0, len(student_heights)):
    counter = counter + 1
    total = total + student_heights[count]


print(total)
print(counter)
print(sum(student_heights))

average = total / counter

print(int(average))