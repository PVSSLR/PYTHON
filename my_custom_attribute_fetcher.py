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
          

    vechile = connect(connection_string,wait_ready=True)
    return vechile

vechile = connectMyCopter()
print("APM version: %s"%vechile.version)
print("Battery   : %s"%vechile.battery)
print("Velocity  : %s"%vechile.velocity)
print("Attitude : %s"%vechile.attitude)
print("Position  : %s"%vechile.location.global_relative_frame)
print("Mode       :%s"%vechile.mode.name)
print("Armed      :%s"%vechile.armed)
print("Is it good to ARM= %s"%vechile.is_armable)


