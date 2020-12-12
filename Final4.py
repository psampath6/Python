#!/usr/bin/env python3
###############################################################################
#
#
# Name:
#   Final4.py
#
# Input:
#
#
# Output:
#
# Purpose:
#   Implement graph data structure with adjacency list and compute if triangular
#   edges exists in the graph tree
#
# Authors:
#   Pradeep Sampath
#   April 2018
###############################################################################


import os, sys
from collections import defaultdict

class Graph(object):
    # Graph data structure
    def __init__(self, connections):
        self.graph = defaultdict(set)
        self.add_connections(connections)
        print("init -",self.graph)

    def add_connections(self, connections):
        #Add connections (list of tuple pairs) to graph
        print("add_connections -", connections)
        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        #Add connection between node1 and node2
        print("add -", node1, node2)
        self.graph[node1].add(node2)
        print("add -", self.graph)

    def is_connected(self, node1, node2):
        print("is_connected -", self.graph)

        nodes_hit = set()
        nodes = list(self.graph.keys())
        print("is_connected -", nodes)
        if node1:
            node1 = nodes[0]
            nodes_hit.add(node1)
            if len(nodes_hit) != len(nodes):
                for node in self.graph[node1]:
                    if node not in nodes_hit:
                            return True
            else:
                return True
            return False
    def find_triangle(self, g):
        print("find triangle -", g.items())

        for node1 in g.items():
            print("find triangles - node1",node1)
            for node2 in g[1]:
                print("find triangles - node2",node2)
                for node3 in g.items():
                    print("find triangles - node3",node3)
                    if self.is_connected(node2, node3) and self.is_connected(node1, node3):
                        print("find triangles - node2 and node3 are connected", )
                        return True






def bestTrio(N, from_array, to_array):


    print(from_array, to_array)

    connections = [ (from_array[n], to_array[n]) for n in range(0,N)]
    print(connections)
    print("connections - ", len(connections))

    graph1 = Graph(connections)
    print(graph1.graph)
    result = graph1.find_triangle(graph1.graph)
    print("result - ",result)
    return 1


if __name__  == "__main__" :

    friends_nodes, friends_edges = input("Enter 2 numbers : ").split(" ")
    friends_nodes, friends_edges = int(friends_nodes), int(friends_edges)
    print("\nfriends_nodes - %d, friends_edges - %d" %(friends_nodes,friends_edges))

    if (friends_nodes >= 1) and (friends_nodes <= 500):
        print("\nfriends_nodes Constraint OK !")
    else:
        print("Usage: friends_nodes should be between 1 to 500")
        exit()

    friends_from = []
    friends_to = []
    for i in range(0,friends_edges):
        f_from, f_to = input("Enter the numbers for friends_from, friends_to : ").split(" ")
        f_from = int(f_from)
        f_to = int(f_to)
        friends_from.append(f_from)
        friends_to.append(f_to)

    print(friends_from, friends_to)
    final_output = bestTrio(friends_nodes, friends_from, friends_to)
    print("Final output : %d" %final_output)
    
    