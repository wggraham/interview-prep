from collections import deque, defaultdict
import sys

'''Deterministic finite automaton(DFA) is a finite state machine that accepts/rejects finite strings of symbols and only produces a unique computation (or run) of the automation for each input string.

DFAs can be represented using state diagrams. For example, in the automaton shown below, there are three states: S0, S1, and S2 (denoted graphically by circles). The automaton takes a finite sequence of 0s and 1s as input. For each state, there is a transition arrow leading out to a next state for both 0 and 1. Upon reading a symbol, a DFA jumps deterministically from a state to another by following the transition arrow. For example, if the automaton is currently in state S0 and current input symbol is 1 then it deterministically jumps to state S1. A DFA has a start state (denoted graphically by an arrow coming in from nowhere) where computations begin, and a set of accept states (denoted graphically by a double circle) which help define when a computation is successful.

img

These are some strings above DFA accepts,

0
00
000
11
110
1001
You are given a DFA in input and an integer N. You have to tell how many distinct strings of length N the given DFA accepts. Return answer modulo 109+7.

Notes

Assume each state has two outgoing edges(one for 0 and one for 1). Both outgoing edges won’t go to the same state.
There could be multiple accept states, but only one start state.
A start state could also be an accept state.
Input format

States are numbered from 0 to K-1, where K is total number of states in DFA.
You are given three arrays A, B, C and two integers D and N.
Array A denotes a 0 edge from state numbered i to state A[i], for all 0 ≤ i ≤ K-1
Array B denotes a 1 edge from state numbered i to state B[i], for all 0 ≤ i ≤ K-1
Array C contains indices of all accept states.
Integer D denotes the start state.
Integer N denotes you have to count how many distinct strings of length N the given DFA accepts.
Constraints       

1 ≤ K ≤ 50  

1 ≤ N ≤ 104

Example :

For the DFA shown in image, input is
A = [0, 2, 1]
B = [1, 0, 2]
C = [0]
D = 0

Input 1
-------
N = 2
Strings '00' and '11' are only strings on length 2 which are accepted. So, answer is 2.

Input 2
-------
N = 1
String '0' is the only string. Answer is 1.'''


class Solution:
    # exceeds memory limit, switch to DFS and saving partial sums approach
    def automata(self, zero_edges, one_edges, accept_states, start_state, n):
        zero_edges = {i: v for i, v in enumerate(zero_edges)}
        one_edges = {i: v for i, v in enumerate(one_edges)}
        accept_states = set(accept_states)
        q = deque([(0, start_state, 1), (1, start_state, 1)])
        total = 0
        while q:
            val, state, length = q.popleft()
            state = zero_edges[state] if not val else one_edges[state]
            if length == n:
                total += 1 if state in accept_states else 0
                continue

            q.append((0, state, length + 1))
            q.append((1, state, length + 1))

        return total

    def automataDFS(self, zero_edges, one_edges, accept_states, start_state, n):
        sys.setrecursionlimit(10 ** 6)
        zero_edges = {i: v for i, v in enumerate(zero_edges)}
        one_edges = {i: v for i, v in enumerate(one_edges)}
        accept_states = set(accept_states)
        waysFrom = {(state, 0): 1 for state in accept_states}

        def explore(state, remaining):
            if (state, remaining) in waysFrom:
                return waysFrom[(state, remaining)]
            if remaining == 0: return 0
            waysFrom[(state, remaining)] = explore(zero_edges[state], remaining - 1) if state in zero_edges else 0
            waysFrom[(state, remaining)] += explore(one_edges[remaining], remaining - 1) if state in one_edges else 0
            return waysFrom[(state, remaining)]

        return explore(start_state, n)

    def automata3(self, zero_edges, one_edges, accept_states, start_state, n):
        zeros = {v: i for i, v in enumerate(zero_edges)}
        ones = {v: i for i, v in enumerate(one_edges)}

        states = max(len(zero_edges) - 1, len(one_edges) - 1)

        waysTo = defaultdict(int)
        waysTo.update({(zero_edges[start_state], 1): 1, (one_edges[start_state], 1): 1})

        for i in range(2, n + 1):
            for state in range(states + 1):
                waysTo[(state, i)] = (waysTo[(zeros[state], i - 1)] + waysTo[(ones[state], i - 1)]) % (10 ** 9 + 7)

            # unnecessary retarded cleanup for interviewbit.com
            # for state in range(states + 1):
            #     if (zeros[state], i - 1) in waysTo:
            #         del waysTo[(zeros[state], i - 1)]
            #     if (ones[state], i - 1) in waysTo:
            #         del waysTo[(ones[state], i - 1)]

        return sum(waysTo[(state, n)] for state in accept_states) % (10 ** 9 + 7)


A = [0, 2, 1]
B = [1, 0, 2]
C = [0]
D = 0
E = 2

A = [35, 27, 45, 1, 11, 43, 24, 26, 25, 6, 4, 12, 30, 32, 21, 18, 7, 40, 16, 48, 29, 37, 34, 46, 5, 28, 36, 47, 0, 9,
     41, 20, 22, 19, 3, 15, 14, 17, 42, 8, 23, 10, 38, 31, 2, 39, 13, 33, 44, 49]
B = [45, 37, 27, 47, 10, 14, 8, 29, 4, 25, 12, 28, 35, 19, 2, 33, 6, 38, 49, 32, 0, 16, 3, 17, 22, 31, 30, 21, 13, 26,
     7, 11, 40, 5, 41, 46, 15, 23, 48, 24, 20, 34, 42, 44, 39, 36, 18, 9, 43, 1]
C = [0, 1, 2, 3, 5, 7, 8, 9, 10, 12, 13, 15, 18, 21, 24, 26, 29, 32, 33, 35, 36, 38, 39, 41, 42, 43, 44, 47, 48, 49]
D = 14
E = 10000
test = Solution()
print(test.automata3(A, B, C, D, E))
