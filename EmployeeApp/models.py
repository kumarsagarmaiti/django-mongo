from mongoengine import *

connect(
    host="mongodb+srv://kumarsagar_functionup:CjDCkJbsxcpkMf5N@cluster0.fnt89sj.mongodb.net/albanero-demo",
)


class Student(Document):
    name = StringField(max_length=50)
    age = IntField()


# s1 = Student(name="Tara", age=20)
# s1.save()
# print(s1.id)
