# IMPORT the required libraries
import pybullet as p
import time
import pybullet_data

# SIMULATION setup
physicsClient = p.connect(p.GUI) # or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) # optionally
p.setGravity(0,0,-10)

# ADD robots and objects
planeId = p.loadURDF("plane.urdf")
startPos = [0,0,1]
startOrientation = p.getQuaternionFromEuler([0,0,0])
boxId = p.loadURDF("assets/two_link_robot.urdf",startPos, startOrientation)
p.resetBasePositionAndOrientation(boxId, startPos, startOrientation)

# MOVE robot to the starting position (home configuration)
# p.resetJointState(boxId, 0, 0.3)
# p.resetJointState(boxId, 1, 0.5)

# IK
target_position = [0.8, 0.8, 0]
target_q = p.calculateInverseKinematics(boxId, 2, target_position)
print(target_q)

# MOVE joints to that position
p.resetJointState(boxId, 0, target_q[0])
p.resetJointState(boxId, 1, target_q[1])

# FK
final_position = p.getLinkState(boxId, 2)
print(final_position)

for i in range (1000):
    p.stepSimulation()
    time.sleep(1./240.)

p.getLinkState

time.sleep(2)