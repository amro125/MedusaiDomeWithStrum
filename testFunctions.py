import math
import numpy as np
import matplotlib.pyplot as plt
import random

global headS
test = np.arange(0,8,2)
print(test)
def dancepos(initPos, t):
    # headS = 4
    phase = 0.25
    baseamp = 350
    amp5 = headS * 8.6
    amp3 = 0.4 * amp5
    amp1 = 0.2 * amp5
    amp5extra = 30
    amptwist = 200
    headS5 = 0.045 * amptwist * headS
    headS3 = 0.09 * amptwist * headS
    # print(headS3)
    # print(headS)

    j_angles = initPos.copy()
    strike = (math.sin((math.pi / headS3) * (t)))
    two = math.sin((math.pi / headS) * (t - 0.75 * headS - phase * headS))
    three = math.sin((math.pi / headS3) * (t - phase * headS3))
    four = math.sin((math.pi / headS) * (t - 0.5 * headS - phase * headS))
    five = math.sin((math.pi / headS5) * (t - phase * headS5))
    six = math.sin((math.pi / (headS) * (t - phase * headS)))

    # j_angles[0] = startp[0] - baseamp * strike
    j_angles[1] = round(initPos[1] - amp1 * two, 5)
    j_angles[2] = round(initPos[2] + amptwist * three,5)
    j_angles[3] = round(initPos[3] + amp3 * four, 5)
    j_angles[4] = round(initPos[4] + amptwist * five, 5)
    j_angles[5] = round(initPos[5] - amp5 * six, 5)
    j_angles[6] = round(initPos[6] - (amptwist * five + amptwist * three - baseamp * strike), 5)
    if abs(j_angles[6]) >= 360:
        j_angles[6] = (j_angles[6] / abs(j_angles[6])) * 359.8
    return j_angles


# period = (0.9*200*headS/10)*2
# print(period)
# initpos = [0,0,0,0,0,0,0]
# timearray = np.arange(0, period, 0.1)
# joints = []
# for t in timearray:
#     joints.append(dancepos(initpos,t))
#
# print(dancepos(initpos,0-.1))
# print(dancepos(initpos,period-0.1))
# joints = np.array(joints)
# graph = joints.transpose()
# i = 0
# for y in graph:
#     plt.plot(timearray,y,label = i)
#     plt.legend()
#     i+=1
# plt.show()
# # plt.legend()
#
#
# import random
#
# # sampleList = [100, [4,200], [300,5], [400,5], [500,3]]
# # sampleList.insert(0,999)
# # print(sampleList)
# list1 = [[1,3],2,3]
# list2 = [8,[9,7]]
# result = [None]*(len(list1)+len(list2))
# result[::2] = list1
# result[1::2] = list2
# print(result)
# timeArr = list.copy()
# for i in range(len(list)):
#     timeArr.insert( i + 1,list[i] + 9)
# print(timeArr)
# randomList = random.choices(test, weights=[50, 50], k=1)

# print(randomList[0])
n = 2
test_list = [1, [2,5,6] , 3, 4, [5,6,65]]
test_list = test_list[-n:] + test_list[:-n]
print(test_list)