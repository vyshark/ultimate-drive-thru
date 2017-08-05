from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [],
        excludes = [],
        include_files=["icons/"]
        )

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('UserInterface.py', base=base, targetName = 'ultimate-drive-thru')
]

setup(name='ultimate drive thru',
      version = '1.0',
      description = 'A Automated Drive thru AI',
      options = dict(build_exe = buildOptions),
      executables = executables)
