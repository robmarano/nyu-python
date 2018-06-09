#!/usr/bin/env python3

if __name__ == "__main__":
    add = lambda x,y,z: x+y+z
    nums_x = [1,2,3]
    nums_y = [1,2,3]
    nums_z = [1,2,3]
    results = add(nums_x,nums_y,nums_z)
    print(results)

    results_2 = list(map(add, nums_x, nums_y, nums_z))
    print(results_2)

    is_even = lambda x: x % 2 == 0
    results_3 = list(filter(is_even,add(nums_x,nums_y,nums_z)))
    print(results_3)

