for row in range(7):
  for col in range(5):
    if(col==0 or col==4)  or (row==3 and (col>0 or col<4)):
        print("*",end="")
    else:
      print(end=" ")
  print()#H

print("   ")

for row in range(7):
  for col in range(5):
    if ((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
      print("*",end="")
    else:
      print(end=" ")
  print()#A

print("   ")

for row in range(7):
  for col in range(5):
    if (col==0 or col==3 and col==0) or ((row==0 or row==3) and (col>0 and col<3)) or (row==1 or row==2) and col==4:
       print("*",end="")
    else:
      print(end=" ")
  print()#P

print("   ")

for row in range(7):
  for col in range(5):
    if (col==0 or col==3 and col==0) or ((row==0 or row==3) and (col>0 and col<3)) or (row==1 or row==2) and col==4:
       print("*",end="")
    else:
      print(end=" ")
  print()#P

print("   ")

for row in range(7):
  for col in range(5):
    if (col==0 and col<4 and col>5 or col==4) or (row==3 and (col>0 or col<4)) or (row==6 or col==0 and col==4) or (col==0 and row==0 or row==3) or (row==1 or row==2) and col==0:
      print("*",end="")
    else:
      print(end=" ")
  print()#Y

print("   ")

for row in range(7):
  for col in range(5):
    if(col==0) or (col==4 and (row!=0 and row!=3 and row!=6)) or ((row==0 or row==3 or row==6) and (col>0 and col<4)):
      print("*",end="")
    else:
      print(end=" ")
  print()#B

print("   ")

for row in range(7):
  for col in range(5):
    if col==2 or (row==0) or row==6:
       print("*",end="")
    else:
      print(end=" ")
  print()#I

print("   ")

for row in range(7):
  for col in range(5):
    if (col==0 or col==3 and col==0) or ((row==0 or row==3) and (col>0 and col<3)) or(row==1 or row==2) and col==4 or (row==4 or row==5 or row==6) and col==4:
       print("*",end="")
    else:
      print(end=" ")
  print()#R

print("   ")

for row in range(6):
  for col in range(5):
    if col==2 or (row==0):
      print("*",end="")
    else:
      print(end=" ")
  print()#T

print("   ")

for row in range(7):
  for col in range(5):
    if(col==0 or col==4)  or (row==3 and (col>0 or col<4)):
        print("*",end="")
    else:
      print(end=" ")
  print()#H

print("   ")

for row in range(7):
  for col in range(5):
     if(col==0 or col==4)or row==0 or row==6:
        print("*",end="")
     else:
      print(end=" ")
  print()#D


print("   ")

for row in range(7):
  for col in range(5):
    if ((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
      print("*",end="")
    else:
      print(end=" ")
  print()#A

print("   ")

for row in range(7):
  for col in range(5):
    if (col==0 and col<4 and col>5 or col==4) or (row==3 and (col>0 or col<4)) or (row==6 or col==0 and col==4) or (col==0 and row==0 or row==3) or (row==1 or row==2) and col==0:
      print("*",end="")
    else:
      print(end=" ")
  print()#Y












  



















