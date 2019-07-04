import sys
import os

from time import sleep
from subprocess import run, Popen
from shutil import copy

import yaml

GH_BASE = os.path.expanduser('~/github')
DANS_BASE = f'{GH_BASE}/Dans-labs'
THEME_BASE = f'{DANS_BASE}/mkdocs-dans'
CLIENTS = f'{THEME_BASE}/clients.yaml'


HELP = f'help.md'

USAGE = '''
Run `build.py` from the Terminal as follows:

```sh
python3 build.py make
python3 build.py docs
python3 build.py g commitmsg
```

`build` builds the DANS theme from the source files.
`pack` installs the DANS theme as a module.
`make` builds the DANS theme from the source files and installs it as a module.

`docs` serves the theme documentation (without make)

`g` does `make`, and pushes the theme repo site to GitHub,
where it will be published under <https://dans-labs.github.io/mkdocs-dans/>.
The repo itself will also be committed and pushed to GitHub.

Replace `commitmsg` by anything that is appropriate as a commit message.

'''


def readArgs():
  args = sys.argv[1:]
  if not len(args) or args[0] in {'-h', '--help', 'help'}:
    console(USAGE)
    return (False, None, [])
  arg = args[0]
  if arg not in {
      'build', 'pack', 'make', 'docs', 'push', 'g',
  }:
    console(USAGE)
    return (False, None, [])
  if arg in {'g'}:
    if len(args) < 2:
      console('Provide a commit message')
      return (False, None, [])
    return (arg, args[1], args[2:])
  return (arg, None, [])


def console(msg, error=False, newline=True):
  msg = msg[1:] if msg.startswith('\n') else msg
  msg = msg[0:-1] if msg.endswith('\n') else msg
  target = sys.stderr if error else sys.stdout
  nl = '\n' if newline else ''
  target.write(f'{msg}{nl}')
  target.flush()


def readYaml(fileName):
  with open(fileName) as y:
    y = yaml.load(y)
  return y


def commit(task, msg):
  run(['git', 'add', '--all', '.'])
  run(['git', 'commit', '-m', msg])
  run(['git', 'push', 'origin', 'master'])


def buildCustom():
  status = run(['npm', 'run', 'build']).returncode
  if status:
    return


def packCustom():
  for fl in ('README.md', 'package.json'):
    copy(fl, f'python/{fl}')

  curDir = os.getcwd()
  os.chdir('python')
  status = run(['pip3', 'install', '.']).returncode
  os.chdir(curDir)
  return not status


def makeCustom():
  status = run(['npm', 'run', 'build']).returncode
  if status:
    return

  for fl in ('README.md', 'package.json'):
    copy(fl, f'python/{fl}')

  curDir = os.getcwd()
  os.chdir('python')
  status = run(['pip3', 'install', '.']).returncode
  os.chdir(curDir)
  return not status


def shipDocs():
  run(['mkdocs', 'gh-deploy'])


def buildDocs():
  run(['mkdocs', 'build'])


def serveDocs():
  proc = Popen(['mkdocs', 'serve'])
  sleep(3)
  run('open http://127.0.0.1:8000', shell=True)
  try:
    proc.wait()
  except KeyboardInterrupt:
    pass
  proc.terminate()


def main():
  (task, msg, remaining) = readArgs()
  if not task:
    return
  elif task == 'build':
    buildCustom()
  elif task == 'pack':
    packCustom()
  elif task == 'make':
    makeCustom()
  elif task == 'docs':
    serveDocs()
  elif task == 'g':
    if makeCustom():
      shipDocs()
      commit(task, msg)


main()
