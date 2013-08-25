class TodoList(list):
    def __init__(self, todoItems=[]):  
        list.__init__(self) 
        for ti in todoItems:
            self.append(ti)

    def append(self, todoItem):
        assert isinstance(todoItem, TodoItem)
        list.append(self, todoItem)

    def insert(self, index, todoItem):
        assert isinstance(todoItem, TodoItem)
        list.insert(self, index, todoItem)

    def __setitem__(self, index, todoItem):
        assert isinstance(todoItem, TodoItem)
        list.__setitem__(self, index, todoItem)

    def __add__(self, todoList):
        assert isinstance(todoList, TodoList)
        return list.__add__(self, todoList)

    def __iadd__(self, todoList):
        assert isinstance(todoList, TodoList)
        return list.__iadd__(self, todoList)

    def extend(self, todoList):
        assert isinstance(todoList, TodoList)
        list.extend(self, todoList)

    def __repr__(self):
        return 'TodoList(%s)' % list.__repr__(self)


class TodoItem(tuple):
    def __new__(type, name, category='general', priority=0):
        return tuple.__new__(type, [priority, {'category': category, 'name': name}])

    def __init__(self, name, category='general', priority=0):
        self._name     = self[1]['name']
        self._category = self[1]['category']
        self._priority = self[0]

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    @property
    def priority(self):
        return self._priority

    def __repr__(self):
        return 'TodoItem(%r, category=%r, priority=%r)'\
                % (self._name, self._category, self._priority)

# vim: set ts=4 sw=4 expandtab smarttab:
