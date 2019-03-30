import java.util.LinkedList;
import java.util.List;

public class inorderTreeTraversal {

    List<Integer> list=new LinkedList<>();

    public List<Integer> inorderTraversal(TreeNode root) {

        if (root==null){
            return this.list;
        }

        inorder(root);
        return this.list;
    }

    private void inorder(TreeNode node){
        if (node.left!=null){
            inorder(node.left);
        }
        this.list.add(node.val);
        if (node.right!=null){
            inorder(node.right);
        }
    }
}
