# chk_character
def main():
    pass
    n=input().split()
    inp=input().split()
    chk=n[1]
    flag=0
    for i in inp:
        if(chk == i):
            flag+=1
    if(flag==1):
        print("yes")
    else:
        print("no")
if __name__ == '__main__':
    main()
