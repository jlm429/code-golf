import java.util.LinkedList;


class MinStack {

    /** initialize your data structure here. */
    LinkedList<ListNode2> ll = new LinkedList();

    public MinStack() {
        //empty constructor
    }

    public void push(int x) {
        ListNode2 node;
        if (this.ll.size()==0 || x<this.ll.peekFirst().min){
            node = new ListNode2(x,x);
        }
        else{
            node = new ListNode2(x, this.ll.peekFirst().min);
        }
        this.ll.push(node);
    }

    public void pop() {
        if (this.ll.size()!=0){
            this.ll.pop();
        }
    }

    public int top() {
        return this.ll.peekFirst().val;
    }

    public int getMin() {
        return this.ll.peekFirst().min;
    }
}

