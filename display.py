import curses
from util import SelectionList, Selection, Action

def highlightSelection(stdscr, selection):
    s = tuple(list(selection.addStrArgs)+[curses.A_REVERSE])
    stdscr.addstr(*s)

def switchSelection(stdscr, lastSelection, currentSelection):
    stdscr.addstr(*lastSelection.addStrArgs)
    highlightSelection(stdscr, currentSelection)

def selectTodoItem(stdscr, todoList):
    """
    Opens a display of the *todoList* for the user to select
    an item and choose an action to take.
    """
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
        

def displayTodoList(stdscr, todoList):
    """
    Creates an initial display of *todoList*.
    """
    stdscr.clear()
    i = 1
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

