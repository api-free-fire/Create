import platform
import os
import sys

print('\033[0;1m[\033[1;30m•\033[0;1m]\033[0;1m LOADING')
bit = platform.architecture()[0]
print(f'\033[0;1m[\033[1;30m•\033[0;1m]\033[0;1m {bit} DETECTED')
try:
    print('\033[0;1m[\033[1;30m•\033[0;1m]\033[0;1m CHECKING FOR UPDATES...')
    os.system('git pull > /dev/null 2>&1')
    print('\033[0;1m[\033[1;32m✓\033[0;1m]\033[0;1m UPDATE CHECK COMPLETE')
except:
    print('\033[0;1m[\033[1;33m!\033[0;1m]\033[0;1m NO GIT REPOSITORY FOUND')
if bit == '64bit':
    sys.path.insert(0, os.path.dirname(__file__))
    import main64
    print('\033[0;1m[\033[1;32m✓\033[0;1m]\033[0;1m MODULE LOADED SUCCESSFULLY')
    print('\033[0;1m[\033[1;30m•\033[0;1m]\033[0;1m RUNNING main()...')
    main64.main()
    print('\n\033[0;1m[\033[1;32m✓\033[0;1m]\033[0;1m PROGRAM FINISHED')
    input('\033[0;1m[\033[1;33m⚠\033[0;1m]\033[0;1m Press Enter to exit...')
elif bit == '32bit':
    print('\033[0;1m[\033[1;31m✗\033[0;1m]\033[0;1m 32BIT NOT SUPPORTED (only 64bit .so file available)')
else:
    print('\033[0;1m[\033[1;31m✗\033[0;1m]\033[0;1m UNSUPPORTED ARCHITECTURE')
