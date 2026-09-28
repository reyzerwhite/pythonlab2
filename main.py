#print("Hello world")

# name="Sergey"
# age=28
# height=1.82
# is_student=False
# print(type(name),type(age),type(height),type(is_student))


# name=input("Введите имя: ")
# sec_name=input("Введите фамилию: ")
# age=int(input("Введите возраст: "))
# height=float(input("Введите рост: "))
# print(name,type(name))
# print(sec_name,type(sec_name))
# print(age,type(age))
# print(height,type(height))

# a=15
# b=4
# print(a+b,a-b,a*b,a/b,a//b,a%b,a**b)

# a=float(input())
# b=float(input())
# summ=a+b
# razz=a-b
# mult=a*b
# dell=a//b
# print(f"сумма: {summ}")
# print(f"разность: {razz}")
# print(f"умножение: {mult}")
# print(f"деление: {dell}")

# for i in range(0,21,2):
#     print(i)

# count=10
# while count>0:
#     print(count)
#     count=count-1
#     if count==0:
#         print("цикл завершен")

# import math
# radius=int(input())
# sqr=math.sqrt(radius)
# l=2*math.pi*radius
# s=math.pi*radius**2
# print(l,s,sqr)

# a=int(input("Введите число: "))
# if a>0:
#     print("положительное")
# elif a<0:
#     print("отрицательное")
# else:
#     print("равно нулю")
# if a%2==0:
#     print("четное")
# else:
#     print("нечетное")

# age=int(input("Возраст: "))
# has_acces=input("Допуск имеется: ")=="True"
# if age>=18 and has_acces:
#     print("Доступ разрешён")
# else:
#     print("Доступ запрещён")

n=int(input())
summ=float(0)
for i in range(0,n):
    m=float(input())
    summ+=m
print(summ,summ/n)
