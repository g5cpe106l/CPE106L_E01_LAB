class Student(object):
    def __init__(self,s):
        self.s = s

    def getName(self):
        return self.s


    def compareEqual(name1,name2):
        if name1.s == name2.s:
            return True
        else:
            return False

    def lessThan(name1,name2):
        if name1.s < name2.s:
            return True
        else:
            return False

    def greaterThan(name1,name2):
        if name1.s > name2.s:
            return True
        else:
            return False




