package algorithm;

import java.util.LinkedList;
import java.util.List;

/**
 * Created by erik on 2016/5/25.
 */
public class Permutations {

    public List<List<Integer>> permute(int[] nums) {
        if(nums == null || nums.length == 0)
            return null;
        List<List<Integer>>[] dp = new List[nums.length];
        for(int i = 0; i < nums.length; i++) {
            List<List<Integer>> res = new LinkedList<>();
            if(i == 0) {
                List<Integer> list = new LinkedList<>();
                list.add(nums[0]);
                res.add(list);
                dp[0] = res;
            }
            else {
                for(List<Integer> lastList : dp[i - 1]) {
                    for(int j = 0; j < i + 1; j++) {
                        List<Integer> list = new LinkedList<>(lastList);
                        list.add(j, nums[i]);
                        res.add(list);
                    }
                }
                dp[i] = res;
            }
        }
        return dp[nums.length - 1];
    }
}
