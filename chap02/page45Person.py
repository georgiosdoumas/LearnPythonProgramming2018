class Person():
    def __init__(me,age):  # again instead of using the common "self", I used the "me", just to show that we can use whatever we want
        me.page=age      # the attribute of the class is page (from person age), and the passed parameter is age

geo = Person(46)
print(geo.page)
print(id(geo))
print(id(geo.page))
geo.page = 35
print(id(geo))
print(id(geo.page))

