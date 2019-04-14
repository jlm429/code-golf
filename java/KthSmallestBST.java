public class KthSmallestBST {

    private int count=0;
    private int k;
    private Integer elt=null;

    public int kthSmallest(TreeNode root, int k) {
        inOrder(root);
        return this.elt;
    }

    private void inOrder(TreeNode node){
        if (node.left!=null && this.elt==null){
            inOrder(node.left);
        }
        if (this.count<this.k){
            this.count++;
            if (this.count==this.k){
                this.elt=node.val;
            }
        }
        if (node.right!=null && this.elt==null){
            inOrder(node.right);
        }
    }
}
