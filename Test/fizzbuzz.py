def fizzbuzz3(n):
    s = ""
    if not n % 3:
        s = "fizz"
    if not n % 5:
        s += "buzz"
    return s if s else str(n)


def fizzbuzz2(n):
    if not n % 3 and not n % 5:
        return "fizzbuzz"
    if not n % 3:
        return "fizz"
    if not n % 5:
        return "buzz"
    return str(n)


def fizzbuzz(n):
    s = "" if n % 3 else "fizz"
    s += "" if n % 5 else "buzz"
    return s if s else str(n)


for i in range(1, 101):
    print(fizzbuzz(i))


def fizzbuzz4(n):
    if n % 3 and n % 5:
        return str(n)
    s = "" if n % 3 else "fizz"
    s += "" if n % 5 else "buzz"
    return s


def convert_timecode(s):
    sec, multiplier = 0, 1
    for num in reversed(s.split(':')):
        sec += int(num) * multiplier
        multiplier *= 60
    return sec


def convert_timecode2(s):
    sec = 0
    for num in s.split(':'):
        sec = sec * 60 + int(num)
    return sec


def convert_timecode3(s):
    sec = 0
    for num in s.split(':'):
        sec *= 60
        sec += int(num)
    return sec

#
# print(fizzbuzz(3))
# print(fizzbuzz(5))
# print(fizzbuzz(15))
# print(fizzbuzz(13))
#
# print(fizzbuzz4(3))
# print(fizzbuzz4(5))
# print(fizzbuzz4(15))
# print(fizzbuzz4(13))
#
#
# print(convert_timecode("10:20:15"))
# print(convert_timecode2("10:20:15"))
# print(convert_timecode3("10:20:15"))
