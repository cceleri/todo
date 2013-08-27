import sys
import logging
todoLogger = logging.getLogger('todo')
#todoLogger.setLevel(logging.DEBUG)

import curses
import pickle

from util import Action
from todotools import TodoListEmpty
import display

def main(stdscr):

    todoList = pickle.load(open('sample.todo','rb'))

    while True:
        action = display.selectTodoItem(stdscr, todoList)
        todoLogger.debug('User chose to '+str(action)+'.')
        if action == None: break
        if action.action == Action.REMOVE:
            todoList.remove(action.todoItem)
            if todoList.empty(): break

if __name__ == '__main__':
    curses.wrapper(main)

# vim: set ts=4 sw=4 expandtab smarttab:
