class MyClass:
   # pass #plays a role as a placeholder when nothing needs to be executed
   print("Hello World")

new_instance = MyClass()

#Code above is a class performing instantiation

class MyClass2:
   a = 5

myc = MyClass2()
print(MyClass2.a) # will print 5 to the console

#Code above is an example of attribute reference, referencing a class object

class MyClass3:
   a = 7

   def hello(self): # need self argument otherwise python will throw an error bceause it expects an instance to be passed as the first argument when calling the method
      print("Hello World")

# Instantiate the class
myc2 = MyClass3()

# Call the hello() method on the instance
myc2.hello()