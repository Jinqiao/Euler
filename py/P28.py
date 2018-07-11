def p28(x):
    s = 4
    points_used = 1
    last_vertex = 3
    edge_length = 2
    for i in range(4, x * x + 1):
        # at vertex
        if i == last_vertex + edge_length * points_used:
            s = s + i
            # print(f'i:{i}, s:{s}')
            points_used = points_used + 1
            if points_used == 4:
                edge_length = edge_length + 2
                points_used = 0
                last_vertex = i + edge_length
    print(s)


p28(1001)
