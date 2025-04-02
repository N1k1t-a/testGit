

def div_safe(a, b):
    print("start for", [a, b])

    try:
        return a/b

    except TypeError as e:
        print("ooops, type error:", e, repr(e))

    print("leaving for", [a, b])


print(div_safe(1, 2))
print(div_safe(10, 2))
print(div_safe(10, "2"))
