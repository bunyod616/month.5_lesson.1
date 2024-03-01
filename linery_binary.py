from datetime import datetime
import time



def binary_search(data, target):
    data.sort()
    l = len(data) - 1
    low = 0
    step = 0
    while True:
        time.sleep(1)
        middle = (low + l) // 2
        step += 1
        if data[middle] == target:
            print(data[middle])
            break

        if data[middle] > target:
            l = middle - 1

        if data[middle] < target:
            low = middle + 1

        if low > l:
            print("invalid")
            break

    print(step)


def linear_search(data, target):
    step = 0
    for i in data:
        time.sleep(1)
        step += 1
        if target == i:
            print(i)
            break
    print(step)

def linear_search_second(data, target):
    step = 0
    for i in data:
        time.sleep(1)
        step += 1
        if target == i:
            print(i)
            break
    print(step)


# if __name__ == "__main__":
#     data = [15,3,22,89,100,34,71]
#     target = int(input("target: "))
#     print(datetime.now().time())
#     binary_search(data, target)
#     print(data)
#     print(datetime.now().time())

# if __name__ == "__main__":
#     data = [15,3,22,89,100,34,71]
#     target = int(input("target: "))
#     print(datetime.now().time())
#     linear_search(data, target)
#     print(data)
#     print(datetime.now().time())

# if __name__ == "__main__":
#     data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
#     target = int(input("target: "))
#     print(datetime.now().time())
#     linear_search(data, target)
#     print(data)
#     print(datetime.now().time())

# if __name__ == "__main__":
#     data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
#     target = int(input("target: "))
#     print(datetime.now().time())
#     binary_search(data, target)
#     print(data)
#     print(datetime.now().time())