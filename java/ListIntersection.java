public class ListIntersection {

    //solution 2 - check len of each, chop head of longer list, then check for intersection
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {

        //check len of each
        int dif=getListLength(headA)-getListLength(headB);

        //chop head of longer list
        if (dif>0){
            headA=chopList(headA, dif);
        }

        else if (dif<0) {
            headB=chopList(headB, dif*-1);
        }

        //check for intersection
        while (headA!=null){
            if (headA==headB){
                return headA;
            }
            headA=headA.next;
            headB=headB.next;
        }
        return null;
    }

    private int getListLength(ListNode head){
        ListNode node=head;
        int len=0;
        while(node!=null){
            len++;
            node=node.next;
        }
        return len;
    }

    private ListNode chopList(ListNode head, int n){
        ListNode node=head;
        int i=0;
        while(node!=null && i<n){
            i++;
            node=node.next;
        }
        return node;
    }
}
