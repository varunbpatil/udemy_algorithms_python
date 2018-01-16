# Backtracking algorithm to place 'n' queens on a (n X n) chess board.


def is_a_solution(arr, n, cur_row, cur_col):
    for r in range(cur_row):
        # same col means not a solution
        if arr[r][cur_col] == 1:
            return False

        # queen on diag means not a solution
        r_diff = cur_row - r
        if (cur_col - r_diff >= 0) and (arr[r][cur_col - r_diff] == 1):
            return False
        
        if (cur_col + r_diff < n) and (arr[r][cur_col + r_diff] == 1):
            return False

    return True



# arr is of size (n X n). Contains all '0's to begin with. '1' indicates presence of a queen.
# cur_row is 0 to start with.
def n_queens(arr, cur_row, n):

    if cur_row >= n:
        # True means we found a solution
        return True

    for cur_col in range(n):

        soln = is_a_solution(arr, n, cur_row, cur_col)

        if not soln:
            continue
        else:
            # Possible solution. Continue further to check whether this brank is ok or not.
            arr[cur_row][cur_col] = 1
            tmp = n_queens(arr, cur_row + 1, n)

            if not tmp:
                arr[cur_row][cur_col] = 0
                # we have to continue to next column
            else:
                # We have found a solution.
                # If we don't want any more solutions, we can "return tmp" here.
                # We can print the solution at the end.
                # return tmp

                # If we want all possible solutions, we can simply continue to next column
                # as though we didn't find a solution.
                # But, before that, we have to print the solution, otherwise we will lose it.
                print(arr)
                arr[cur_row][cur_col] = 0


    # If we are outside the for loop means, we did not find a solution.
    # Time to backtrack
    return False





arr = [[0]*4, [0]*4, [0]*4, [0]*4]  # Note: we cannot write [[0]*4]*4 because
                                    # we will get reference to the same list 4 times
                                    # and if we modify one list, the other 3 lists
                                    # will also get modified.
n_queens(arr, 0, 4)
