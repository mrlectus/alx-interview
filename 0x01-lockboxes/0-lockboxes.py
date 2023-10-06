#!/usr/bin/python3
"""
lockboxes for interviews
"""


# can unlock
def canUnlockAll(boxes):
    """
    Function to determine if all boxes can be open
    """
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
