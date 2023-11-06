#lab 3.3

pi = 'global pi variable' 
  
def outer():
    pi = 'enclosed pi variable'
    def inner():
        pi = 'local pi variable'
        print(pi) # local pi
    inner()
    print(pi) #enclosed pi
  
outer()
print(pi) # global pi
