import sys
def is_dot_in_ellipse(x, y, cx, cy, rx, ry):
    return ((x - cx)/rx)**2 + ((y - cy)/ry)**2

def main():
    ellipse_file = sys.argv[1]
    dots_file = sys.argv[2]
    with open(ellipse_file) as file:
        lines = file.readlines()
        cx, cy = map(float, lines[0].split())
        rx, ry = map(float, lines[1].split())
    dots = []
    with open(dots_file) as file:
        for line in file:
            line = line.strip()
            if line:
                x, y = map(float, line.split())
                dots.append((x, y))
    for x, y in dots:
        result = is_dot_in_ellipse(x, y, cx, cy, rx, ry)
        if abs(result - 1.0) < 1e-9: # это сравнение делаем для точности при вычислениях чисел с плавающей точкой
            print('0')
        elif result < 1:
            print('1')
        else:
            print('2')

if __name__ == "__main__":
    main()