import numpy as np

robot = np.array([2,3])
target = np.array([
    [1,2],
    [4,5],
    [9,5]
    ])

distances = np.linalg.norm(
    target - robot, 
    axis=1
)

closest = np.argmin(distances)

direction = target[closest] - robot

unit_direction = direction / np.linalg.norm(direction)

print("Robot Position:", robot)
print("Target:", target)
print("Distances:", distances)
print("Closest point:", target[closest])
print("Unit Direction:", unit_direction)