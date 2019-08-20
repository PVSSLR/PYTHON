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

vehicle = connectMyCopter()
print("================================================================================")
print("WELCOME TO CUSTOMIZED DRONE ATTRIBUTES")
print("================================================================================")
print("APM version: %s"%vehicle.version)
print("Battery   : %s"%vehicle.battery)
print("Velocity  : %s"%vehicle.velocity)
print("Attitude  : %s"%vehicle.attitude)
print("Position  : %s"%vehicle.location.global_relative_frame)
print("Mode      :%s"%vehicle.mode.name)
print("Armed     :%s"%vehicle.armed)
print("Is it good to ARM= %s"%vehicle.is_armable)
print("================================================================================")
print("================================================================================")

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
print("PROPS SPINNING INITIATED")
print("NOTE:-Please check your drone propellers")
print("================================================================================")

     
