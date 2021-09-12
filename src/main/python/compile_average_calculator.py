import sys

from fbs_runtime.application_context.PyQt5 import ApplicationContext

from average_calculator import window

if __name__ == '__main__':
    appctxt = ApplicationContext()
    window.show()
    sys.exit(appctxt.app.exec())
