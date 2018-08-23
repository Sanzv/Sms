def printNumber( arg1, *varNumber ):
   """This prints a variable passed arguments"""
   print ("Output is: ")
   print(arg1)
   for var in varNumber:
      print (var)
   return;
printNumber(10)
printNumber( 70, 60, 50 )
printNumber(11,22,33,44,55,66)