import numpy as np

name=np.array(["shaurya","kunal","shriya","soham","atharv","pranav"])
marks=np.array([99.9,63,23,67,43,85])

print("\n----Student details----")
print("name:",name)
print("marks:",marks)

print("\n----Student analysis----")

print("total sum:",np.sum(marks))
print("avg marks:",np.mean(marks))
print("highest marks:",np.max(marks))
print("lowest marks:",np.min(marks))

print("\n----Topper----")
top_index=np.argmax(marks)
print("\n🏆Topper:",name[top_index],"-",marks[top_index])

print("\n-----Result-----")
result=np.where(marks>=30,"Pass","Fail")

for i in range(len(name)):
    print(name[i],":",result[i])

print("\n-----Grade-----")
for i in range(len(marks)):
    m=marks[i]
    if m>=90 and m<=100:
        Grade="A+"
    elif m>=80 and m<=89:
        Grade="A"
    elif m>=70 and m<=79:
        Grade="B1"
    elif m>=60 and m<=69:
        Grade="B2"
    elif m>=50 and m<=59:
        Grade="C+"
    elif m>=40 and m<=49:
        Grade="C"  
    elif m>=30 and m<=39:
        Grade="D"  
    else:
        Grade="F"
    print(name[i],":",Grade)

print("\n-----Filtered data-----")

avg=np.mean(marks)

print("\n students scoring above average:")
print(name[marks>avg],"-",marks[marks>avg])

print("\n students scoring below 40: ")
print(name[marks<40],"-",marks[marks<40])

print("\n-----Sorted Data-----")

sorted_indices=np.argsort(marks)

print("\n (Name Sorted):",name[sorted_indices])
print("\n (Marks Sorted):",marks[sorted_indices])

print("\n-----Suggestions-----")

print("\n Needs improvement:")
print(name[marks<40])

print("\n Excellent Students: ")
print(name[marks>80])


