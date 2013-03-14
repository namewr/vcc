def calc(w_a, w_b):
    rows = len(w_a)+1
    cols = len(w_b)+1
        
    gap_cost = 1
    match_cost = 2
    dis_mat = [[i*gap_cost+j*gap_cost for j in range(cols)] for i in range(rows)]

    for i in range(1, rows):
        for j in range(1, cols):
            dis_mat[i][j] = min(dis_mat[i-1][j]+gap_cost,
                                dis_mat[i][j-1]+gap_cost,
                                dis_mat[i-1][j-1]+((w_a[i-1]!=w_b[j-1])*match_cost)) # matching cost here       

    return dis_mat[rows-1][cols-1]
