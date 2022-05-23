import heapq
import numpy as np

goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]


def manhattan(state):
    xycoord = {1: [0,0], 2: [0,1], 3: [0,2], 4: [1,0], 5: [1,1], 6: [1,2], 7: [2,0], 8: [2,1], 0: [2,2]}
    arr = np.array(state)
    arr_ = np.reshape(arr, (3,3))
    goalstate = np.array(goal)
    goalstate_ = np.reshape(goalstate, (3,3))
    h = 0
    for i in range(3):
        for j in range(3):
            if (arr_[i][j] != 0):
                if (arr_[i][j] != goalstate_[i][j]):
                    val = arr_[i][j]
                    coord = xycoord[val]
                    h += abs(i - coord[0]) + abs(j - coord[1])
                
    return h

#given a state of the puzzle, represented as a single list of integers with 
#0 in the empty space, print to the console all of the possible successor
#states
def print_succ(state):
    liststate = []
    temp = [0,0,0,0,0,0,0,0,0]
    for i in range(len(state)):
        temp[i] = state[i]
    temp1 = [0,0,0,0,0,0,0,0,0]
    for i in range(len(state)):
        temp1[i] = state[i]
    temp2 = [0,0,0,0,0,0,0,0,0]
    for i in range(len(state)):
        temp2[i] = state[i]
    temp3 = [0,0,0,0,0,0,0,0,0]
    for i in range(len(state)):
        temp3[i] = state[i]
    if (0 == state[0] or 0 == state[2] or 0 == state[6] or 0 == state[8]):
        if (0 == state[0]):
            temp[0] = state[1]
            temp[1] = 0
            liststate.append(temp)
            temp1[0] = state[3]
            temp1[3] = 0
            liststate.append(temp1)
            sorted(liststate)
            for i in range(len(liststate)):
                h = manhattan(liststate[i])
                print("{} h:{}".format(liststate[i], h))
        elif (0 == state[2]):
            temp[2] = state[1]
            temp[1] = 0
            liststate.append(temp)
            temp1[2] = state[5]
            temp1[5] = 0
            liststate.append(temp1)
            sorted(liststate)
            for i in range(len(liststate)):
                h = manhattan(liststate[i])
                print("{} h:{}".format(liststate[i], h))
        elif (0 == state[6]):
            temp[6] = state[3]
            temp[3] = 0
            liststate.append(temp)
            temp1[6] = state[7]
            temp1[7] = 0
            liststate.append(temp1)
            sorted(liststate)
            for i in range(len(liststate)):
                h = manhattan(liststate[i])
                print("{} h:{}".format(liststate[i], h))
        elif (0 == state[8]):
            temp[8] = state[5]
            temp[5] = 0
            liststate.append(temp)
            temp1[8] = state[7]
            temp1[7] = 0
            liststate.append(temp1)
            sorted(liststate)
            for i in range(len(liststate)):
                h = manhattan(liststate[i])
                print("{} h:{}".format(liststate[i], h))
    elif (0 == state[1] or 0 == state[3] or 0 == state[5] or 0 == state[7]):
        if (0 == state[1]):
            temp[1] = state[0]
            temp[0] = 0
            liststate.append(temp)
            temp1[1] = state[2]
            temp1[2] = 0
            liststate.append(temp1)
            temp2[1] = state[4]
            temp2[4] = 0
            liststate.append(temp2)
            sorted(liststate)
            for i in range(len(liststate)):
                h = manhattan(liststate[i])
                print("{} h:{}".format(liststate[i], h))
        elif (0 == state[3]):
            temp[3] = state[0]
            temp[0] = 0
            liststate.append(temp)
            temp1[3] = state[4]
            temp1[4] = 0
            liststate.append(temp1)
            temp2[3] = state[6]
            temp2[6] = 0
            liststate.append(temp2)
            sorted(liststate)
            for i in range(len(liststate)):
                h = manhattan(liststate[i])
                print("{} h:{}".format(liststate[i], h))
        elif (0 == state[5]):
            temp[5] = state[2]
            temp[2] = 0
            liststate.append(temp)
            temp1[5] = state[4]
            temp1[4] = 0
            liststate.append(temp1)
            temp2[5] = state[8]
            temp2[8] = 0
            liststate.append(temp2)
            sorted(liststate)
            for i in range(len(liststate)):
                h = manhattan(liststate[i])
                print("{} h:{}".format(liststate[i], h))
        elif (0 == state[7]):
            temp[7] = state[4]
            temp[4] = 0
            liststate.append(temp)
            temp1[7] = state[6]
            temp1[6] = 0
            liststate.append(temp1)
            temp2[7] = state[8]
            temp2[8] = 0
            liststate.append(temp2)
            sorted(liststate)
            for i in range(len(liststate)):
                h = manhattan(liststate[i])
                print("{} h:{}".format(liststate[i], h))
        #3 successors
    elif (0 == state[4]):
        temp[4] = state[1]
        temp[1] = 0
        liststate.append(temp)
        temp1[4] = state[3]
        temp1[3] = 0
        liststate.append(temp1)
        temp2[4] = state[5]
        temp2[5] = 0
        liststate.append(temp2)
        temp3[4] = state[7]
        temp3[7] = 0
        liststate.append(temp3)
        sorted(liststate)
        for i in range(len(liststate)):
                h = manhattan(liststate[i])
                print("{} h:{}".format(liststate[i], h))
        #4 successors
    return None

