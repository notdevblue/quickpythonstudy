# https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions

# 함수를 정의할 때 매개변수에 기본값을 넣을 수 있음
# 세가지의 형식이 있고, 서로 섞을 수 있음

# 1. 기본 매개변수 값

# 이건 아주 익숙한 거임
def ask_ok(prompt, retries=4, reminder="Please try again!"):
    while True:
        reply = input(prompt)
        if reply in {"y", "ye", "yes"}:
            return True
        if reply in {"n", "no", "nop", "nope"}:
            return False
        retries -= 1
        if retries < 0:
            raise ValueError("Invalid user response")
        print(reminder)

# 이 함수는 여러 방식으로 호출될 수 있음
# ask_ok("Do you really want to quit?")
# 필수 인수만 전달

# ask_ok("OK to overwrite the file?", 2)
# 옵션 인수 하나만 전달

# ask_ok("OK to install Gentoo Linux?", 2, "Com on, only yes or no!")
# 다 전달

# 이 예시는 in 키워드도 제공.
# sequence 가 특정한 값을 가졌는지 확인.

# 기본값은 함수 정의할 때 defining scope 에서 구해짐, 그래서
i = 5
def f(arg = i): # 여기서 arg 의 기본값이 evaluated 됨, 기본값 i 의 값은 5 이기 때문에 arg 는 5임.
    print(arg)  # 근데 이게 되는건 신기하네

i = 6
f()
# 는 5를 출력.

# 기본값은 한번만 초기화됨.
# 기본값이 mutable 한 오브젝트인 경우, 상당히 흥미로운 일이 벌어짐

def f(a, L=[]):
    L.append(a)
    return L

print(f(1)) # L => [1]
print(f(2)) # L => [1, 2]
print(f(3)) # L => [1, 2, 3]
# L 은 한번만 초기화되기 때문에 리스트에 계속 추가되는 것임
# 만약 연속되는 호출에 기본값이 공유되는걸 막고 싶으면, 아레와 같이 함수를 작성할 수 있음

def f(a, L=None):
    if L is None:
        L = []
    L.append(a) # 사실 이거 값 확인을 해야 함, 아니면 'Type' as no attribute 'append' 예외가 발생할 것.
    return L

print(f(1)) # L => [1]
print(f(2)) # L => [2]
print(f(3)) # L => [3]

# 2. 키워드 매개변수

# 함수는 키워드 매개변수를 통해 호출될 수 있음. keyword=value 형식임.

def parrot(voltage, state="a stiff", action="voom", type="Wooyeop P Bass White"):
    print("-- This parrot woudn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- it's", state, "!")

# 하나의 요구되는 매개변수 voltage 와 세가지의 optional 매개변수를 받아들임
# parrot(1000)                                        # 1 positional argument
# parrot(voltage=1000)                                # 1 keyword argument
# parrot(voltage=2000, action="wa sans")              # 2 keyword argument
# parrot(action="wa sans!", voltage=2000)             # 2 keyword argument (with different place from previous call)
# parrot("a million", "bereft of life", "jump")       # 3 positional argument
# parrot("a thousand", state="Installing linux")      # 1 positional, 1 keyword

# 아레의 호출은 유효하지 않음
# parrot()                            # 요구되는 매개변수가 없음 (voltage 는 기본값이 없음)
# parrot(voltage=5.0, "bonjour")      # keyword argument 뒤에 나온 non-keyword argument (이건 syntax error임)
# parrot(110, voltage=220)            # 같은 매개변수에 두가지의 값
# parrot(actor="John Xi Na")          # 없는 키워드

# 함수 호출에서는 키워드 매개변수는 포지셔널 매개변수 뒤에 와야 함.
# 키워드 매개변수는 함수에서 받아들이는 매개변수 중 하나여야 함, 순서는 중요하지 않음
# non-optional 매개변수에도 해당됨. (parrot(voltage=100) 도 유효함)
# 어느 매개변수도 하나 이상의 값을 받을 순 없음. 아레의 예제는 이 규칙으로 인해 실패함.

def function(a):
    pass

try:
    function(0, a=1) # TypError: function() got multiple values for argument 'a'
except Exception as e:
    print(e)

# 함수의 최종 매개변수가 **name 인 경우, dictionary 를 받음, 앞에 정의된 매개변수를 제외한 모든 키워드 매개변수를 가지고 있음
# 또 다른 최동 매개변수인 *name 과 같이 사용될 수 있음, 튜플을 받음. 이는 최종 매개변수 항목에 있는 positional 매개변수를 가짐.

def install_gentoo(distro, *arguments, **keywords):
    print("-- Let's install", distro, "!")
    print("-- I'm sorry. we don't have any space left at disk to install", distro)
    for arg in arguments:
        print(arg)
    for key in keywords:
        print(key, ":", keywords[key])

install_gentoo("Gentoo", "Arch", "FreeBSD", "Void", han="wooyeop", install="Gentoo")

# 함수 호출시 제공한 변수 순서대로 출력되는걸 볼 수 있음.