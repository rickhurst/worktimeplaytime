import os
import optparse

def run():

  global PID_FILE, LOG_FILE
  USAGE = "python [-p PIDFILE] [-l LOGFILE]\n\n" \
          "Commands:\n  - worktime\n  - playtime"

  parser = optparse.OptionParser(usage=USAGE)
  options, args = parser.parse_args()

  run_commands = True

  status_file = "/Users/rickhurst/worktimeplaytime.txt"
  if os.path.isfile(status_file):
    # read it
    f = open(status_file, "r")
    file_command = f.read()
    print("file command: " + file_command)

    if file_command == "ignore":
      print("ignoring commands")
      run_commands = False
      
  else:
    print('no file commands found')

  if run_commands:
    if args:
      if args[0] == "worktime":
        os.system('ansible-playbook /Users/rickhurst/apps/worktimeplaytime/worktime.yml') 
      if args[0] == "playtime":
        os.system('ansible-playbook /Users/rickhurst/apps/worktimeplaytime/playtime.yml')
    else:
      print("no args") 


if __name__ == '__main__':
  run()

