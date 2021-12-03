# Program for n’th node from the end of a Linked List

# Given a Linked List and a number n, write a function that returns the value at the n’th node from the end of the Linked List.

class Node :
    def __init__ ( self , data ) :
        self.data = data
        self.next = None

class LinkedList :
    def __init__ ( self ) :
        self.head = None
    
    def printList ( self ) :
        temp = self.head
        while ( temp ) :
            print ( temp.data )
            temp = temp.next
        
    def add ( self , data ) :
        if self.head != None :
            last = self.head
            end = self.head
            while ( end ) : 
                last = end
                end = end.next
            last.next = Node ( data )
        else : self.head = Node ( data )
    
    def size ( self ) :
        temp = self.head
        n = 0
        while ( temp ) :
            n += 1
            temp = temp.next
        return n
    
    def nthElement ( self , n ) :
        ll_length = self.size()
        if n > ll_length :
            print ( "given paramater excedes total length of linked list" )
            print ( "length of linked list = " , ll_length )
            return
        
        index = 1
        temp = self.head
        while ( index < n ) : 
            temp = temp.next
            index += 1
        print ( temp.data )

llist = LinkedList()
llist.add ( 1 )
llist.add ( 2 )
llist.add ( 3 )
llist.add ( 4 )
llist.add ( 5 )
llist.nthElement( 2 )