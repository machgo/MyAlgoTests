import java.util.Iterator;
import java.util.NoSuchElementException;

public class MyLinkedList<E> implements List<E> {

	// auxiliary class for the nodes
	class LNode implements Position<E>{
		E elem;
		LNode prev,next; 
		Object creator = MyLinkedList.this;
		@Override
		public E element() {
			return elem;
		}		
	}
	
	// instance variables of MyLinkedList
	private LNode first,last;
	private int size;

	private LNode castToLNode(Position p){
		LNode n;
		try {
			n = (LNode) p;
		} catch (ClassCastException e) {
			throw new RuntimeException("This is not a Position belonging to MyLinkedList"); 
		}
		if (n.creator == null) throw new RuntimeException("position was already deleted!");
		if (n.creator != this) throw new RuntimeException("position belongs to another MyLinkedList instance!");			
		return n;
    }
	
	@Override
	public Position<E> first() {
		return first;
	}

	@Override
	public Position<E> last() {
		return last;
	}

	@Override
	public boolean isFirst(Position<E> p) {
		// TODO Auto-generated method stub
		return false;
	}

	@Override
	public boolean isLast(Position<E> p) {
		// TODO Auto-generated method stub
		return false;
	}

	@Override
	public Position<E> next(Position<E> p) {
		LNode n = (LNode) p;
		if (n.creator != this)throw new RuntimeException("invalid position");
		return n.next;
	}

	@Override
	public Position<E> previous(Position<E> p) {
		LNode n = (LNode) p;
		if (n.creator != this)throw new RuntimeException("invalid position");
		return n.prev;
	}

	@Override
	public E replaceElement(Position<E> p, E o) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public Position<E> insertFirst(E o) {
		LNode n = new LNode();
		n.elem = o;
		n.next = first;
		if (first != null)	first.prev = n;
		else last = n;
		first = n;
		size++;
		return n;
	}

	@Override
	public Position<E> insertLast(E o) {
		LNode n = new LNode();
		n.elem = o;
		n.prev = last;
		if (last != null)	last.next = n;
		else first = n;
		last = n;
		size++;
		return n;
	}

	@Override
	public Position<E> insertBefore(Position<E> p, E o) {
        LNode n = new LNode();
		LNode pn = castToLNode(p);

        n.elem = o;
        if (pn.prev != null)
        {
            pn.prev.next = n;
            n.prev = pn.prev;
        }
        else
        {
            //is first entry
            last = n;
            n.prev = null;
        }
        pn.prev = n;
        n.next = pn;
        return n;
	}

	@Override
	public Position<E> insertAfter(Position<E> p, E o) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public void remove(Position<E> p) {
        LNode pn = (LNode) p;
        //if first 
        if (pn.prev == null)
        {
            first = pn.next;
            pn.next.prev = null;
        }
        else
            pn.prev.next = pn.next;
        //if last
        if (pn.next == null)
        {
            last = pn.prev;
            pn.prev.next = null;
        }
        else
            pn.next.prev = pn.prev;

        pn = null;

	}

	@Override
	public Iterator<Position<E>> positions() {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public Iterator<E> elements() {
		return new Iterator<E>(){
			LNode currentNode = first;

			@Override
			public boolean hasNext() {
				return currentNode != null;
			}

			@Override
			public E next() {
				if (currentNode == null) throw new NoSuchElementException("there are no more elments in this LinkedList");
				LNode ret = currentNode;
				currentNode = currentNode.next;
				return ret.elem;
			}
		};
	}

	@Override
	public int size() {
		// TODO Auto-generated method stub
		return 0;
	}

	@Override
	public boolean isEmpty() {
		// TODO Auto-generated method stub
		return false;
	}

    public String printAll()
    {
        LNode p = (LNode)first;
        String output = "";
        while(p != null)
        {
            output += p.element();
            output += " | ";
            p = p.next;
        }
        return output;
    }


	public static void main(String[] args) {
		List<String> ll = new MyLinkedList<>(); 
		Position<String> p = ll.insertFirst("hans");
		ll.insertFirst("ida");
        System.out.println(((MyLinkedList)ll).printAll());
		ll.insertAfter(p,"hans 2");
        System.out.println(((MyLinkedList)ll).printAll());
        ll.insertBefore(p, "blubb");
        System.out.println(((MyLinkedList)ll).printAll());
        ll.remove(ll.previous(p));
        System.out.println(((MyLinkedList)ll).printAll());
//		Iterator<String> it = ll.elements();
//		while (it.hasNext()){
//			String s = it.next();
//			System.out.println(s);
//		}
	}
}
