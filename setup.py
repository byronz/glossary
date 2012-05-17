from distutils.core import setup
import py2exe

includes = []
excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
            'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
            'Tkconstants', 'Tkinter']
packages = ['yaml']
#dll_excludes = ['libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll', 'tcl84.dll', 'tk84.dll']

setup(
    data_files=[('cfg',['config.yml']),
                ('output', [])],
    options = {"py2exe": {"unbuffered": True,
                          "optimize": 2,
                          "includes": includes,
                          "excludes": excludes,
                          "packages": packages,
                          "bundle_files": 2,
                          "dist_dir": "dist",
                          "skip_archive": True,
                         },
              },
    console = ['glossary.py'],
)
