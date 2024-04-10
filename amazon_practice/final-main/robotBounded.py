def isRobotBounded(instructions):
    # Directions: north, east, south, west
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # Starting position and direction
    x, y = 0, 0
    directionIndex = 0  # Start facing north

    for i in instructions:
        if i == 'G':
            dx, dy = directions[directionIndex]
            x, y = x + dx, y + dy
        elif i == 'L':
            directionIndex = (directionIndex - 1) % 4  # Turn left
        elif i == 'R':
            directionIndex = (directionIndex + 1) % 4  # Turn right

    # The robot is in a circle if it's back at the origin or not facing north
    return (x == 0 and y == 0) or directionIndex != 0

instructions = "GGGL"
print(isRobotBounded(instructions))
