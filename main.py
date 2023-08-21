def dice(K, m, Z):
    value = [i for i in range(1, K+1)]
    n = max(K+1, Z+1)
    counter = [0] * n
    for i in range(1, K+1):
        counter[i] = 1

    for _ in range(m-1):
        tmp = [0] * n
        for i in range(n):
            for v in value:
                if i + v >= Z:
                    tmp[Z] = counter[i] + tmp[Z]
                else:
                    tmp[i + v] = counter[i] + tmp[i+v]
        counter = tmp
    result = sum(counter[Z:])
    return result / K ** m

def main():
    print(dice(6,100,380))


if __name__ == "__main__":
    main()
