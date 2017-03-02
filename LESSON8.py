def divider():
    while True:
        nums=input('enter 2 digits (format:x y):')
         (x,y)=nums.split()
    try:
        x=int(x)
        y=int(y)
        res=x/y
        print(res)
    except ZeroDivisionError:
        print('ZeroDivisionError')
        print('try again without 0')
    except ValueError:
        print('ValueError')
        print('try again without letters')
    except:
        print("Something went wrong!")
        raise
