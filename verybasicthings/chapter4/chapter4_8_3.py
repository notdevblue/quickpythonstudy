# https://docs.python.org/3/tutorial/controlflow.html#special-parameters

# 3. Special Parameters

# 기본적으로 매개변수는 함수에게 위치로, 또는 키워드를 통해 명시적으로 전달될 수 있음.
# 가독성과 성능을 위해; 개발자가 함수 정의만 보고, 이것이 위치로 전달되는지, 키워드로 전달되는지, 위치 키워드 둘다 이용해서 전달되는지 알 수 있게, 매개변수가 전달되는 방식을 제한할 수 있음.

# 함수 선언은 아레와 같음

def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    pass

# pos1, pos2 => 위치 한정
# pos_or_kwd => 위치 또는 키워드
# kwd1, kwd2 => 키워드 한정

# / 과 * 는 옵션임. 사용되었을 때, 함수로 매개변수가 어떻게 전달되는지 나타냄. 위치 한정, 위치+키워드, 키워드 한정. 키워드 매개변수는 named parameters 라고도 함.

# 선언에 '/', '*' 가 없다면 매개변수는 위치 또는 키워드로 전달될 수 있음

# 이를 자세히 들어가 보면, 특정한 매개변수는 위치 한정으로 전달되게 할 수 있음.
# 위치 한정이면, 매개변수 순서만 중요함, Keyword 로 전달 안됨.
# / 앞에 위치 한정 매개변수가 위치함. (위치 한정 매개변수가 위치. <omegalul>)
# / 는 논리적으로 위치 한정 매개변수를 다른 매개변수랑 나누는데 사용됨.
# / 없으면 위치 한정이 없는거임.
# / 뒤에 있는건 위치+키워드 또는 키워드 한정임

# 키워드 한정으로 만드려면 * 뒤에 선언하면 됨.

def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

standard_arg(2) # >>> 

# pos_only_arg(arg = 2) # TypeError: got some positional-only arguments passed as keyword argumetns: 'arg'
pos_only_arg(2)

# kwd_only_arg(2) # TypeError: kwd_only_arg takes 0 positional arguments but 1 was given
kwd_only_arg(arg = 2)

combined_example(1, kwd_only=3, standard=2)


# 추가적으로 아레의 함수는 name 과 **kwds 의 name 을 key 로 가지는 것의 충돌이 있을 수 있음
def foo(name, **kwds):
    return 'name' in kwds

# foo(1, **{'a': 2}) # 이런 식으로도 전달이 가능하네

# foo(1, **{'name': 2}) # TypeError: got multiple values for argument 'name'

# 하지만 position-only 를 사용하면 달라짐
def foo(name, /, **kwds):
    return 'name' in kwds

print(foo(1, name="hello"))
# 앞에 name 은 position-only 이기 때문에 **kwds랑 충돌이 없음 (가변 매개변수 이슈)

# 가이드

# * 유저에게 매개변수 이름을 제공하고 싶지 않을 때 positional-only 를 사용
#   파라미터 이름이 특별한 의미가 없을때 유용함:
#       함수 호출 시 인수 순서를 강제하고 싶을 때,
#       위치 기반 매개변수와 가변 인수를 받고 싶을 때
# * 이름이 의미가 있을 때 keyword-only 를 사용.
#   이름을 명시적으로 밝혀 함수 선언을 더욱 이해하기 좋게 만들고 싶거나,
#   유저가 인수 전달을 위치 기반으로 의존하지 않게 하기 위해.
# * API 인 경우, positional-only 를 통해 미래의 매개변수 이름 수정으로 인한 breaking change 를 사전에 막음.
