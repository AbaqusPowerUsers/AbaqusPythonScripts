def UnRegisterPy():
    try:
        reg = OpenKey(HKEY_LOCAL_MACHINE, regpath)
    except EnvironmentError:
        print "*** Python not registered?!"
        return
    try:
        DeleteKey(reg, installkey)
        DeleteKey(reg, pythonkey)
        DeleteKey(HKEY_LOCAL_MACHINE, regpath)
    except:
        print "*** Unable to un-register!"
    else:
        print "--- Python", version, "is no longer registered!"