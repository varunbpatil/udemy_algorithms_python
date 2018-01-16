# Aho-Corasick pattern matching
#
# Resources:
# 1. Youtube
#    - https://www.youtube.com/watch?v=ePafMI_rSJg (Step1: Building Trie)
#    - https://www.youtube.com/watch?v=qPyhPXPl3T4 (Step2: Adding fallback)
#    - https://www.youtube.com/watch?v=IcXimoT_YXA (Step3: Actual pattern matching)
#
#    (Youtube is the easiest to understand)
#
# 2. geeksforgeeks
#    - https://www.geeksforgeeks.org/aho-corasick-algorithm-pattern-searching/
#
# 3. Python implementation
#    - https://github.com/coells/100days/blob/master/day%2034%20-%20aho-corasick.ipynb
#
# In this file, I will be trying out my own implementation from scratch.
# The code has been written so that it is easy to understand the algorithm
# and not with an intention to write a highly pythonic code in a few lines
# that nobody can understand.
#
# defaultdict:
#     The argument to defaultdict() specifies the default "value" that should be
#     returned when you access a dict "key" like d["key"] and "key" is not present
#     in the dictionary.


from collections import defaultdict
from itertools import count


# Data structures that are required for Aho-corasick algorithm
def aho_corasick():
    # Finite State Automaton
    #
    # Input: Tuple (current state, char)
    # Output: new state
    #
    # Returns an increasing "state" number when key is not already present in
    # the dictionary.
    #
    # Think of "states" as nodes of the tree and "characters" as the edges of the tree.
    G = defaultdict(count(start=1, step=1).__next__)


    # Fallback states
    #
    # Input: current state
    # Output: Fallback state
    #
    # By default, fallback to root (state 0).
    F = defaultdict(lambda: 0)


    # Outputs
    #
    # Input: current state
    # Output: Set of strings corresponding to the given state
    #
    # A state can correspond to multiple string outputs (a "set" of string outputs)
    # The string outputs must be one among the given patterns.
    O = defaultdict(set)


    # Outgoing chars from given state
    #
    # Input: current state
    # Output: Set of characters that have outgoing edges from this state to a new state.
    #
    # A given state can branch out to multiple other states.
    #
    # This is defined more as a convinience data structure.
    # For example, to check whether there is an outgoing node for char 'c' from state 's',
    # there are two ways to do it...
    # 1. if (s, c) in G
    # 2. if c in C[s]
    C = defaultdict(set)

    return (G, F, O, C)



# Step1: Contruct a Trie data structure given a list of patterns.
def build_trie(list_of_patterns, AC):
    (G, F, O, C) = AC

    for pattern in list_of_patterns:

        state = 0 # Root of the trie

        for char in pattern:
            # Store the char that branches out from this state
            C[state].add(char)

            # Get the new state given current state and character
            state = G[(state, char)]

        O[state].add(pattern)



# Step2: Build fallback states
#        Uses BFS (queue)
def build_fallback(AC):
    (G, F, O, C) = AC

    # Fallback for root node (state 0) is itself
    F[0] = 0

    # Add the root node (state 0) to the queue
    q = [0]


    # While the queue is not empty, do...
    while q:

        # Pop the first item from the queue
        cur_state = q.pop(0)

        cur_state_fallback = F[cur_state]

        
        # Update the "fallback states" and "outputs" for each of "cur_state"s children.
        # Then, add the children into the queue.


        # Special case: If cur_state = 0 (root), its children will always have
        #               fallback state = 0 and no additions to their "outputs".
        if cur_state == 0:
            for c in C[cur_state]:
                child_state = G[(cur_state, c)]
                F[child_state] = 0
                q.append(child_state)
        else:
            for c in C[cur_state]:
                child_state = G[(cur_state, c)]

                # Go up the fallback chain starting from "cur_state_fallback"
                # until you find a fallback state that has an outgoing edge
                # for char 'c' or you reach the root (state = 0).
                while (cur_state_fallback != 0) and (c not in C[cur_state_fallback]):
                    cur_state_fallback = F[cur_state_fallback]

                # If you are at this point, it means...
                # 1. You have reached the root (cur_fallback_state = 0) OR
                # 2. The fallback state that cur_state_fallback is currently referring
                #    to has an outgoing edge for char 'c'.
                #
                # Set the fallback state for "child_state"
                F[child_state] = G[(cur_state_fallback, c)] if (cur_state_fallback, c) in G else 0


                # You now have to add the "outputs" from F[child_state] to the child_state.
                # Since "outputs" of both states are python sets, you have do a merge operation.
                O[child_state] = O[child_state].union(O[F[child_state]])


                # Now, add the child_state to the queue
                q.append(child_state)



def search(test_string, AC):
    (G, F, O, C) = AC
    state = 0

    for i, c in enumerate(test_string):
        # If the current state has an outgoing edge for char 'c', follow that edge.
        # Otherwise, we need to go to fallback states.
        if c in C[state]:
            state = G[state, c]
            if O[state]:
                print("Found " + str(O[state]) + " ending @ " + str(i))
        else:
            # Go up the fallback chain until you find a fallback state that
            # has an outgoing edge for char 'c' or you reach the root (state 0).
            while (state != 0) and (c not in C[state]):
                state = F[state]

            # At this point, either...
            # 1. You are at root (state 0) OR
            # 2. "state" has an outgoing edge for char 'c'
            if c in C[state]:
                state = G[state, c]
                if O[state]:
                    print("Found " + str(O[state]) + " ending @ " + str(i))






AC = aho_corasick()
build_trie(["bar", "ara", "bara", "barbara"], AC)
build_fallback(AC)
search("barbarian barbara said: barabum", AC)
