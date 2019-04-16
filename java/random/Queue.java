public class Queue<T> {

    private ListNode3 head;
    private ListNode3 tail;

    public Queue(){
    }

    public void enQueue(T obj){
        if (head==null){
            head=new ListNode3(obj);
            tail=head;
        }
        else {
            ListNode3 node=new ListNode3(obj);
            tail.next=node;
            tail=node;
        }
    }

    public T deQueue(){
        if (head==null) throw new NullPointerException();
        else {
            T obj=(T) head.val;
            head=head.next;
            return obj;
        }
    }

    public T peekFirst(){
        if (head==null) throw new NullPointerException();
        return (T) head.val;
    }

    public T peekLast(){
        if (tail==null) throw new NullPointerException();
        return (T) tail.val;
    }
}
