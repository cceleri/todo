import sys
import logging
todoLogger = logging.getLogger('todo')
#todoLogger.setLevel(logging.DEBUG)

import curses
import pickle

import action
from todotools import TodoListEmpty
import display

def main(stdscr):

    todoList = pickle.load(open('sample.todo','rb'))

    while True:
        a = display.selectTodoItem(stdscr, todoList)
        todoLogger.debug('User chose to '+str(action)+'.')
        if a.action == action.QUIT: break
        if a.action == action.REMOVE:
            todoList.remove(a.todoItem)
            if todoList.empty(): break

if __name__ == '__main__':
    curses.wrapper(main)

# vim: set ts=4 sw=4 expandtab smarttab:
