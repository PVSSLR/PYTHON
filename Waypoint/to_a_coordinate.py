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

     
def get_distance_meters(targetLocation,currentLocation):
     dLat = targetLocation.lat - currentLocation.lat
     dLon = targetLocation.lon - currentLocation.lon
     return math.sqrt((dLon*dLon)+(dLat*dLat))*1.113195e5


def goto(targetLocation):
    distanceToTargetLocation = get_distance_meters(targetLocation,vehicle.location.global_relative_frame)
    vehicle.simple_goto(targetLocation)
    while vehicle.mode.name=="GUIDED":
         currentDistance = get_distance_meters(targetLocation,vehicle.location.global_relative_frame)
         if currentDistance<distanceToTargetLocation*0.01:
              print("it has reached its target way point") 
	      time.sleep(2)
              break 
         time.sleep(1)
    return None

wp1 = LocationGlobalRelative(13.060599,80.285531,0)

vehicle = connectMyCopter()
arm_and_takeoff(10)
goto(wp1)

vehicle.mode = VehicleMode("RTL")
while vehicle.mode != 'RTL':
       print("Drone is Returning back")
       time.sleep(1)

vehicle.mode = VehicleMode("LAND")
while vehicle.mode != 'LAND':
       print("Drone is going to enter LAND mode")
       time.sleep(1)
print("vehicle in land mode")

while True:
     time.sleep(1)

     
