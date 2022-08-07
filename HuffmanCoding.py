import heapq
import math
import sys
from collections import deque

class Node:
    def __init__(self, left=None, right=None, root=None):
        self.left = left
        self.right = right
        self.root = root
    def children(self):
        return((self.left, self.right))
    def getLetter(self):
        return self.root
        
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
        

def HuffmanCoding(filename):
    file = open(filename)
    text = file.read()
    
    freq = {}
    for letter in text:
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1
    
    freq = {n: freq[n]/len(text) for n in freq}

    # MinHeap
    H = []
    
    # Counter breaks ties in frequency
    counter = 0
    for x in freq:
        T_x = Node(root=x)
        heapq.heappush(H, (freq[x], counter, T_x))
        counter += 1
        
    while len(H) > 1:
        T_left = heapq.heappop(H)
        T_right = heapq.heappop(H)
        T_parent = Node(left=T_left[2], right=T_right[2], root=None)
        heapq.heappush(H, (T_left[0] + T_right[0], counter, T_parent))
        counter += 1
        
    r = H[0][2]
    codeWordMap = {}
    S = Stack()
    cw = ''
    S.push((r, ''))
    while(S.size() != 0):
        (u, cw) = S.pop()
        if u.getLetter() != None:
            codeWordMap[u.getLetter()] = cw
        if not (None in u.children()):
            S.push((u.children()[1], cw+'1'))
            S.push((u.children()[0], cw+'0'))
    
    codeWordArray = []
    for char in codeWordMap:
        codeWordArray.append(char)
    print('%-10s%-20s%-5s' % ('Character', 'Codeword', 'Frequency'))
    wtSum = 0
    for char in sorted(codeWordArray):
        print('%-10s%-20s%-5s' % (char, codeWordMap[char], str(round(freq[char]*100, 5))) + '%')
        wtSum += len(codeWordMap[char]) * freq[char]
    print('\n')
    print('Average Codeword Length: ' + str(wtSum))
    print('Original Size: ' + str(len(text)*8))
    encodedText = []
    for char in text:
        encodedText += codeWordMap[char]
    print('Encoding Size: ' + str(len(encodedText)))
    print('Compression Ratio: ' + str(round(len(encodedText)/(len(text)*8) * 100, 5)) + "%")

HuffmanCoding(sys.argv[1])