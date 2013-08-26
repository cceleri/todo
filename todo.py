import sys

import logging
todoLogger = logging.getLogger('todo')

import todotools
import argparse

import curses

import pickle

def main(stdscr):

    tl = pickle.load(open('sample.todo','rb'))

    i = 0
    for key in tl.keys():
        for item in tl[key]:
            stdscr.addstr(i, 0, str(item))
            i+=1
    q = stdscr.getch()

if __name__ == '__main__':
    curses.wrapper(main)

# vim: set ts=4 sw=4 expandtab smarttab:
