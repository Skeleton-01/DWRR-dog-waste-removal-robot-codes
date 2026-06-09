import numpy as np

robot = np.array([2,3])
poop = np.array([
    [1,2], [4,5], [9,5]
])

distances = np.linalg.norm(
    poop - robot,
    axis=1
)

closest = np.argmin(distances)

direction = poop[closest] - robot

unit_direction = direction / np.linalg.norm(direction)

print("Robot Position:", robot)
print("Poop:", poop)
print("Distances:", distances)
print("Closest point:", poop[closest])
print("Unit Direction:", unit_direction)