class JustCounter:
   __secretCount = 0

   def count(self):
      self.__secretCount += 1
      print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()

# Error because of data hiding
#print(counter.__secretCount)

print(counter._JustCounter__secretCount)
