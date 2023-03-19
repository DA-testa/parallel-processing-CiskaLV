# python3

class Thread:
    def __init__(self, index):
        self.index = index
        self.time = 0

    def __lt__(self, other):
        return self.time < other.time


def parallel_processing(n, m, data):
    output = []

    threads = [Thread(i) for i in range(n)]
    
    for i in range(m):
        thread = min(threads)

        output.append((thread.index, thread.time))
        thread.time += data[i]

    return output

def main():
    inList = list(map(int, input().split()))
    n = inList[0]
    m = inList[1]

    data = list(map(int, input().split()))

    result = parallel_processing(n,m,data)

    for i, j in result:
        print(i, j)


if __name__ == "__main__":
    main()
