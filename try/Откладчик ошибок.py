def get(value):
    if value > 0:
        return "Positive"
    if value < 0:
        return "Negative"
    return 'Zero'

if __name__ == '__main__':
    value = int(input())
    print(get(value).upper())