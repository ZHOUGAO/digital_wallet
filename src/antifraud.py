
'''
This program aims to accomplish the coding challenge from InsightDataScience;

A "digital wallet" company called PayMo is imaged, by which the PayMo users make
transaction;

The features to prevent fraudulent payment requests from untrusted users are implemented,
which are different relationship degrees between two IDs making transaction.

A file with "trusted" or "unverified" notices will be generated according to the different
features which limit the distance (relationship degree) between the two IDs.
'''

#install pygraph package
'''
download python-graph-master from https://github.com/pmatiello/python-graph.git
run: make install-core and make install-dot
'''

#import the modules

from pygraph.classes.graph import graph
import pygraph.algorithms.minmax
import os
import sys


## Create a function to generate the graph from the source csv file for the transaction records
def generate_graph_sub_from_csv_file(file_name):
    new_graph = graph()  #Create a data structure based on graph module
    nodes={}     #node library
    edges = {}  #edge library

    #access the transaction history file and import the data into node and edge library
    file_in = open(file_name,'r')  
    cont = file_in.readlines()
    for ii in range(1, len(cont)):
        line = cont[ii]
        line = line.strip()
        temp =  line.split(',')
        id1 = temp[1].strip()
        id2 = temp[2].strip()
        #ex_amount = float(temp[3])  'for future developing new features like adding weight'
        #new_graph.add_nodes([id1,id2])
        nodes[id1] = 0
        nodes[id2] = 0
        
        temp_list = [id1,id2]
        temp_list.sort()
        edges[tuple(temp_list)] = 0

    #collect the key lists from the libraries
    nodes2 = nodes.keys()
    edges2 = edges.keys()

    #add nodes to the data structure
    new_graph.add_nodes(nodes2)

    #add edges to the data structure
    for each_edge in edges2:
        new_graph.add_edge(tuple(each_edge))

    print "GRAGH IS GENERATED"
   
    return new_graph


## Create a function to determin the shortest distance between to IDs and return the result
def determine_dis_between_two_person(graph, ID1, ID2):
    span, dist = pygraph.algorithms.minmax.shortest_path(graph, ID1)
    result = dist[ID2]
    return result


## Create a function to scan the curren transaction data using the graph generated by the history transaction
## and create an output file for the notice information based on different relationship degree
def get_payment_notice(history_file, scan_file, output_file, relation_degree=1, max_payment_amount = 10000):
    distance = relation_degree
    scanned_file = open(scan_file, 'r') #access the file to be scanned
    file_out = open(output_file, 'w') #set up an output file

    #generate a new graph dat structure based on the history transaction
    Graph = generate_graph_sub_from_csv_file(history_file)

    #scan the current file and calculate the relationship distance for each line
    cont = scanned_file.readlines()
    for ii in range(1, len(cont)):
        line = cont[ii]
        line = line.strip()
        temp =  line.split(',')
        id1 = temp[1].strip()
        id2 = temp[2].strip()

        #add on an additional feature to warn the payment limit exceeding
        payment = float(temp[3])
        if payment > max_payment_amount:
            file_out.write('warning for exceeding the maximum payment limit' + '\n')
            continue

        #calculate the closest path between the two IDs
        dist = determine_dis_between_two_person(Graph, id1, id2)

        #file output depending on difference distance (relationship degree)
        if dist <= distance:
            file_out.write('trusted' + '\n')
        else:
            file_out.write('unverified' + '\n')
            
    print output_file + " is generated" +'\n'
    file_out.close()


## A function to collect file names from the input arguments
def get_file_names():
    if len(sys.argv) != 6:
        print "please type in the names of all the 5 necessary files following the current python file"
        exit()
    List = sys.argv
    return List


if __name__ == "__main__":
    #get the necessary file names from arugument
    file_list = get_file_names()
    history_transaction_file = file_list[1]
    current_transaction_file = file_list[2]
    output1 = file_list[3]
    output2 = file_list[4]
    output3 = file_list[5]

    #Create a notice information file based on Feature 1 with 1st degree friend relationship
    get_payment_notice(history_transaction_file, current_transaction_file, output1, 1)

    #Create a notice information file based on Feature 2 with 2st degree friend relationship
    get_payment_notice(history_transaction_file, current_transaction_file, output2, 2)

    #Create a notice information file based on Feature 3 with 4st degree friend relationship
    get_payment_notice(history_transaction_file, current_transaction_file, output3, 3)

