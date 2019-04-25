# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 09:00:18 2019

@author: zhangwx
"""

'如何实现链表的逆序'

'''
1 就地逆序
时间复杂度O(N) 空间复杂度O(1)
''' 
class LNode:
    def __init__(self,x):
        self.data = x
        self.next = None
        
def Reverse(head):
    #判断链表是否为空
    if head == None or head.next == None:
        return
    pre = None
    cur = None
    next = None
    #star reverse
    cur = head.next
    next = cur.next
    cur.next = None
    pre = cur
    cur = next
    #while循环遍历
    while cur.next != None:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next 
    #链表最后一个节点
    cur.next = pre
    #head node
    head.next = cur
    
'''
3 插入法
'''    
def Reverse2(head):
    if head == None or head.next == None:
        return
    cur = None
    next = None
    cur = head.next.next
    head.next.next = None
    while cur is not None:
        next = cur.next
        cur.next = head.next
        head.next = cur
        cur = next
        
    
if __name__=="__main__":
    i = 1
    head = LNode(None)
    head.next = None
    tmp = None
    cur = head
    while i<8 :
        tmp = LNode(i)
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1
    print("逆序前: ",end='')
    cur = head.next
    while cur != None:
        #print(cur.data,"", end='')
        print('{} '.format(cur.data),end='')
        cur = cur.next
    print('\n' + "逆序后: ",end='')
    
    Reverse(head)
    cur = head.next
    while cur != None:
        #print(cur.data,"", end='')
        print('{} '.format(cur.data),end='')
        cur = cur.next
            
    print('\n' + "逆序后: ",end='')
    Reverse2(head)
    cur = head.next
    while cur != None:
        #print(cur.data,"", end='')
        print('{} '.format(cur.data),end='')
        cur = cur.next
    
'''
2 递归法
时间复杂度O(N)
'''


        
    
    
    
    
    