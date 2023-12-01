import numpy as np
from robotInputs import robotInfo


class Robots:
    def __init__(self, IPadress,startPos, tStrums, phase = 0):
        self.arm = IPadress
        self.initPos = startPos
        self.phase = phase
        self.strum1 = []
        self.strum2 = []
        self.tStrums = tStrums
        self.total = []
        self.idk = self.test3(3)

        # self.startT = startT
        # self.endT = startT + sum(startPos[0])

    def test3(self, number):
        print(number)
        return [number + 3, 3]

    def test2(self):
        for num in self.tStrums:
            self.instant = num
            self.total.append(self.test3(num))



traj = robotInfo
print(robotInfo[0].timeStamp)
r1 = Robots(1,3,[3,5],2)
print(r1.idk)
input()

r1.test2()
r1.total.append(7)
print(r1.total)


r2 = Robots(2,3,[2,4],2)
# r2.test2()
# print(r1.noclue)

sorter = []

arms = [r1 ,r2]

for arm in arms:
    for i in arm.tStrums:
        arm.total.append(arm.test3(i))
        sorter.append([arm, i])
print(arms[0].total)

times = sorted(sorter,key = lambda x: x[1])
# print(times[3][0].phase)