def get_succ(state):
    liststate = []
    temp = [0,0,0,0,0,0,0,0,0]
    for i in range(len(state)):
        temp[i] = state[i]
    temp1 = [0,0,0,0,0,0,0,0,0]
    for i in range(len(state)):
        temp1[i] = state[i]
    temp2 = [0,0,0,0,0,0,0,0,0]
    for i in range(len(state)):
        temp2[i] = state[i]
    temp3 = [0,0,0,0,0,0,0,0,0]
    for i in range(len(state)):
        temp3[i] = state[i]
    if (0 == state[0] or 0 == state[2] or 0 == state[6] or 0 == state[8]):
        if (0 == state[0]):
            temp[0] = state[1]
            temp[1] = 0
            liststate.append(temp)
            temp1[0] = state[3]
            temp1[3] = 0
            liststate.append(temp1)
        elif (0 == state[2]):
            temp[2] = state[1]
            temp[1] = 0
            liststate.append(temp)
            temp1[2] = state[5]
            temp1[5] = 0
            liststate.append(temp1)
        elif (0 == state[6]):
            temp[6] = state[3]
            temp[3] = 0
            liststate.append(temp)
            temp1[6] = state[7]
            temp1[7] = 0
            liststate.append(temp1)
        elif (0 == state[8]):
            temp[8] = state[5]
            temp[5] = 0
            liststate.append(temp)
            temp1[8] = state[7]
            temp1[7] = 0
            liststate.append(temp1)
    elif (0 == state[1] or 0 == state[3] or 0 == state[5] or 0 == state[7]):
        if (0 == state[1]):
            temp[1] = state[0]
            temp[0] = 0
            liststate.append(temp)
            temp1[1] = state[2]
            temp1[2] = 0
            liststate.append(temp1)
            temp2[1] = state[4]
            temp2[4] = 0
            liststate.append(temp2)
        elif (0 == state[3]):
            temp[3] = state[0]
            temp[0] = 0
            liststate.append(temp)
            temp1[3] = state[4]
            temp1[4] = 0
            liststate.append(temp1)
            temp2[3] = state[6]
            temp2[6] = 0
            liststate.append(temp2)
        elif (0 == state[5]):
            temp[5] = state[2]
            temp[2] = 0
            liststate.append(temp)
            temp1[5] = state[4]
            temp1[4] = 0
            liststate.append(temp1)
            temp2[5] = state[8]
            temp2[8] = 0
            liststate.append(temp2)
        elif (0 == state[7]):
            temp[7] = state[4]
            temp[4] = 0
            liststate.append(temp)
            temp1[7] = state[6]
            temp1[6] = 0
            liststate.append(temp1)
            temp2[7] = state[8]
            temp2[8] = 0
            liststate.append(temp2)
        #3 successors
    elif (0 == state[4]):
        temp[4] = state[1]
        temp[1] = 0
        liststate.append(temp)
        temp1[4] = state[3]
        temp1[3] = 0
        liststate.append(temp1)
        temp2[4] = state[5]
        temp2[5] = 0
        liststate.append(temp2)
        temp3[4] = state[7]
        temp3[7] = 0
        liststate.append(temp3)
        #4 successors
    return sorted(liststate)

#given a state of the puzzle, perform the A* search algorithm and print 
#the path from the current state to goal state
import heapq

def solve(state):
    pq = [] #open
    trace = [] # closed
    trace_state = []
    pq_state = []
    start = state
    
    h = manhattan(state)
    parent_index = -1
    g = 0
    
    heapq.heappush(pq, (g+h, state, (g, h, parent_index)))
    pq_state.append(state)
    
    while len(pq) > 0:
        current_item = heapq.heappop(pq)
        for i in range(len(trace)):
            current_i, current_statei, (current_gi, current_hi, current_parenti) = trace[i]
            current_f, current_state, (current_g, current_h, current_parent) = current_item
            if (current_f == current_i and current_state == current_statei and current_g ==
               current_gi and current_h == current_hi and current_parent == current_parenti):
                continue
        trace.append(current_item)
        current_f, current_state, (current_g, current_h, current_parent) = current_item
        trace_state.append(current_state)
        if current_state == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
            reconstruct_path(trace, start, current_state, current_parent)
            break
        else:
            successors = get_succ(current_state)
            new_parent = len(trace) - 1
            new_g = current_g + 1
            
            for successor in successors:
                new_h = manhattan(successor)
                new_f = new_h + new_g
                
                if successor not in pq_state or successor not in trace_state:
                    heapq.heappush(pq, (new_f, successor, (new_g, new_h, new_parent)))
                    pq_state.append(successor)
                        
    return None

def reconstruct_path(came_from, start, end, endparent):
    current_parent = endparent
    current_state = end
    path = []
    counter = 0
    val = manhattan(end)
    while current_parent != -1:
        nextpath = came_from[current_parent]
        current_f, current_state, (current_g, current_h, current_parent) = nextpath
        path.append(current_state)
    path = list(reversed(path))
    for i in range(len(path)):
        counter = i
        h = manhattan(path[i])
        print("{} h={} moves: {}".format(path[i], h, i))
    h = manhattan(end)
    counter += 1
    print("{} h={} moves: {}".format(end, h, counter))
    return None