import subprocess

def rofi(prompt, options, rofi_args=None, fuzzy=True):
    optionstr = '\n'.join(option.replace('\n', ' ') for option in options)
    args = ['choose', '-i']
    if rofi_args:
        args += rofi_args
    args = [str(arg) for arg in args]


    result = subprocess.run(args, input=optionstr, stdout=subprocess.PIPE, universal_newlines=True)
    returncode = result.returncode
    stdout = result.stdout.strip()
    
    index = int(stdout)
    selected = options[index] if index != -1 else ''

    if returncode == 0:
        key = 0
    elif returncode == 1:
        key = -1
    elif returncode > 9:
        key = returncode - 9

    return key, index, selected
