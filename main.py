
import os
import sys
import time
import numpy as np
import math
# from xarm.wrapper import XArmAPI
import argparse
from pythonosc import udp_client
from MedusaiClass import robotsTraj
from robotInputs import robotInfo
import random

def probCheck(currProb, arm):
    choices = list(range(len(arm.prob)+1))
    weights = [(100-sum(arm.prob))] + arm.prob
    strum = random.choices(choices, weights=weights, k=1)
    newprob = currProb.copy()
    newprob[arm.robnum] = strum[0]
    print(weights)
    print(newprob)
    return newprob




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Setup the IP address #
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1", help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=5004, help="The port the OSC server is listening on")
    args = parser.parse_args()
    client = udp_client.SimpleUDPClient(args.ip, args.port)

    # Setup the robots #
    Arm = []
    for curInfo in robotInfo:
        Arm.append(robotsTraj(curInfo.IP, curInfo.initPos,curInfo.timeStamp,curInfo.traj,curInfo.Phase))
    input("press Enter to set up")
    for setupArm in Arm:
        setupArm.setupBot(True)
    time.sleep(0.5)

    # Setup the Trajectories #
    sortedTraj = []
    num = 0
    for curArm in Arm:
        curArm.robnum = num
        curArm.trajectories = curArm.makeStrum()
        curArm.Movement = curArm.finalTraj()
        for i in range(len(curArm.tStrums)):
            curArm.prob = robotInfo[num].Probs[i]
            sortedTraj.append([curArm, curArm.tStrums[i]])
            times = sorted(sortedTraj, key=lambda x: x[1])
        num += 1
    t = 0

    choice = [0]*len(Arm)
    input("press enter to start")
    time.sleep(3)

    start_time = time.time()
    while True:
        for moveT in range(len(Arm[0].Movement[0])):
            tcheck = time.time()
            t += 0.004
            for check in sortedTraj:
                if abs((t % check[0].Period) - check[1]) < 0.002:
                    choice = probCheck(choice, check[0])
                    if choice[check[0].robnum] > 0:
                        client.send_message("/strum", [check[0].robnum])
                        print("strum", check[0].robnum)

            debug = []
            for curArm in Arm:
                strumSend = choice[curArm.robnum]
                api = curArm.xArm
                trajToSend = curArm.Movement[strumSend][moveT]

                api.set_servo_angle_j(angles=trajToSend, is_radian=False)
                debug.append(trajToSend)
                client.send_message("/arm{}".format(curArm.robnum), trajToSend)
                # print(choice)
                print(round(t,3))


            tnow = time.time() - start_time
            # input()
            # if tts>0.004:
                # print(tts)
            tloop = time.time()-tcheck
            while abs(tloop) < 0.004:
                tloop = time.time() - tcheck
                # print(tts)
                # tnow = time.time() - start_time
                time.sleep(0.0001)