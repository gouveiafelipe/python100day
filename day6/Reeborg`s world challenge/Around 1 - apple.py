def turn_right():
    turn_left()
    turn_left()    
    turn_left()   

def walk():
    put("token")
    move()
    while not object_here():
        if not right_is_clear():
            if front_is_clear() and not wall_in_front():
                move()
            elif wall_in_front() and not right_is_clear():
                turn_left() 
        else: 
             turn_right()
             move()   
              
                
                
                          
walk()

       
            


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
