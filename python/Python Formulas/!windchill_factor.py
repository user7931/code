def f(T,V):
    return 13.12 + 0.6215*T - 11.37*(V**0.16) + 0.3965*T*(V**0.16)
T = 32
V = 2

print ((f(T,V)))