package algorithm;

/**
 * Created by erik on 2016/5/23.
 * a binary tree node
 */

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode(int x) { val = x; }
 * }
 */
public class UniqBST {
    public List<TreeNode> generateTrees(int n) {
//        if(n == 0)
//            return new LinkedList<TreeNode>();
//        return helper(1, n);
        List<TreeNode>[] dp = new List[n];
        dp[0] = new LinkedList<TreeNode>();
        dp[0].add(null);
        for(int i = 1; i <= n; i++) {
            dp[i] = new LinkedList<TreeNode>();
            for(int j = 0; j < i; j++) {
                for (TreeNode nodeL : dp[j]) {
                    for (TreeNode nodeR : dp[i - j - 1]){
                        TreeNode node = new TreeNode(j + 1);
                        node.left = nodeL;
                        node.right = clone(nodeR, j + 1);
                        dp[i].add(node);
                    }
                }
            }
        }
        return dp[n];
    }

    private TreeNode clone(TreeNode old, int offset) {
        if(null == old)
            return null;
        TreeNode res = new TreeNode(old.val + offset);
        res.left = clone(old.left, offset);
        res.right = clone(old.right, offset);
        return res;
    }

    public static void main() {
        new UniqBST().generateTrees(0);
    }

    private List<TreeNode> helper(int start, int end) {
        List<TreeNode> res = new LinkedList<TreeNode>();
        if(start > end) {
            res.add(null);
            return res;
        }
        for(int i = start; i <= end; i++) {
            List<TreeNode> left = helper(start, i - 1);
            List<TreeNode> right = helper(i + 1, end);
            for(TreeNode l : left) {
                for(TreeNode r : right) {
                    TreeNode root = new TreeNode(i);
                    root.left = l;
                    root.right = r;
                    res.add(root);
                }
            }
        }
        return res;
    }
}

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}
