def count_gold(pyramid: list[list[int]]) -> int:
    l = []
    neighbour = []
    
    # add first list (single element) to master list    
    l.append(pyramid[0])

    # store highest possible adjacent index
    for i in range(pyramid[1], len(pyramid)):


    return


print("Example:")
print(
    count_gold(
        [
            [1],
            [2, 3],
            [3, 3, 1],
            [3, 1, 5, 4],
            [3, 1, 3, 1, 3],
            [2, 2, 2, 2, 2, 2],
            [5, 6, 4, 5, 6, 4, 3],
        ]
    )
)

print(count_gold(
        [
            [1],
            [2, 1],
            [1, 2, 1],
            [1, 2, 1, 1],
            [1, 2, 1, 1, 1],
            [1, 2, 1, 1, 1, 1],
            [1, 2, 1, 1, 1, 1, 9],
        ]
    ))