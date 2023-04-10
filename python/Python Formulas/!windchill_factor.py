T = input("Temprature: ")
V = input("Velocity: ")

def f(T,V):
    return 13.12 + 0.6215*T - 11.37*(V**0.16) + 0.3965*T*(V**0.16)

print ("The windchill factor is: ", (f(T,V))) #I hope this works lol if it does :)