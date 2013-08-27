def binarySearch(sortedList, value):
    if len(sortedList) == 1:
        return sortedList[0]
    if value < sortedList[len(sortedList)/2]:
        return binarySearch(sortedList[:len(sortedList)/2], value)
    return binarySearch(sortedList[len(sortedList)/2:], value)

# vim: set ts=4 sw=4 expandtab smarttab:
