REMOVE = 0
ADD    = 1
QUIT   = 2

class Action(object):
    def __init__(self, action, todoItem=None):
        self.action = action
        self.todoItem = todoItem

    def __str__(self):
        if self.action == Action.REMOVE:
            return 'remove '+str(self.todoItem)
        if self.action == Action.ADD:
            return 'add '+str(self.todoItem)
        if self.action == Action.QUIT:
            return 'quit'

