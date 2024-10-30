def min_beads_to_remove(n, necklace):
    # count initial number of red and blue beads
    total_R = necklace.count('R')
    total_B = 2*n - total_R # since total_B is the compliment of total_R

    # if already equal, no removal required
    if total_R == total_B:
        return 0
    
    # initialize left and right pointer and count red and blue beads
    left_R, left_B = 0, 0
    right_R, right_B = 0, 0

    # initialize min removal to max possible (all beads removed)
    min_removal = 2*n

    # use two pointers left and right
    for i in range(2*n):
        # update left count
        if necklace[i] == 'R':
            left_R += 1
        else:
            left_B += 1
        
        # update right pointers (compliment of left)
        right_R = total_R - left_R
        right_B = total_B - left_B

        # check if we can make left and right beads equal
        if left_R + right_R == left_B + left_B:

            # calculate number of removal
            removal = i+1 - (2*n-(i+1))
            min_removal = min(min_removal, removal)
    
    return min_removal