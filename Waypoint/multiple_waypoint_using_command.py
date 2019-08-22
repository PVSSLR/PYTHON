from dronekit import connect, LocationGlobalRelative,APIException ,VehicleMode,Command
import exceptions
import math
import argparse
import time 
import socket
from pymavlink import mavutil


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

wphome = vehicle.location.global_relative_frame

cmd1 = Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,0,0,0,0,0,0,wphome.lat,wphome.lon,wphome.alt)
cmd2 = Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,0,0,0,0,0,0,13.060544,80.284953,15)
cmd3 = Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,0,0,0,0,0,0,13.060084,80.284872,10)
cmd4 = Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH,0,0,0,0,0,0,0,0,0)


##download commands

cmds = vehicle.commands
cmds.download()
cmds.wait_ready()


##will clear the command lists
cmds.clear()

##Add in our new commands 
cmds.add(cmd1)
cmds.add(cmd2)
cmds.add(cmd3)
cmds.add(cmd4)

##upload the command 
vehicle.commands.upload()

arm_and_takeoff(10)
print("arm and takeoff done")
vehicle.mode = VehicleMode("AUTO")
while vehicle.mode!="AUTO":
      time.sleep(.2)
while vehicle.location.global_relative_frame.alt>2:
      print("Drone is executing and we can still run code")
      time.sleep(2)






























     
