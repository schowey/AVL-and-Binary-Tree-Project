#Steven Howey
#Exercise 20.2
#12/5/19
#SDEV 220

from AVLTreeClass import AVLTree
from BinaryTreeClass import BinaryTree
import random
from time import time

def main():
    bt = BinaryTree()
    createBinaryTree(bt)
    searchBinaryTree(bt)
    deleteBinaryTree(bt)
    avl = AVLTree()
    createAVLTree(avl)
    searchAVLTree(avl)
    deleteAVLTree(avl)

def createBinaryTree(tree):
    i = 0
    start_time = time()
    while i <= 50000:

        e = random.randint(0, 10000000)
        tree.insert(e)
        i += 1

    end_time = time()
    seconds_elapsed = end_time - start_time
    print ("Create Binary Tree: ", seconds_elapsed)

def searchBinaryTree(tree):


    i = 0
    start_time = time()

    for i in range (3):
        e = random.randint(0, 10000000)
        tree.search(e)
        i += 1

    end_time = time()
    seconds_elapsed = end_time - start_time
    print ("Search Binary Tree: ", seconds_elapsed)

def deleteBinaryTree(tree):


    i = 0
    start_time = time()

    for i in range(0, 50000):
        tree.delete(i)
        i += 1

    end_time = time()
    seconds_elapsed = end_time - start_time
    print ("Delete Binary Tree: ", seconds_elapsed)

def createAVLTree(tree):

    i = 0
    start_time = time()
    while i <= 50000:

        e = random.randint(0, 10000000)
        tree.insert(e)
        i += 1

    end_time = time()
    seconds_elapsed = end_time - start_time
    print ("Create AVL Tree: ", seconds_elapsed)

def searchAVLTree(tree):


    i = 0
    start_time = time()

    for i in range (3):
        e = random.randint(0, 10000000)
        tree.search(e)
        i += 1

    end_time = time()
    seconds_elapsed = end_time - start_time
    print ("Search AVL Tree: ", seconds_elapsed)

def deleteAVLTree(tree):


    i = 0
    start_time = time()

    for i in range(0, 500000):
        tree.delete(i)
        i += 1

    end_time = time()
    seconds_elapsed = end_time - start_time
    print ("Delete AVL Tree: ", seconds_elapsed)

main()