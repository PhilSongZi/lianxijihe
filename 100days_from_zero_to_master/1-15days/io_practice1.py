import time


def main():
    # 一次读取文件
    with open('./save_txts/西洲曲.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # for-in逐行读取
    with open('./save_txts/西洲曲.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)

    print()

    # 读取文件按行读取到列表
    with open('./save_txts/西洲曲.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(lines)


if __name__ == '__main__':
    main()
