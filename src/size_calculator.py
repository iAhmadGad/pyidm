def calculateSize(b):
    if b > pow(2, 10):
        return str(b / pow(2, 10)) + " kilobytes"
    elif b > pow(2, 20):
        return str(b / pow(2, 20)) + " megabytes"
    elif b > pow(2, 30):
        return str(b / pow(2, 30)) + " gigabytes"
    elif b > pow(2, 40):
        return str(b / pow(2, 40)) + " terabytes"
    return str(b) + " bytes"
