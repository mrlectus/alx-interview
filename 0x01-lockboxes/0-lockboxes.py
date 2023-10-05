#!/usr/bin/python3


# can unlock
def canUnlockAll(boxes):
    keys = set()
    keys.add(0)
    stack = [0]
    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key not in keys:
                keys.add(key)
                stack.append(key)
    return len(keys) == len(boxes)
