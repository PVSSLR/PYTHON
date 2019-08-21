from dronekit import connect, LocationGlobalRelative,APIException ,VehicleMode
import exceptions
import math
import argparse
import time 
import socket


def connectMyCopter():
    parser = argparse.ArgumentParser(description='commands')
    parser.add_argument('--connect')
    args = parser.parse_args()

    connection_string = args.connect

    if not connection_string:
	   import dronekit_sitl
           sitl=dronekit_sitl.start_default()
           connection_string=sitl.connection_string()
          

    vehicle = connect(connection_string,wait_ready=True)
    return vehicle



def arm_and_takeoff(targetHeight):


	while vehicle.is_armable!=True:
	      print("Please wait till the Drone to become armable")
	      time.sleep(1)
	print("Drone is now armable")

	vehicle.mode = VehicleMode("GUIDED")

	while vehicle.mode != "GUIDED":
	      print("Wait for guided mode...")
	      time.sleep(1)
	print("Vehicle will be in guided mode in a while")

	vehicle.armed = True
	while vehicle.armed==False:
	      print("...connecting")
	      time.sleep(1)
	print("================================================================================")
	print("|                     PROPS SPINNING INITIATED                                 |")
	print("|            NOTE:-Please check your drone propellers                          |") 
	print("================================================================================")
        vehicle.simple_takeoff(targetHeight) 
        while True:
             print("Current Altitude: %d"%vehicle.location.global_relative_frame.alt)
             if vehicle.location.global_relative_frame.alt>=.95*targetHeight:
                  break
             time.sleep(1)
        print("Target altitude reached!!")   
        return None     

vehicle = connectMyCopter()
arm_and_takeoff(10)


     
