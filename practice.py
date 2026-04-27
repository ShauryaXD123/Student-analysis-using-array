import numpy as np

# --------------Data-----------------

name=np.array(["shaurya","pranav","atharv","soham","shriya"])
marks=np.array([99,45,69,29,78])

# --------------Display---------------

print("\n----Student data----")
print("names:",name)
print("marks:",marks)

# --------------Basic analysis--------------

print("total marks:",np.sum(marks))
print("avg marks:",np.mean(marks))
print("highest marks:",np.max(marks))
print("lowest marks:",np.min(marks))

# -------------Topper----------------
top_index =np.argmax(marks)
print("\n🏆 Topper:",name[top_index],"-",marks[top_index])

# -------------Pass/Fail--------------

print("\n-----result-----")
result=np.where(marks>=30,"Pass","Fail")
# res = ["Pass","Pass","Pass","Fail","Pass"]

for i in range(len(name)):
    print(name[i],":",result[i])

# --------------Grade--------------

print("\n-----Grade----")
for i in range(len(marks)):
    m=marks[i]

    if m>=90 and m<=100:
        Grade ="A+"
    elif m>=80 and m<=89:
        Grade ="A"
    elif m>=70 and m<=79:
        Grade ="B1" 
    elif m>=60 and m<=69:
        Grade ="B2"
    elif m>=50 and m<59:
        Grade ="C+"
    elif m>=40 and m<49:
        Grade ="C"
    elif m>=30 and m<39:
        Grade ="D"
    else:
        Grade="F"
    print(name[i], ":", Grade)    
        
# ------------Filtered Data--------------

print("\n----Filtered Data----")

avg=np.mean(marks)

print("\n students scoring above average: ")
print(name[marks>avg],"-",marks[marks>avg])

print("\n students scoring below 40: ")
print(name[marks<40],"-",marks[marks<40])

print("\n--- SORTED DATA ---")

sorted_indices = np.argsort(marks)

print("Names (sorted):", name[sorted_indices])
print("Marks (sorted):", marks[sorted_indices])

print("\n--- SUGGESTION ---")

print("Needs Improvement:")
print(name[marks < 40])

print("\nExcellent Students:")
print(name[marks > 80])







      