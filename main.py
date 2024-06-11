import sys 

def graduation_ceremony(N, min_attendance):
    matrix = [[0] * (min_attendance + 1) for _ in range(N + 1)] 

    for i in range(min_attendance):
        matrix[0][i] = 1 

    for i in range(1, N + 1): 
        for j in range(min_attendance - 1, -1, -1):
            matrix[i][j] = matrix[i - 1][0] + matrix[i - 1][j + 1]

    ways_to_attend = matrix[N][0]
    probability_miss = matrix[N - 1][1]

    return f"{probability_miss}/{ways_to_attend}"

if __name__ == "__main__":
    N = int(sys.argv[1])
    min_attendance = 4 
    rs = graduation_ceremony(N, min_attendance)
    print(rs)
