x = int(input("Please enter parkjein's height: "))

if x < 156:
    print("Too short!")
elif x > 156:
    print("Too tall!")
else:
    print("Correct!")
# switch case 가 없네
# match case 가 생김 3.10부터
match x:
    case 156:
        print("Wa parkjein height", x, "amazing!")
    case _:
        print("nope")

distros = ["ubuntu", "arch", "gentoo", "void"]
for distro in distros:
    print(distro, len(distro))

users = {"Parkjein": "inactive", "Han": "active", "SeonHanSam": "inactive"} # json?

# python 에서 for 문은 C, Pascal 과는 다르게 
for user, status in users.copy().items():
    if status == "inactive":
        del users[user] # users.items() 로 순회한 경우, 순회 중 수정으로 터짐. 위 방법도 그리 안전해보이지는 않는데 뭔가 무튼 그럼

print(users)

active_users = {}
for user, status in users.items():
    if status == "active":
        active_users[user] = status;

print(active_users)

# range() function
for i in range(5):
    print(i)

print(list(range(5, 10)))
# [5, 6, 7, 8, 9]
print(list(range(0, 10, 3))) # range(start, end, step). [start + step * 0, start + step * 1, ...]
# [0, 3, 6, 9]
print(list(range(-10, -100, -30)))
# [-10, -40, -70]
print(list(range(-10, -15)))
# [] (step 이 1인데 끝이 더 작으면..)

# range(10) -> sequence of length 10. (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

a = ["Hello", "World", "Install", "Gentoo"]
for i in range(len(a)): # sequence 에 인덱스로 접근하려면 range(len(<sequence>)) 가 유용함
    print(i, a[i])

# range 는 list 처럼 작동하지만, 사실 iterate 되는 시퀀스의 연속되는 항목을 반환함, 실제로 리스트를 만들지는 않음, 이로 인해 공간을 절약하게 됨.
# range 와 같은 객채를 iterable 이라고 함.
# 공급이 없을때까지 연속되는 항목을 계속 획득하는 로직인 함수나 구성자에게 알맞음.
# for statement 처럼 구성자를 봤고, iterable 을 받아들이는 함수의 예시진 sum 도 있음

print(sum(range(4))) # -> 6

# https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
# todo