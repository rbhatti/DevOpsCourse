# This is how I solved it 
main():
    x  = int(input("m:"))
    print("E:", einstein(x))

def einstein(n):
    return n * 300000000 * 300000000

main()

#2nd method from youtube Video 
# x  = int(input("m:"))
# c = 300000000
# E = x * c * c
# print(E)
