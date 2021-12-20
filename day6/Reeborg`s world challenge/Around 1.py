def turn_right():
    turn_left()
    turn_left()    
    turn_left()   

def walk():
    put("token")
    move()
    while not object_here():
        if front_is_clear() and not wall_in_front():
            move()
            if wall_in_front():
                turn_left() 
            

walk()

def walk_stop():
    if not object_here():
        walk()
    else:
        done()
        


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
