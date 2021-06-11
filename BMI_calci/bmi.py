def tometre(height,typ):
    ls=''
    if typ == 1: #cms
        return height/100
    elif typ == 2: #inches
        return  height * 0.02539999999997257
    elif typ == 3: #feet and inches
        return (height*12) * 0.02539999999997257
    elif typ == 4:
        return height
i=int(input("Your height is in \nEnter 1 for cms\nEnter 2 for inches\nEnter 3 for feet and inches\nEnter 4 for mts : "))
dic={1:"cms",2:"inches",3:"feet"}
height=float(input("Enter your height :"))
if 1<=i<=3:
    print("Your height is {} in {} , {} in metres".format(height,dic.get(i),round(tometre(height,i),3)))
    height=tometre(height,i)
elif i==4:
    print('Your height is ',height,'mts')
else:
    print('execute again')
weight=float(input("Enter your weight in kgs : "))
print('Your weight is ',weight,'kgs')
def bmi(h,w):
    print(w,h)
    b=w/(h*h)
    print('Body Mass Index(BMI) = ',round(b,3))
    if b <= 18.49:
        print('You are underweight . Have more healthy food yoo')
    elif b <= 24.99:
        print('Great!!! You are healthy')
    elif b <= 29.99:
        print('Overweight , Excercise mannnn')
    else:
        print('Obese , Do consult doctor please')
bmi(height,weight)
print(70/3.125)