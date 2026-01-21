import sys

def arr_all(n, m):
    if n <= 0 or m <= 0:
        return []
    head = []
    current = 0
    while True:
        head.append(current + 1)
        current = (current + m - 1) % n
        if current == 0:
            break
    return head

def main():
    n_1 = int(sys.argv[1])
    m_1 = int(sys.argv[2])
    n_2 = int(sys.argv[3])
    m_2 = int(sys.argv[4])
    path1 = arr_all(n_1, m_1)
    path2 = arr_all(n_2, m_2)
    result = ''.join(map(str, path1)) + ''.join(map(str, path2))
    print(result)

if __name__ == "__main__":
    main()








