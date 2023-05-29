#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        ret_value = fct(*args)
        return ret_value
    except Exception as errinfo:  # stores the errorinfo in errinfo var
        print("Exception: {}".format(errinfo), file=sys.stderr)
        return None
