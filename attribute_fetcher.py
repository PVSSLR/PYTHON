from dronekit import connect, LocationGlobalRelative,APIException ,VehicleMode
import exceptions
import math
import argparse
import time 
import socket


def connectMyCopter():
    parser = argparse.ArgumentParser(description='commands')
    parser.add_argument('--c')
    args = parser.parse_args()

    connection_string = args.connect

    if not connection_string:
	   import dronekit_sitl
           sitl=dronekit_sitl.start_default()
           connection_string=sitl.connection_string()
          

    vechile = connect(connection_string,wait_ready=True)
    return vechile

vechile = connectMyCopter()
