queue = []


def addBlob(blob):
    queue.append(blob)


def getNext():
    queue.sort()
    return queue.pop(0)


def hasNext():
    return len(queue) != 0
