# **Class Method**

### **What is a class method?**
A class method is a method that bound to a class rather than it s object. It doesn't require creation of a class instance.

The difference between a **static method** and a **class method** is:
+ **Static method** knows nothing about the class and just deals with the parameters or only the function that placed inside the class.
+ **Class method** works with the class and it's parameters.

## **When do you use class method?**

### **1. Factory methods**

**Factory methods** are those methods which return a class object (like constructor) for different use cases. It is similar to function overloading in C++. Since, Python doesn't have anything as such, class methods and static methods are used. The example is in `class_method2.py`.

### **2. Correct instance creation in inheritance**

Whenever you derive a class from implementing a factory method as a class method, it ensures correct instance creation of the derived class.

You can create a static method for the above example but the object it creates, will always be hardcoded as Base class.

But, **when you use a class method, it creates the correct instance of the derived class**.

# **Static Method**

### **What is a static method?**

Static methods, much like class methods, are methods that bound to a class rather than its object, or a function that placed inside the class. They do not require a class instance creation. So, are not dependent on the state of the object. The example is in `class_method3.py`.

The difference between a **static method** and a **class method** is:
+ **Static method** knows nothing about the class and just deals with the parameters or only the function that placed inside the class.
+ **Class method** works with the class and it's parameters

## **When do you use static method?**

### **1. Grouping utility function to a class**

Static methods have very limited use case, because like class methods or any other methods within a class, **they cannot access properties of the class itself**. However, **when you need a utility function that doesn't access any properties of a class but makes sense that it belongs to the class**, You need to use static functions. The example is in `static_method1.py`.

### **2. Having a single implementation**

Static methods are used when **we don't want subclasses of a class change/override a specific implementation of a method**. The example is in `static_method2.py`.
