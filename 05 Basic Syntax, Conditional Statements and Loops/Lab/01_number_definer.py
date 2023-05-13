n = float(input())
positive, negative, large, small = False, False, False, False

if n == 0:
    print('zero')
elif n > 0:
    positive = True
    if n > 1000000:
        large = True
    elif n < 1:
        small = True
elif n < 0:
    negative = True
    if abs(n) > 1000000:
        large = True
    elif abs(n) < 1:
        small = True

if positive and not small and not large:
    print('positive')
elif small and positive:
    print('small positive')
elif large and positive:
    print('large positive')
elif small and negative:
    print('small negative')
elif negative and not small and not large:
    print('negative')
elif large and negative:
    print('large negative')