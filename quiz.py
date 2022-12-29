currt=0
worng=0
while True:
    print("world 1st langages:")
    print("5 ot exit")
    print("1.tamil\n2.englis\n3.girik\n4.chinnes")
    a=int(input("enter ans optinon:"))
    if a==1:
        print("curret")
        currt+=1
    elif a in [2,3,4]:
        print("worng")
        worng+=1
   
    print("what we use in Ai programing langage:")
    print("1.java\n2.python\n3.c#\n4.javascrip")
    b=int(input("what is your ans:"))
    if b==2:
        print("curret")
        currt+=1
    elif b in [1,3,4]:
        print("worng")
        worng+=1
    print("what are the yous of program")
    print("1.develp\n2.manufaction\n3.clearn\n4.stady")
    c=int(input("what is your ans:"))
    if c==1:
        print("currt")
        currt+=1
    elif c in [2,3,4]:
        print("worng")
        worng+=1 
    break
    
print("your currt point is:",currt)
print("your worng point is:",worng)