from collections import defaultdict
import sys
import logging

todotoolsLogger = logging.getLogger('todo.todotools')

class TodoList(defaultdict):
    def __init__(self, todoItems=[]):  
        defaultdict.__init__(self, list) 
        for ti in todoItems:
            self[ti.category].append(ti)

    @property
    def categories(self, ):
        return [key for key in self.keys()]

    # required method for pickling because defaultdict
    # does not do this nicely
    def __reduce__(self):
        return (TodoList, (self.__getAllItems(),),)

    def __getAllItems(self):
        allItems = []
        for __, value in self.items():
            allItems += value
        return allItems

    def __repr__(self):
        allItems = self.__getAllItems()
        return 'TodoList(%s)' % repr(allItems)

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

    @name.setter
    def name(self, value):
        todotoolsLogger.debug('Changing name of '+str(self)+' to '+str(value))
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        todotoolsLogger.debug('Changing category of '+str(self)+' to '+str(value))
        self._category = value

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        todotoolsLogger.debug('Changing priority of '+str(self)+' to '+str(value))
        self._priority = value

    def __del__(self):
        todotoolsLogger.debug('Deleting ', repr(self))

    def __str__(self):
        return self._category+': '+self.name+' ('+str(self._priority)+')'

    def __repr__(self):
        return 'TodoItem(%r, category=%r, priority=%r)'\
                % (self._name, self._category, self._priority)

# vim: set ts=4 sw=4 expandtab smarttab:
