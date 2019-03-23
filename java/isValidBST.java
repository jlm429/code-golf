class isValidBST {
    private static boolean checkValidBST(TreeNode node, Integer min, Integer max){

        if (node==null){
            return Boolean.TRUE;
        }

        if (min!=null && node.val <= min){
            return Boolean.FALSE;
        }

        if (max!=null && node.val >= max){
            return Boolean.FALSE;
        }

        if (!checkValidBST(node.left, min, node.val) || !checkValidBST(node.right, node.val, max)){
            return Boolean.FALSE;
        }

        return Boolean.TRUE;

    }

    public static boolean isValidBST(TreeNode root) {
        //base case - node is null
        //if (node==null):
        return checkValidBST(root, null, null);

    }
}