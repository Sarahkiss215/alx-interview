#!/usr/bin/python3


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    to other boxes can be opened..
    '''
    bx = len(boxes)
    opened_boxes = set([0])
    closed_boxes = set(boxes[0]).difference(set([0]))
    while len(closed_boxes) > 0:
        boxId = closed_boxes.pop()
        if not boxId or boxId >= bx or boxId < 0:
            continue
        if boxId not in seen_boxes:
            closed_boxes = closed_boxes.union(boxes[boxId])
            opened_boxes.add(boxId)
    return bx == len(opened_boxes)
