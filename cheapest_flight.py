#!/venv/bin/python3

def cheapest_flight(costs: list, a: str, b: str) -> int:
    # create dictionary to store flight costs between cities
    prices = {}

    # populate the dictionary with prices from the schedule
    for route in costs:
        city1, city2, price = route
        prices[(city1, city2)] = price
        prices[(city2, city1)] = price

    # function to recursively find the cheapest route
    def find_cheapest(current, target, visited):
        # if current city is the destination, return 0 (no cost)
        if current == target:
            return 0
        
        # count current city as visited
        visited.add(current)

        # list storing prices for possible routes
        route_prices = []

        # iterate through neighbours of the current city
        for key in prices.keys():
            if current in key:
                # find the neighbour city
                neighbour = key[0] if key[1] == current else key[1]

                # make sure neighbour has not been visited
                if neighbour not in visited:
                    # recursively find the cost of reaching the target from the neighbour
                    cost_to_target = find_cheapest(neighbour, target, visited.copy())
                
                    # if a valid route is found, add the cost to the total price
                    if cost_to_target is not None:
                        route_prices.append((prices[current, neighbour] + cost_to_target))

        # if no valid route is found, return none
        if not route_prices:
            return None
        
        # return the minimum cost among possible routes
        return min(route_prices)
    
    # find the cheapest route from a to b
    best_price = find_cheapest(a, b, set())

    return best_price if best_price is not None else 0

print (
    cheapest_flight(
        [
            ["A", "C", 40],
            ["A", "B", 20],
            ["A", "D", 20],
            ["B", "C", 50],
            ["D", "C", 70],
        ],
        "D",
        "C",
    )
    == 60
)