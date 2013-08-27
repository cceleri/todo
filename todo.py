import sys

import logging
todoLogger = logging.getLogger('todo')

import todotools
import argparse

import curses

import pickle

from util import SelectionList, Selection, Action
from todotools import TodoListEmpty

def displayTodoList(stdscr, todoList, i=1):
    selectionList = SelectionList()
    for category in todoList.categories:
        stdscr.addstr(i, 1, '='*len(category))
        stdscr.addstr(i+1, 1, category)
        stdscr.addstr(i+2, 1, '='*len(category))
        i+=4
        j = 1
        for item in todoList[category]:
            stdscr.addstr(i, 1, str(j)+'. '+item.name)
            selectionList.append(Selection((i, 1, str(j)+'. '+item.name), item))
            i += 1
            j += 1
        i += 1

    return selectionList

def highlightSelection(stdscr, selection):
    s = tuple(list(selection.addStrArgs)+[curses.A_REVERSE])
    stdscr.addstr(*s)

def switchSelection(stdscr, lastSelection, currentSelection):
    stdscr.addstr(*lastSelection.addStrArgs)
    highlightSelection(stdscr, currentSelection)

def selectTodoItem(stdscr, todoList):
    stdscr.clear()
    selectionList = displayTodoList(stdscr, todoList)
    currentSelection = selectionList.current()
    highlightSelection(stdscr, currentSelection)

    while True:
        lastSelection = currentSelection
        k = stdscr.get_wch()
        if k in ['k', curses.KEY_UP]:
            currentSelection = selectionList.prev()
        elif k in ['j', curses.KEY_DOWN]:
            currentSelection = selectionList.next()
        elif k in ['d']:
            return Action(Action.REMOVE, currentSelection.todoItem)
        elif k == 'q':
            return None

        switchSelection(stdscr, lastSelection, currentSelection)
        stdscr.refresh()
        

def main(stdscr):

    todoList = pickle.load(open('sample.todo','rb'))

    while True:
        action = selectTodoItem(stdscr, todoList)
        if action == None: break
        if action.action == Action.REMOVE:
            todoList.remove(action.todoItem)
            if todoList.empty(): break

if __name__ == '__main__':
    curses.wrapper(main)

# vim: set ts=4 sw=4 expandtab smarttab:
