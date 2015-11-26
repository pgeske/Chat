import curses

stdscr = curses.initscr()
#Create Input Window
input_window = curses.newwin(5, 400, 0, 0)
input_window.border(0)
input_window.refresh()
input_window.move(2,5)
#Create Message Window
messsage_window = curses.newwin(50, 400, 5, 0)
messsage_window.border(0)
messsage_window.refresh()
while True:
    my_string = input_window.getstr()
    input_window.erase()
    input_window.border(0)
    input_window.move(2,5)
    messsage_window.move(2, 1)
    messsage_window.addstr(my_string)
    messsage_window.refresh()
    input_window.refresh()
curses.endwin()

#myscreen = curses.initscr()
#
#myscreen.border(0)
#myscreen.addstr(12, 25, "Python curses in action!")
#myscreen.refresh()
#myscreen.getch()
#
#curses.endwin()
