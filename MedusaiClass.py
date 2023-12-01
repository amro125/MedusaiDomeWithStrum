import numpy as np
import math
import time
from xarm.wrapper import XArmAPI

# Timing Mods #
headS = 2
baseamp = 350
amp5 = headS * 8.6
amp3 = 0.4 * amp5
amp1 = 0.2 * amp5
amp5extra = 30
amptwist = 200
headS5 = 0.045 * amptwist * headS
headS3 = 0.09 * amptwist * headS
global stepT
stepT = 0.004

class robotsTraj:
    def __init__(self, IPadress, startPos, tStrums,trajInput, phase = 0):
        self.arm = IPadress
        self.initPos = startPos
        self.phase = phase
        self.tStrums = tStrums

        self.beginPos = self.dancepos(0)
        self.xArm = XArmAPI(self.arm)
        self.trajInput = trajInput
        self.Period = 2*headS3



    
    def setupBot(self,enableState):
        self.xArm.set_simulation_robot(on_off=False)
        self.xArm.motion_enable(enable=enableState)
        self.xArm.clean_warn()
        self.xArm.clean_error()
        self.xArm.set_mode(0)
        self.xArm.set_state(0)
        self.xArm.set_servo_angle(angle=self.beginPos, wait=True, speed=20, acceleration=0.5, is_radian=False)
        time.sleep(0.1)
        self.realTimeMode()
    
    def realTimeMode(self):
        self.xArm.set_mode(1)
        self.xArm.set_state(0)


    def probabilityChoice(self):
        choices = list(range(len()))


    def fifth_poly(self, q_i, q_f, v_i, vf, t):
        # time/0.005
        traj_t = np.arange(0, t, stepT)
        dq_i = v_i
        dq_f = vf
        ddq_i = 0
        ddq_f = 0
        a0 = q_i
        a1 = dq_i
        a2 = 0.5 * ddq_i
        a3 = 1 / (2 * t ** 3) * (20 * (q_f - q_i) - (8 * dq_f + 12 * dq_i) * t - (3 * ddq_f - ddq_i) * t ** 2)
        a4 = 1 / (2 * t ** 4) * (30 * (q_i - q_f) + (14 * dq_f + 16 * dq_i) * t + (3 * ddq_f - 2 * ddq_i) * t ** 2)
        a5 = 1 / (2 * t ** 5) * (12 * (q_f - q_i) - (6 * dq_f + 6 * dq_i) * t - (ddq_f - ddq_i) * t ** 2)
        traj_pos = a0 + a1 * traj_t + a2 * traj_t ** 2 + a3 * traj_t ** 3 + a4 * traj_t ** 4 + a5 * traj_t ** 5
        for i in range(len(traj_pos)):
            traj_pos[i] = round(traj_pos[i],5)
        return traj_pos

    def dancevel(self, t):
        j_angles = [0, 0, 0, 0, 0, 0, 0]
        strike = (math.pi / headS3) * (math.cos((math.pi / headS3) * (t)))
        two = (math.pi / headS) * math.cos(math.pi / headS) * (t - 0.75*headS-self.phase*headS)
        three = (math.pi / headS3) * (math.cos((math.pi / headS3) * (t-self.phase*headS3)))
        four = (math.pi / headS) * math.cos((math.pi / headS) * (t-0.5*headS-self.phase*headS))
        five = (math.pi / headS5) * math.cos((math.pi / headS5) * (t-self.phase*headS5))
        six = (math.pi / headS) * math.cos((math.pi / headS) * (t-self.phase*headS))
        seven = (math.pi / headS5) * math.cos((math.pi / headS5) * (t-self.phase*headS5))

        # j_angles[0] = -baseamp * strike
        j_angles[1] = -amp1 * two
        j_angles[2] = +amptwist * three
        j_angles[3] = +amp3 * four
        j_angles[4] = +amptwist * five
        j_angles[5] = -amp5 * six
        j_angles[6] = - amp5 * seven
        return j_angles

    def dancepos(self, t):
        j_angles = self.initPos.copy()
        strike = (math.sin((math.pi / headS3) * (t)))
        two = math.sin((math.pi / headS) * (t - 0.75*headS-self.phase*headS))
        three = math.sin((math.pi / headS3) * (t-self.phase*headS3))
        four = math.sin((math.pi / headS) * (t-0.5*headS-self.phase*headS))
        five = math.sin((math.pi / headS5) * (t-self.phase*headS5))
        six = math.sin((math.pi / (headS) * (t-self.phase*headS)))
        seven = math.sin((math.pi / (headS5) * (t-self.phase*headS5)))

        # j_angles[0] = startp[0] - baseamp * strike
        j_angles[1] = self.initPos[1] - amp1 * two
        j_angles[2] = self.initPos[2] + amptwist * three
        j_angles[3] = self.initPos[3] + amp3 * four
        j_angles[4] = self.initPos[4] + amptwist * five
        j_angles[5] = self.initPos[5] - amp5 * six
        j_angles[6] = self.initPos[6] - amp5 * seven
        if abs(j_angles[6]) >= 360:
            j_angles[6] = (j_angles[6]/abs(j_angles[6]))*359.8
        for i in range(len(j_angles)):
            j_angles[i] = round(j_angles[i],5)
        return j_angles

    def danceblock(self,tS, tEnd):
        tArr = np.arange(tS,tEnd, stepT)
        blockd = []
        for t in tArr:
            blockd.append(self.dancepos(t))
        return blockd

    def matlabparser(self, traj, startP, v_i, v_f):
    # format is [[[pos1,pos2],[time1,time2]],[[JOINT2pos1,pos2],[time1,time2]]]
        trajblock = []
        j = 0
        for joint in traj:
            # format is now at [[pos1,pos2],[time1,time2]]
            jointblock = np.empty([0, 1])
            if len(joint[0]) == 1:
                iter = 1
            else:
                iter = len(joint[0])
            for i in range(iter):
                if i == 0:
                    v = v_i[j]
                    vf = 0
                    qi = startP[j]
                    qf = joint[0][i]
                elif i == iter - 1:
                    v = 0
                    vf = v_f[j]
                    qi = joint[0][i - 1]
                    qf = joint[0][i]
                else:
                    v = 0
                    vf = 0
                    qi = joint[0][i - 1]
                    qf = joint[0][i]
                timescale = sum(joint[1]) * joint[1][i] / sum(traj[0][1])
                step = self.fifth_poly(qi, qf, v, vf, timescale)
                jointblock = np.append(jointblock, step)
            # print("JOINT BLOCK",j,len(jointblock))
            trajblock.append(jointblock)
            j += 1
        # print(len(trajblock[3]))
        #fix lengths
        lengths = []
        for i in trajblock:
            lengths.append(len(i))
        size = min(lengths)
        # reformat
        reformat = []
        for i in range(size):
            row = []
            # for q in range(7):
            # print(len(trajblock[q]))
            for j in range(7):
                row.append(trajblock[j][i])
            reformat.append(row)
        return reformat

    def makeStrum(self):
        trajectory = []
        for i in range(len(self.tStrums)):
            struminput = self.trajInput[i]
            tCur = self.tStrums[i]
            endT = tCur + sum(struminput[0][1])
            endpos = self.dancepos(endT)
            for j in range(7):
                struminput[j][0][-1] = endpos[j]
            startP = self.dancepos(tCur)
            vstruminit = self.dancevel(tCur)
            vfinal = self.dancevel(endT)
            play = self.matlabparser(struminput,startP,vstruminit,vfinal)
            noplay = []
            tnoplay = np.arange(tCur, endT, stepT)
            for time in tnoplay:
                noplay.append(self.dancepos(time))
            # trajectoryBlock = [play]
            trajectory.append(play)
        return trajectory

    def finalTraj(self):
        # timeArr = self.tStrums
        greenzone = [[0,0]]
        for i in range(len(self.tStrums)):
            greenzone.append([self.tStrums[i],self.tStrums[i]+9])
        greenzone.append([self.Period,self.Period])
        # timeArr.append(self.Period)
        interpoints= []
        for i in range(len(greenzone)-1):
            iterations = []
            toAdd = self.danceblock(greenzone[i][1],greenzone[i+1][0])
            # for j in range(len(self.trajectories)):
            iterations.append(toAdd)
            interpoints.append(toAdd)

        # interweave in betweens and finals #
        result = [None] * (len(interpoints) + len(self.trajectories))
        result[::2] = interpoints
        result[1::2] = self.trajectories
        strumoutput = []
        for i in result:
            strumoutput = strumoutput+ i

        # shift trajectory by phase #
        # the phase factor indicates how much of the trajectory will be put in front of the section
        n = int(self.phase*self.Period/stepT)
        strumresultoffset = strumoutput[-n:] + strumoutput[:-n]

        nostrum = self.danceblock(0,self.Period)
        nostrumoffset = nostrum[-n:] + nostrum[:-n]
        resultoffset = [nostrumoffset,strumresultoffset]
        resultoffset = [nostrum, strumoutput]

        return resultoffset


            # greenzone.append([timeArr[i], timeArr[i]])







    # def createStrumLoop

# r1 = Robots(2,7,4,1,2)
# r1.test2()
# print(r1.startT)
# print(r1.strum8)
