tomato-punch
============

Xubuntu panel applet for time tracking indicator using the pomodoro method.


requirements:
    - xubuntu operating system
    - genmon panel applet from the xfce4-goodies package
    - python 
    - todo.txt

# what?

Pomodoro is a time-tracking method based upon 20 minute periods called pomodoros. the inventor of the method named it this because he used a kitchen timer that looked like a tomato.

in the pomodoro method, you break your work into 20 minute tasks. you set a timer at the start of each task, and work until the timer goes off. at that point you immediately stop working, get up to stretch your legs, walk around a bit, and look at something other than a grid of glowing dots. ahhhh.

todo.txt is a text file format for keeping a todo list. lots of people have written programs you can use with todo.txt files. i use a todo.txt file to keep track of what tasks i need to do. 

punch-time-tracking is a python script that lets you 'punch in' and 'punch out' of tasks on your todo.txt file. it records how long you've spend on each task, and lets you print a nice record of what you spend your day working on. 

tomato-punch will let you add a panel applet to xubuntu, showing you how much time you have left in your current pomodoro sprint. when you are not working, the tomato-punch indidicator shows a green tomato. when you `punch in` to a task, the tomamto turns red, and a 20 minute timer shows up, along with a progress bar. as time passes, the tomato gradually drains from the top, and the progress bar fills from the bottom. this means that the amount of redness left in the tomato, the timer, and the progress bar all show you how much time you have left in your sprint.


# how

### setup
first, install a [todo.txt implementation](https://github.com/ginatrapani/todo.txt-cli.)
then, install xfce4-goodies. this has a panel applet called 'genmon' which stands for 'generic monitor'

add a 'genmon' applet to your panel. configure this applet to use a command executing the included script with the argument `genmon`, like so:

     `python /path/to/this/dir/punch.py genmon`


you should see a red tomato icon in your panel, with the world 'idle' next to it.

### usage

create a task for yourself with todo:

    [mneyer@neyer-lt:~/synced/src/neyer/tomato-punch]
    [11:17:46 05/14/14 2014]
    [(master)(none)]
    $> todo add "Make tomato-punch open source"
    4 Make tomato-punch open source
    TODO: 4 added.

start working on your task with punch. i've included a modified `punch.py` script here; i have it aliased in my bash to just 'punch.'

    [mneyer@neyer-lt:~/synced/src/neyer/tomato-punch]
    [11:17:54 05/14/14 2014]
    [(master)(none)]
    $> punch in 4
    Start timer on: Make tomato-punch open source


now you should see the tomato indicator turn red and show you how much time is left in your pomodoro.
