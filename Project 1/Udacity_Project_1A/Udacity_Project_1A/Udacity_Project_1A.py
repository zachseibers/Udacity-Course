#Project 1 of Udacity Course - Take a Break

#Key Steps
#1) Initiate, and wait 2 hours
#2) Open Browser to play song
#3) Repeat n number of times

import webbrowser,time

total_breaks = 3
break_count = 1

print("This program started on "+time.ctime())
while(break_count <= total_breaks):
    time.sleep(5)
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=NUC2EQvdzmY")
    print("This is break number",break_count)
    break_count = break_count + 1
print('good job')