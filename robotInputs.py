class snakeTraj:
    def __init__(self, IP, initPos, Phase = 0):
        self.traj = []
        self.timeStamp = []
        self.IP = IP
        self.Phase = Phase
        self.initPos = initPos

endp = [0,0,0,0,0,0,0]

defaultP = [70, 70]
## Arm 1 ##
arm1Traj = snakeTraj('192.168.1.236', [0.0, -30, 0.0, 125, 0.0, 11.0, -45],0)

strumD = 15
center = 52.4
head1 = center - strumD / 2
head2 = center + strumD / 2
trajInput1 = [[[6, 4.7, 4.7, 0, endp[0]], [0.75, 0.25, 2, 1, 5]], [[-27.6, -56.2, -56.2, endp[1]], [1, 2, 2.5, 3.5]],
                   [[6, 4.7, 4.7, endp[2]], [0.75, 0.25, 5, 3]], [[118.1, 35.75, 35.75, 100, endp[3]], [1.5, 2, 1, 2, 2.5]],
                   [[0, 0, 70, endp[4]], [2, 3, 2, 2]], [[head1, head1, head2, -10, endp[5]], [1, 3, 0.3, 3.5+0.7, 1]],
                   [[-35.9, -35.9, endp[6]], [1, 7.5, 0.5]]]
arm1Traj.traj =[trajInput1]
arm1Traj.timeStamp = [34]
arm1Traj.Probs = [[100]]


## Arm 3 ##
arm7Traj = snakeTraj('192.168.1.203', [0, 41, 0, 134, 0, 50, 0],0.25)

strumD = 15
center = 91.5
head1 = center - strumD / 2
head2 = center + strumD / 2
#we want to go to [31.8, 66.2, -34.6, 131.4, -21.7, -strumD/2 + 91.5, -22.7]
trajInput7 = [[[31.8, 31.8, endp[0]], [3, 2, 4]], [[66.2, 66.2, endp[1]], [3, 2, 4]],
                   [[-38, -34.6, -34.6, endp[2]], [2, 1, 2, 4]], [[134, 131.4, 131.4, 137, endp[3]], [2, 1, 2.5, 1.5, 2]],
                   [[-21.7, -21.7, endp[4]], [4, 0.5, 4.5]], [[20,20, head1, head2, head2, endp[5]], [1,1, 2, 0.3, 0.75+0.7, 3.25]],
                   [[-22.7, -22.7, endp[6]], [2, 3, 4]]]
arm7Traj.timeStamp =[8] # time should be 8
arm7Traj.traj = [trajInput7] # start position is 0,42,-14,127.9,120.5,58,-10.4

arm7Traj.Probs = [[100]]


## Arm 2 ##
arm2Traj = snakeTraj('192.168.1.242', [0.0, -8.5, 0, 95, 0, 30, -45],0.5)

strumD = 15
center = 52.4
head1 = center - strumD / 2
head2 = center + strumD / 2
trajInput2 = [[[6, 4.7, 4.7, 0, endp[0]], [0.75, 0.25, 2, 1, 5]], [[-27.6, -56.38, -56.38, endp[1]], [1, 1, 2, 5]],
                   [[6, 4.7, 4.7, endp[2]], [0.75, 0.25, 6, 2]], [[118.1, 35.75, 35.75, 100, endp[3]], [1.5, 1, 2, 2, 2.5]],
                   [[0, 0, 70, endp[4]], [2, 3, 2, 2]], [[head1, head1, head2, -10, endp[5]], [1, 1.5, 0.3, 3.5+0.7, 2]],
                   [[-35.9, -35.9, endp[6]], [1, 7.5, 0.5]]]
arm2Traj.timeStamp =[] # NONE
arm2Traj.traj = []
arm2Traj.Probs = [[100], [100]]


## Arm 3 ##
arm3Traj = snakeTraj('192.168.1.204', [34.0, 21, 0, 90, 0, 30, -45],0.75)

strumD = 15
center = 54.2+strumD/2
head1 = center - strumD / 2
head2 = center + strumD / 2
#we have to get to 9.2, 58.7, -182, 49.1 18, 54.2, -38.5
trajInput3 = [[[9.2, 9.2, endp[0]], [3, 3, 3]], [[58.7, 58.7, endp[1]], [3, 4, 2]],
                   [[-182, -182, endp[2]], [3, 3, 3]], [[85, 49.1, 49.1, 85, endp[3]], [1.5, 2.5, 1, 2, 2]],
                   [[18, 18, endp[4]], [3, 3, 3]], [[head1, head1, head2, 70, endp[5]], [1, 3, 0.3, 2+0.7, 2]],
                   [[-38.5, -38.5, endp[6]], [3, 3, 3]]]
