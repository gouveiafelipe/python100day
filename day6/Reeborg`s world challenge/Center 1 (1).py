def turn_right():
    turn_left()
    turn_left()    
    turn_left()   
 

def walk():
    if not right_is_clear():
        if front_is_clear() and not wall_in_front():
            move()
        elif wall_in_front() and not right_is_clear():
            turn_left() 
    else: 
            turn_right()
            move()
                                
def journey3():
    put("token")
    while not wall_in_front():
        move()
    if wall_in_front():
        put("token")
        for i in range(2):
                turn_left()
        move()
    while not object_here():
        move()
        if object_here():
            for i in range(2):
                turn_left()
            take()
            move()
            put("token")
            move()    
    if object_here():
        for i in range(2):
            turn_left()
        take()
        move()
        put("token")
        take()
journey3()             
        
    
  
    
 
                        

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
