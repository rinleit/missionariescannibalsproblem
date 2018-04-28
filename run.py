#!/usr/bin/python3
# -*- coding: utf-8 -*-
import math
import sys
from copy import deepcopy

# Name: Le Van Rin
# MSSV: 1413235
# Bai Tap Bonus 2 - AI
# Missionaries and Cannibals Problem

# C : Cannibals
# M : Missionaries 
class State:
    def __init__(self, C_Left, M_Left, boat, C_Right, M_Right):
        self.C_Left = C_Left
        self.M_Left = M_Left
        self.boat = boat
        self.C_Right = C_Right
        self.M_Right = M_Right

        self.cur_state = (self.C_Left, self.M_Left, self.boat, self.C_Right, self.M_Right)
        self.stack = [self.cur_state]
        self.visited = [self.cur_state]

        self.moves = (self.M2_C0, self.M0_C1, self.M0_C2, self.M1_C0, self.M1_C1)

    def is_goal(self):
        if self.C_Left == 0 and self.M_Left == 0:
            return True
        else:
            return False

    def is_valid(self):
        if self.M_Left >= 0 and self.M_Right >= 0 \
            and self.C_Left >= 0 and self.C_Right >= 0 \
            and (self.M_Left == 0 or self.M_Left >= self.C_Left) \
            and (self.M_Right == 0 or self.M_Right >= self.C_Right):
            return True
        else:
            return False
    
    def get_cur_state(self):
        return self.cur_state
         
    
    def set_state(self, newstate):
        self.C_Left, self.M_Left, self.boat, self.C_Right, self.M_Right = deepcopy(newstate)
        self.update()
        
    # Move Two missionaries
    def M2_C0(self):
        if self.boat == "left":
            self.boat = "right"
            self.M_Left -= 2
            self.M_Right += 2
        else:
            self.boat = "left"
            self.M_Left += 2
            self.M_Right -= 2
        
        if not self.is_valid():
            return False
        else:
            self.update()
            return self.add_stack()
            
    # Move Two cannibals 
    def M0_C2(self):
        if self.boat == "left":
            self.boat = "right"
            self.C_Left -= 2
            self.C_Right += 2
        else:
            self.boat = "left"
            self.C_Left += 2
            self.C_Right -= 2
        
        if not self.is_valid():
            return False
        else:
            self.update()
            return self.add_stack()
    
    def update(self):
        self.cur_state = (self.C_Left, self.M_Left, self.boat, self.C_Right, self.M_Right)
    # Move One missionary and one cannibal
    def M1_C1(self):
        if self.boat == "left":
            self.boat = "right"
            self.C_Left -= 1
            self.C_Right += 1
            self.M_Left -= 1
            self.M_Right += 1
        else:
            self.boat = "left"
            self.M_Left += 1
            self.M_Right -= 1
            self.C_Left += 1
            self.C_Right -= 1
        
        if not self.is_valid():
            return False
        else:
            self.update()
            return self.add_stack()
    
    # Move One missionary 
    def M1_C0(self):
        if self.boat == "left":
            self.boat = "right"
            self.M_Left -= 1
            self.M_Right += 1
        else:
            self.boat = "left"
            self.M_Left += 1
            self.M_Right -= 1
        
        if not self.is_valid():
            return False
        else:
            self.update()
            return self.add_stack()
    
    # Move one cannibal 
    def M0_C1(self):
        if self.boat == "left":
            self.boat = "right"
            self.C_Left -= 1
            self.C_Right += 1
        else:
            self.boat = "left"
            self.C_Left += 1
            self.C_Right -= 1
        
        if not self.is_valid():
            return False
        else:
            self.update()
            return self.add_stack()
    
    def add_stack(self):
        cur_state = self.get_cur_state()
        if cur_state not in self.visited:
            self.stack.append(cur_state)
            return True
        return False

def breadth_first_search(state):
    if state.is_goal():
        return state.cur_state

    stack = [[state.cur_state], ]

    while state.stack:
        cur_state = state.stack.pop(0)
        path = stack.pop(0)
        state.visited.append(cur_state)
        for move in state.moves:
            state.set_state(cur_state)
            if move():
                if state.is_goal():
                    result = path + [state.cur_state]
                    return result
                stack.append(path + [state.cur_state])
    return None


def depth_first_search(state):
    if state.is_goal():
        return state.cur_state

    stack = [[state.cur_state], ]

    while state.stack:
        cur_state = state.stack.pop()
        path = stack.pop()
        state.visited.append(cur_state)
        for move in state.moves:
            state.set_state(cur_state)
            if move():
                if state.is_goal():
                    result = path + [state.cur_state]
                    return result
                stack.append(path + [state.cur_state])
    return None


def print_path(path):
        child = path.pop(0)
        print("| %s - %s %s %s - %s |" % (str(child[0]), str(child[1]), "<START>", str(child[3]), str(child[4])))
        for child in path:
            print("| %s - %s %s %s - %s |" % (str(child[0]), str(child[1]), "<======" if child[2] is "left" else "======>", str(child[3]), str(child[4])))

def main(algorithm):
    start_state = State(3,3,'left',0,0)
    if algorithm == 1:
        path = breadth_first_search(start_state)
    else:
        path = depth_first_search(start_state)
    print("=== Missionaries and Cannibals Problem ===")
    print("| C_Left, M_Left, boat, C_Right, M_Right |")
    print(" Solution:")
    print_path(path)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "dfs":
            main(1)
        elif sys.argv[1] == "bfs":
            main(2)
    
