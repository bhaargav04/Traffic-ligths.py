import time
a=['EAST','SOUTH','WEST','NORTH']
def manual():
    d=input("Enter the direction:")
    for i in range(0,4):
        if(a[i]==d):
            print(a[i],"GREEN")
        else:
            print(a[i],"RED")
    manual()
def automatic():
    while(True):
        for j in range(0,4):
            for i in range(0,4):
                if(i==j):
                    print(a[i],":GREEN")
                else:
                    print(a[i],":RED")
            print("\n")
            time.sleep(5)
print("1.automatic\n2.manual")
x=eval(input("Enter your choice:"))
if(x==1):
    automatic()
else:
    manual()
