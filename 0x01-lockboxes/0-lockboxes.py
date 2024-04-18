#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    Function to determine if all boxes can be open
    """
    # if exists boxes
    if not boxes:
        return False
    # check if is a list
    if type(boxes) is not list:
        return False
    for box in boxes:
        if type(box) is not list:
            return False
    # status of each box
    status = [False for i in range(len(boxes))]
    status[0] = True
    # get the key from box 0 (default opened box)
    keys = [key for key in boxes[0]]
    # while exists boxes to open
    while False in status:
        newkeys = []
        if len(keys) == 0:
            return False
        for key in keys:
            if key < len(boxes) and not status[key]:
                newkeys = newkeys + boxes[key]
                status[key] = True
        keys = newkeys
    return True
