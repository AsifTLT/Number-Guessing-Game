import random 

top_of_range = input("type a number : ")

if top_of_range.isdigit():
    
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("print type a larger number than 0 next time.")
        quit()
else:
    print("print type number next time.")
    quit()    
random_number = random.randint(0, top_of_range)
# print(random_number)
while True:
    
    
    break
    

