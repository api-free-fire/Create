import platform
import os
import sys
import importlib.util
print('\033[0;1m[\033[1;30m•\033[0;1m]\033[0;1m LOADING')
bit = platform.architecture()[0]
print(f'\033[0;1m[\033[1;30m•\033[0;1m]\033[0;1m {bit} DETECTED')
try:
    print('\033[0;1m[\033[1;30m•\033[0;1m]\033[0;1m CHECKING FOR UPDATES...')
    os.system('git pull')
    print('\033[0;1m[\033[1;32m✓\033[0;1m]\033[0;1m UPDATE CHECK COMPLETE')
except:
    print('\033[0;1m[\033[1;33m!\033[0;1m]\033[0;1m NO GIT REPOSITORY FOUND')
if bit == '64bit':
    try:
        spec = importlib.util.spec_from_file_location("main64", "./main64.cpython-313-aarch64-linux-android.so")
        main64 = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(main64)
        print('\033[0;1m[\033[1;32m✓\033[0;1m]\033[0;1m MODULE LOADED SUCCESSFULLY')
    except Exception as e:
        print(f'\033[0;1m[\033[1;31m✗\033[0;1m]\033[0;1m FAILED TO LOAD MODULE: {e}')
elif bit == '32bit':
    print('\033[0;1m[\033[1;31m✗\033[0;1m]\033[0;1m 32BIT NOT SUPPORTED (only 64bit .so file available)')
else:
    print('\033[0;1m[\033[1;31m✗\033[0;1m]\033[0;1m UNSUPPORTED ARCHITECTURE')
