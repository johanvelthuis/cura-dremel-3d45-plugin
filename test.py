#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#voor een groot deel gebaseerd op:
#https://blog.cluster.fail/monitoring-the-dremel-3d45-via-network


import os
import sys
import requests
import json
import threading

print(sys.version)
ip_address = "10.0.0.114"
data = 'getprinterstatus'
file = "/Users/johan/Downloads/cabinet.gcode"

debug = True

def getprinterstats():
    #threading.Timer(3.0, getprinterstats).start()
    # get data and parse it
    url = "http://" + ip_address + ":80/command"
    r = requests.post(url=url, data=data)
    resp = r.text
    json_string = r.text
    encoded = json.loads(json_string)
    jobname = encoded['jobname'].strip('.gcode')
    progress = str(encoded['progress'])
    remaining_seconds = int(encoded['remaining'])
    elapsed_seconds = int(encoded['elaspedtime'])
    filament_type = encoded['filament_type ']
    plate_target_temp = str(encoded['buildPlate_target_temperature'])
    plate_temp = str(encoded['platform_temperature'])
    nozzle_target_temp = str(encoded['extruder_target_temperature'])
    nozzle_temp = str(encoded['temperature'])
    layer = str(encoded['layer'])
    chamber_temp = str(encoded['chamber_temperature'])

    # write to file
    if not debug:
        f = open("printer.txt", "w")
        f.write('Current Job: ' + jobname + '\n')
        f.write('Progress: ' + progress + '%' + '\n')
        if remaining_seconds > 0:
            remaining_seconds = str(remaining_seconds)
            f.write('Time Remaining: ' + remaining_seconds + 's' + '\n')
        else:
            pass
        elapsed_seconds = str(elapsed_seconds)
        f.write('Time Elapsed: ' + elapsed_seconds + 's' + '\n')
        f.write('Filament: ' + filament_type + '\n')
        f.write('Nozzle Temp: ' + nozzle_temp + '°C (current) ' + '/ ' + nozzle_target_temp + '°C (target)' + '\n')
        f.write('Plate Temp: ' + plate_temp + '°C (current) ' + '/ ' + plate_target_temp + '°C (target)' + '\n')
        f.write('Chamber Temp: ' + chamber_temp + '°C (current)' + '\n')
        f.close()
    else:
        print(encoded)
        print('Current Job: ' + jobname + '\n')
        print('Progress: ' + progress + '%' + '\n')
        if remaining_seconds > 0:
            remaining_seconds = str(remaining_seconds)
            print('Time Remaining: ' + remaining_seconds + 's' + '\n')
        else:
            pass
        elapsed_seconds = str(elapsed_seconds)
        print('Time Elapsed: ' + elapsed_seconds + 's' + '\n')
        print('Filament: ' + filament_type + '\n')
        print('Nozzle Temp: ' + nozzle_temp + '°C (current) ' + '/ ' + nozzle_target_temp + '°C (target)' + '\n')
        print('Plate Temp: ' + plate_temp + '°C (current) ' + '/ ' + plate_target_temp + '°C (target)' + '\n')
        print('Chamber Temp: ' + chamber_temp + '°C (current)' + '\n')

def printjob(filepath):
    #if getprinterstats()==True:
        url = "http://" + ip_address + ":80/print_file_uploads"
        files = {'print_file': open(filepath,'rb')}
        print("Komen we hier?")
        r = requests.post(url=url, files=files)
        print("Komen we hier???")
        json_string = r.text
        encoded = json.loads(json_string)
        print(encoded)
        message = str(encoded['message']);
        if message == "success":
            print("uploaden lijkt gelukt")
            url = "http://" + ip_address + ":80/command"
            data = "PRINT=" + os.path.basename(filepath)
            print("JV DATA" + data)
            r = requests.post(url=url, data=data)
            json_string = r.text
            encoded = json.loads(json_string)
            print(encoded)
            message = str(encoded['message']);
            if message == "success":
                print("ga nu printen...")
                return True
            else:
                print("Er is een error")
                return False


#printjob(file)
getprinterstats()


