#taks10
#Nested if/elif
#70more=first division
#70to50=secand div
# less30=fail
mark=int(input("Enter your marks: "))
if mark>=70:
  print("first division")
elif mark<70 and mark >=50:
  print("secand division")
elif mark<50 and mark>=30:
  print("third division")
else:
  print("fail")

