# modules/obfuscator.py

def apply_xor(code, key):
    return f"""
exec(''.join([chr(ord(c)^ord(k)) for c,k in zip("{code}", "{(key*(len(code)//len(key)+1))[:len(code)]}")]))
"""
