#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897

def rotate():

    #Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    # Receiveing the user's input
    print("Let's make a square")
    side = input("length of each side: ")
    
    for i in range (0,4):

  
    	vel_msg.linear.x=0.2
    	vel_msg.linear.y=0
    	vel_msg.linear.z=0
    	vel_msg.angular.x = 0
    	vel_msg.angular.y = 0

    	t0 = float(rospy.Time.now().to_sec())
    	current_distance = 0

       # The turtle gets the linear speed as input as long as it covers the given distance
    	while(current_distance < side):
           
            velocity_publisher.publish(vel_msg)
          
            t1=float(rospy.Time.now().to_sec())
           
            current_distance= 0.2*(t1-t0)
      
        vel_msg.linear.x = 0
       
        velocity_publisher.publish(vel_msg)

        angular_speed = 0.2
        vel_msg.angular.z = angular_speed

        t00 = rospy.Time.now().to_sec()
        current_angle = 0
        relative_angle = 90*2*PI/360
        # The turtle takes a right turn after covering the required distance.
        while(current_angle < relative_angle):
            velocity_publisher.publish(vel_msg)
            t11 = rospy.Time.now().to_sec()
            current_angle = angular_speed*(t11-t00)


        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
    
        # The turtle is brought to a stop after 4 iterations.

       
    rospy.spin()

if __name__ == '__main__':
    try:
        rotate()
    except rospy.ROSInterruptException:
        pass
