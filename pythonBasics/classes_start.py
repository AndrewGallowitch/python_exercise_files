#
# Example file for working with classes
#

class myClass():
  def method1(self):
    print("myClass method1")
  
  def method2(self, someString):
    print("myClass method2" + someString)

class anotherClass(myClass):
  def method1(self):
    myClass.method1(self)
    print("anotherClass method1")
  
  def method2(self, string):
    print("anotherClass method2" + string)

def main():
  c = myClass()
  c.method1()
  c.method2(" This is a string from the super class")
  
  c2=anotherClass()
  c2.method1()
  c2.method2(" This is drew")

if __name__ == "__main__":
  main()
