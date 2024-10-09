nested_list = [1, 'a', [2, 'b', 3], [[4], 'hello', [5, [6, 7]]], 8, 'z', [2, 3]]

def summer(_list, _sum, total_loop, total_recurs):
    
    total_recurs = total_recurs + 1
    
    for item in _list:
        
        if isinstance(item, int):#here we know it is a number and add that number to the sum of all the numbers
            _sum += item         
            total_loop = total_loop + 1

        elif isinstance(item, list):#right here is when we know we have an array instead of a number
            total_loop = total_loop + 1
            _sum, total_loop, total_recurs,  = summer(item, _sum, total_loop, total_recurs)

    return _sum, total_loop, total_recurs, 

def depth(_list):
    depth_count = 0
    max_depth = 0

    for item in _list:
        
        if isinstance(item, list):
            
            depth_count = depth(item) + 1

            if depth_count > max_depth:
                max_depth = depth_count

    return max_depth

g = depth(nested_list)
print("\nmax depth of nested lists: ", g)

x, y, z = summer(nested_list, 0, 0, 0)
print("sum of all integers: ", x )
print("number of items: ", y )
print( "number of recursions: ", z,"\n")
