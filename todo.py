import sys

import logging
todoLogger = logging.getLogger('todo')

import todotools
import argparse

import curses

import pickle

from util import SelectionList, Selection
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
    selectionList = displayTodoList(stdscr, todoList)
    highlightSelection(stdscr, selectionList.current())
    currentSelection = selectionList.current()

    while True:
        lastSelection = currentSelection
        k = stdscr.get_wch()
        if k in ['k', curses.KEY_UP]:
            currentSelection = selectionList.prev()
        elif k in ['j', curses.KEY_DOWN]:
            currentSelection = selectionList.next()
        elif k in ['d']:
            todoList.remove(currentSelection.todoItem)
            if todoList.empty(): raise TodoListEmpty
            stdscr.clear()
            currentIndex = selectionList.getCurrentIndex()
            selectionList = displayTodoList(stdscr, todoList)
            selectionList.setCurrentIndex(currentIndex)
            lastSelection = selectionList.current()
            currentSelection = selectionList.current()
        elif k == 'q':
            break

        switchSelection(stdscr, lastSelection, currentSelection)
        stdscr.refresh()
        

def main(stdscr):

    todoList = pickle.load(open('sample.todo','rb'))

    while True:
        try:
            action = selectTodoItem(stdscr, todoList)
        except TodoListEmpty:
            break

if __name__ == '__main__':
    curses.wrapper(main)

# vim: set ts=4 sw=4 expandtab smarttab:
