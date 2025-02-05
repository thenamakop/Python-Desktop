# Rigth angled triangle/ right half pyramid
#for i in range (0,6,1):
 #   for j in range (0,i+1,1):
  #      print("*",end=" ")
   # print("\n")

# inverse triangle/ left half pyramid

#for i in range (0,6,1):
 #   for j in range (0,6-i,1):
  #      print("*",end=" ")
   # print("\n")

# equilateral triangle
#for i in range (0, 5, 1):
 #   print(" "*(5-i), end = " ")
  #  for j in range (0, i+1, 1):
   #     print("*", end = " ")
    #print("\n")

# Inverse Equilateral Triangle
#for i in range(5,-1,-1):
#    print(" "*(5-i), end = " ")
 #   for j in range(0, i+1, 1):
  #      print("*", end = " ")
   # print("\n")

# Square
#for i in range(0, 5, 1):
 #   for j in range(0, 5, 1):
  #      print("*", end = " ")
   # print("\n")

# Horizontal rectangle
#for i in    range(0, 5, 1):
 #   for j in range(0, 7 ,1):
  #      print("*", end = " ")
   # print("\n")

# Hollow Equilateral Triangle
#for i in range(0,5,1):
 #   print(" "*(5-i), end = " ")
  #  for j in range(0,i+1,1):
   #     if ( i == 4 or j == 0 or j == i):
    #        print("*", end = " ")
     #      print(" ", end =" ")
    #pri#nt("\n")

#Alphabetical triangle

#for i in range(65,70,1):
 #   print(" "*(70-i), end = " ")
  #  for j in range(65,i+1,1):
   #     print(chr(i), end=" ")
    #print("\n")

#for i in range(0,5,1):
 #   c=65
  #  print(" "*(5-i),end="")
   # for j in range(0,i+1,1):
    #    print(chr(c),end=" ")
     #   c=c+1
    #print("\n")    
    
# Diamond Pattern
#for i in range (0, 3, 1):
 #   print(" "*(3-i), end = " ")
  #  for j in range (0, i+1, 1):
    #    print("*", end = " ")
   # print("\n")
#for i in range(3,-1,-1):
 #   print(" "*(3-i), end = " ")
  #  for j in range(0, i+1, 1):
   #     print("*", end = " ")
    #print("\n")
    
# Hollow Diamond
#for i in range (0, 3, 1):
 #   print(" "*(3-i), end = " ")
  #  for j in range (0, i+1, 1):
   #     if (j ==0 or j==2 or i == 0  ):
    #        print("*", end = " ")
     #   else:
      #      print(" ", end= " ")
    #print("\n")
#for i in range(3,-1,-1):
 #   print(" "*(3-i), end = " ")
  #  for j in range(0, i+1, 1):
   #     if (j == 0 or j == i or i == 0  ):
    #        print("*", end = " ")
     #   else:
      #      print(" ", end = " ")
    #print("\n")

#Palindrome Equilateral Triangle
#for i in range(1,6,1):
 #   print(" "*(6-i), end=" ")
  #  for j in range(0,i,1):
   #     print(i-j, end=" ")
    #
    #for k in range(2,i+1,1):
     #   print(k, end=" ")
    #print("\n")

# Rhombus
#for i in range(0,7,1):
 #   print(" "*i,end="")
  #  for j in range(0,5,1):
   #     print("*", end = " ")
    #print("\n")        

#Butterfly Pattern
#for i in range(0,5,1):
 #   for j in range(0,i+1,1):
  #      print("*",end=" ")
   # print("  "*(5-i-1),end="")
    #for k in range(0,i+1,1):
     #   print("*",end=" ")
    #print("\n")
#for i in range(3,-1,-1):
 #   for j in range(0,i+1,1):
  #      print("*",end=" ")
   # print("  "*(5-i-1),end="")
    #for k in range(0,i+1,1):
    #     print("*",end=" ")
    #print("\n")

#Reverse number triangle
x = 0 
for i in range(5,-1,-1):
    print(" "*(5-i), end="")
    for j in range(0+x, i+1+x, 1):
        print(j, end=" ")
    x = x +1
    print("\n")    
    