def num_ways(current):
    global way
    #breakpoint()
    for step in [1, 3, 5]:
        print(1)
        print(current, step, way)
        pre = current
        current += step
        print(2)
        print(current, step, way)
        #if reached the highest stair -> raise way
        if current == 10:
            way += 1
            #current = pre
            return
        #if crossed the destination, return
        elif current > 10:
            #current = pre
            way = way
            return
        #if not reached, call the function recusively
        else:
            num_ways(current)
            current = pre
    return way
way = 0
print(num_ways(0))

