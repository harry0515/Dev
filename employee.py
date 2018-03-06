class employee(object):

    def __init__(self , first, last, number):
        self.first = first
        self.last = last
        self.number = number


    def __str__(self):
        return "%s %s, number:%s" %(self.first, self.last, self.number)

    def __del__(self):
        return "deleted"

    @property
    def fullname(self):
        return "%s %s" %(self.first, self.last)

    @fullname.setter
    def fullname(self,name):
        self.first , self.last = name.split(" ")

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None

    def add_attr (self, att, value):
        self.att = value

    @classmethod
    def add_address(cls):
        cls.address = None


    def add_attrb(self,**kwargs):
        att_dict = {}
        for n in kwargs:
           att_dict[n] = kwargs[n]

        return att_dict






employee.add_address()

x = employee("hari","prasad","3305646583")

print x
print x.fullname

x.fullname = "neel kamal"

print x

del x.fullname

print x

# del x
#
# print x




print x.__dict__
