

import java.util.LinkedList;
import java.util.List;

public class levelOrderTraversal {

    private List<List<Integer>> levelList=new LinkedList<>();

    public List<List<Integer>> levelOrder(TreeNode root){
        if (root==null){
            return this.levelList;
        }
        getLevelList(root, 0);
        zigZagOrder();
        return this.levelList;
    }

    private void zigZagOrder(){
        for (int i=1; i<this.levelList.size(); i=i+2){
            reverseList(i);
        }
    }

    private void reverseList(int level){
        List<Integer> reverseList=new LinkedList<>();
        List<Integer> list = new LinkedList<>(this.levelList.get(level));
        for (int i=list.size()-1; i>=0; i--){
            reverseList.add(list.get(i));
        }
        this.levelList.set(level, reverseList);
    }


    private void getLevelList(TreeNode node, int level){
        if (node==null){
            return;
        }

        else {
            if (this.levelList.size()<=level){
                List<Integer> temp = new LinkedList<>();
                this.levelList.add(temp);
            }
            this.levelList.get(level).add(node.val);
            level++;
            getLevelList(node.left, level);
            getLevelList(node.right, level);
        }
    }
}
