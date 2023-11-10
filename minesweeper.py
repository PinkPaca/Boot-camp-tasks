#input
mine_grid=[["-","-","-","#","#"],
           ["-","#","-","-","-"],
           ["-","-","#","-","-"],
           ["-","#","#","-","-"],
           ["-","-","-","-","-"]]

def mine_counter(initial_map):
    row_num=len(initial_map)
    col_num=len(initial_map[0])
    dx=[-1,-1,-1,0,0,1,1,1]
    dy=[-1,0,1,-1,1,-1,0,1]

    mine_num=[[None]*row_num for _ in range (col_num)]

    #extend initial_map to ensure about the edges
    initial_map.insert(0,['-']*row_num)
    initial_map.append(['-']*row_num)

    for i in range(row_num+2):
        initial_map[i].insert(0,['-'])
        initial_map[i].append(['-'])

    for i in range(1,row_num+1):
        for j in range(1,col_num+1):
            adj_mine=0
            if initial_map[i][j] == "#":
                mine_num[i-1][j-1]="#"
            else:
                for k in range(8):
                    if initial_map[i+dx[k]][j+dy[k]]=="#":
                        adj_mine=adj_mine+1
                
                mine_num[i-1][j-1]=str(adj_mine)
    return mine_num



print(mine_counter(mine_grid))