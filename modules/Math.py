def lerp(start, end, t):
    return start + t * (end - start)

def clamp(value, min, max):
    if value < min:
        return min
    elif value > max:
        return max
    else:
        return value

def abs(value):
    if value < 0: return -value
    return value

def normalize(x_min, x_max, x):
    return (x - x_min)/(x_max - x_min)