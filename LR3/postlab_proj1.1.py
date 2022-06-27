def main():
    from postlab_proj1 import Student
    s = Student("Anna")
    t = Student("Belle")
    a = s.compareEqual(t)
    if a == True:
        print(s.getName(), " is equal to ",t.getName())
    else:
        print(s.getName(), " is not equal to ",t.getName())
    b = s.lessThan(t)
    if b == True:
        print(s.getName(), " is less than ",t.getName())
    else:
        print(s.getName(), " is not less than ",t.getName())
    c = s.greaterThan(t)
    if c == True:
        print(s.getName(), " is greater than ",t.getName())
    else:
        print(s.getName(), " is not greater than ",t.getName())

main()