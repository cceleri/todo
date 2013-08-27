class Selection(object):
    def __init__(self, addStrArgs, todoItem):
        self.addStrArgs = addStrArgs
        self.todoItem = todoItem

class SelectionList(list):
    """ Represents a list of items sorted by category. """
    def __init__(self, iterator=[]):
        list.__init__(self, iterator)
        self._currentItemIndex = 0
        self._currentCategoryIndex = 0
        self._categoryStartIndices = [0]
        currCategory = self[0].category
        for i in xrange(1,len(self)):
            if self[i].category != currCategory:
                currCategory = self[i].category
                self._categoryStartIndices.append(i)

    def current(self):
        return self[self._currentItemIndex]

    def getCurrentIndex(self):
        return self._currentItemIndex

    def setCurrentIndex(self, index):
        if index >= len(self):
            index = len(self) - 1
        if index < 0:
            index = 0
        self._currentItemIndex = index
        self._currentCategoryIndex =
                util.binarySearch(
                        self._categoryStartIndices,
                        self._currentCategoryIndex)

    def remove(self, value):
        if self._currentItemIndex == 


        list.remove(self, value)
        if self._currentItemIndex == len(self):
            self._currentItemIndex -= 1

    @updateCategoryIndex
    def nextItem(self):
        if self._currentItemIndex < len(self)-1:
            self._currentItemIndex += 1
            if self._currentItemIndex\
                    == self._categoryStartIndices[self._currentCategoryIndex+1]
                self._currentCategoryIndex += 1
        return self[self._currentItemIndex]

    def prevItem(self):
        if self._currentItemIndex > 0:
            self._currentItemIndex -= 1
        return self[self._currentItemIndex]

    def nextCategory(self):
        if self._currentCategoryIndex < len(self._categoryStartIndices) - 1:
            self._currentCategoryIndex += 1
            self._currentItemIndex = self._categoryStartIndices[self._currentCategoryIndex]
        return self[self._currentItemIndex]

    def prevCategory(self):
        if self._currentCategoryIndex > 0:
            self._currentCategoryIndex -= 1
            self._currentItemIndex = self._categoryStartIndices[self._currentCategoryIndex]
        return self[self._currentItemIndex]
        


# vim: set ts=4 sw=4 expandtab smarttab:
