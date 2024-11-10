def example1():
    example1_0 = "my name - {arg1}, my age - {arg2}"
    print(example1_0.format(arg1="uriy", arg2=11))

def example2():
    name ="uriy"
    age=11
    example2_0 = f"my name - {name}, my age - {age}"
    print(example2_0)

def example3(name, age):
    example1_0 = "my name - {arg1}, my age - {arg2}"
    print(example1_0.format(arg1=name, arg2=age))

def example4(name,age):
    example2_0 = f"my name - {name}, my age - {age}"
    print(example2_0)

if __name__ == "__main__":
    example1()
    example2()
    example3(name="uriy",age=11)
    example3(name="kolya",age=12)
    example4(name="Татьяна",age=36)
    example4(name="Женя",age=14)