class Action(object):
    REMOVE = 0
    ADD = 1

    def __init__(self, action, todoItem):
        self.action = action
        self.todoItem = todoItem

class Selection(object):
    def __init__(self, addStrArgs, todoItem):
        self.addStrArgs = addStrArgs
        self.todoItem = todoItem

class SelectionList(list):
    def __init__(self, iterator=[]):
        list.__init__(self, iterator)
        self._current = 0

    def current(self):
        return self[self._current]

    def getCurrentIndex(self):
        return self._current

    def setCurrentIndex(self, index):
        if index >= len(self):
            index = len(self) - 1
        if index < 0:
            index = 0
        self._current = index

    def remove(self, value):
        list.remove(self, value)
        if self._current == len(self):
            self._current -= 1

    def next(self):
        if self._current < len(self)-1:
            self._current += 1
        return self[self._current]

    def prev(self):
        if self._current > 0:
            self._current -= 1
        return self[self._current]
