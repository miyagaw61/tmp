from sys import argv

def hoge(a, b):
    return a+b

def main():
    print(hoge(int(argv[1]), int(argv[2])))

if __name__ == '__main__':
    main()
