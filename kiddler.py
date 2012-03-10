from math_kiddler import *
print "hello!!!! Welcome to the world of kiddler"
print "You will be given four choices to work upon..Let's start"
print " 1.Math puzzle\n 2.Word puzzle \n 3.Typing Practice"
choice= raw_input(">")
if choice=="1":
    print "please select among these"
    print "1.Calculation \n2.Variable Finding"
    choice=raw_input(">")
    def func():
        if choice=="1":
            calculation()
        elif choice=="2":
            variable()
        else: 
            print "wrong input, please enter 1 or 2"
            func()
            
        
func()        