arm3Traj.timeStamp =[14] # 14 or 48
arm3Traj.traj = [trajInput3] # we are at 34 24.4 -181.1 85.3 18 17.5 -46.5
arm3Traj.Probs = [[100], [100]]

## Arm 4 ##
arm4Traj = snakeTraj('192.168.1.208', [144, 26, 0, 120, 0, 40, -45],1)

strumD = 15
center = 52.4
head1 = center - strumD / 2
head2 = center + strumD / 2
trajInput2 = [[[6, 4.7, 4.7, 0, endp[0]], [0.75, 0.25, 2, 1, 5]], [[-27.6, -56.38, -56.38, endp[1]], [1, 1, 2, 5]],
                   [[6, 4.7, 4.7, endp[2]], [0.75, 0.25, 6, 2]], [[118.1, 35.75, 35.75, 100, endp[3]], [1.5, 1, 2, 2, 2.5]],
                   [[0, 0, 70, endp[4]], [2, 3, 2, 2]], [[head1, head1, head2, -10, endp[5]], [1, 1.5, 0.3, 3.5+0.7, 2]],
                   [[-35.9, -35.9, endp[6]], [1, 7.5, 0.5]]]
arm4Traj.timeStamp =[] #31
arm4Traj.traj = []
arm4Traj.Probs = []

## Arm 5 ##
arm5Traj = snakeTraj('192.168.1.237', [10, 46, 0, 113, 0, 10, -45],0.75)

strumD = 15
center = 8
head1 = center - strumD / 2
head2 = center + strumD / 2
desiredpos = [27, 69, 52.5, 126.5, -17.2, 8, -30.4]
# we want to go to  [27, 68.75, 52.5, 126, -17.2, -strumD/2 +8, -30.4]
trajInput5 = [[[desiredpos[0], desiredpos[0], endp[0]], [4, 0.5, 4.5]], [[desiredpos[1], desiredpos[1], endp[1]], [4, 0.5, 4.5]],
                   [[desiredpos[2], desiredpos[2], endp[2]], [4, 0.5, 4.5]], [[desiredpos[3], desiredpos[3], endp[3]], [4, 0.5, 4.5]],
                   [[desiredpos[4], desiredpos[4], endp[4]], [4, 0.5, 4.5]], [[head1, head1, head2, endp[5]], [3, 1, 0.3, 4+0.7]],
                   [[desiredpos[6], desiredpos[6], endp[6]], [3, 1.5, 4.5]]]
arm5Traj.timeStamp =[30] # at 30
arm5Traj.traj = [trajInput5] # we are at 10 49.4 52.5 108.5 50.3 -3 -49.3
arm5Traj.Probs = [[100]]

## Arm 6 ##
arm6Traj = snakeTraj('192.168.1.244', [-70.5, -59.5, 0, 132, -130, 10, -45],0)

strumD = 15
center = -3.2
head1 = center - strumD / 2
head2 = center + strumD / 2
desiredpos= [-57.4, -59.1, -102.9, 105.4, 29, -3.2, -0.2]
trajInput6 = [[[desiredpos[0], desiredpos[0], endp[0]], [4, 0.5, 4.5]], [[desiredpos[1], desiredpos[1], endp[1]], [4, 0.5, 4.5]],
                   [[desiredpos[2], desiredpos[2], endp[2]], [4, 0.5, 4.5]], [[desiredpos[3], desiredpos[3],150,  endp[3]], [4, 0.5,1.5, 3]],
                   [[desiredpos[4], desiredpos[4], endp[4]], [4, 0.5,4.5]], [[head1, head1, head2, endp[5]], [3, 1, 0.3, 4+0.7]],
                   [[desiredpos[6], desiredpos[6], endp[6]], [3, 1.5, 4.5]]]
arm6Traj.timeStamp =[41.25] #41.25
arm6Traj.traj = [trajInput6] #currently at -70.5,-58.3, -88.7, 134.8, 29, -5.7, -58.7
arm6Traj.Probs = [[100]]








robotInfo = [arm1Traj, arm7Traj, arm2Traj, arm3Traj, arm4Traj, arm5Traj, arm6Traj]
# robotInfo = [arm2Traj]

for curinfo in robotInfo:
    if len(curinfo.timeStamp) != len(curinfo.traj):
        print("WARNING: your times to strum do not math your trajectories for",curinfo.IP)
        exit()
    for checks in curinfo.timeStamp:
        # for check in checks:
        if checks + 9 > 72:
            print("cant do this yet! strumming too late :(")
            exit()
    # for traj
