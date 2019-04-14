public class KthSmallestBST {

    private int count=0;
    private int k;
    private int elt=-5000;

    public int kthSmallest(TreeNode root, int k) {
	this.k=k;
        inOrder(root);
        return this.elt;
    }

    private void inOrder(TreeNode node){
        if (node.left!=null && this.elt==-5000){
            inOrder(node.left);
        }
        if (this.count<this.k){
            this.count++;
            if (this.count==this.k){
                this.elt=node.val;
            }
        }
        if (node.right!=null && this.elt==-5000){
            inOrder(node.right);
        }
    }
}
