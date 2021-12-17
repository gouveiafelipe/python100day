# You should not use the sum() or len() functions in your answer
# You should try to replicate their functionality using what you have learnt about for loops.

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

total_heights = 0
sum_heights = 0

for i in student_heights:
    total_heights += 1
    sum_heights += i

average_heights = round(sum_heights / total_heights)

print(average_heights)



# Write your code below this row 👇
