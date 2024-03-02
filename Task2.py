r#taks10
#Nested if/elif
#70more=A grade
#70to50=B grade
#50to40=C grade
#40to30=D grade 
# less30=fail
mark=int(input("Enter your marks: "))
if mark>=70:
  print("A grade")
elif mark<70 and mark >=50:
  print("B grade")
elif mark<50 and mark>=30:
  print("C grade")
elif mark<30 and mark>=20:
  print("D grade")
else:
  print("fail")
  
