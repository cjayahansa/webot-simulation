from controller import Robot

# Time step of the simulation
TIMESTEP = 64

#funtions
def driver(arr):
    if arr[1]:
        if arr[0]:
            return 'turn_right'
            #print('turn_right')
        if arr[2]:
            return 'turn_left'
            #print('turn_left')
        else:
            return 'turn_left'
        #return 'you need to do something'
        
        #print('wll ahead')
    else:
        return 'go_straight'
        #print('go straight')

    return 0

# Create the Robot instance
robot = Robot()

# Main function
if __name__ == "__main__":  # <-- should be __main__, not _main_

    # Configure motors
    right_motor = robot.getDevice('MotorR')
    left_motor = robot.getDevice('MotorL')
    
    # Set motors to velocity control mode
    right_motor.setPosition(float('inf'))
    left_motor.setPosition(float('inf'))  # <-- typo: serPosition → setPosition
    
    right_motor.setVelocity(0.0)
    left_motor.setVelocity(0.0)  # <-- typo: serVelocity → setVelocity
    
    # Configure sensors
    front = robot.getDevice('front_sensor')
    right = robot.getDevice('right_sensor')
    left = robot.getDevice('left_sensor')
    
    front.enable(TIMESTEP)
    right.enable(TIMESTEP)
    left.enable(TIMESTEP)
    
    kp = 0.007
    
    

    # Main control loop
    while robot.step(TIMESTEP) != -1:
        #GLOABAL VARIABLE
        SpeedR= 8.0 
        SpeedL= 8.0
    
        val_L=left.getValue()
        val_R=right.getValue()
        val_F=front.getValue()
        err = val_R-val_L
        
        Wall=[val_L < 900, val_F < 600, val_R < 900]
       # print(Wall)
        
        
        disishion = driver(Wall)
        #print(disishion)
        
        if disishion == 'go_straight':
            SpeedR = 4.0 - kp*err
            SpeedL = 4.0 + kp*err
         
         
        if disishion == 'turn_right':
            SpeedR = -5.0
            SpeedL = 5.0
        
        if disishion == 'turn_left':
             SpeedR = 5.0
             SpeedL = -5.0
             
        print(disishion)
        print(val_L,'',val_F,'',val_R,'')
        print(err)
        # Example: Move forward]
        
        right_motor.setVelocity(-1*SpeedR)
        left_motor.setVelocity(-1*SpeedL)
