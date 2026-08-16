class Solution {
    public int majorityElement(int[] nums) {
        int n =nums.length;
        HashMap<Integer,Integer> map = new HashMap<>();

        for(int val:nums){
            map.put(val,map.getOrDefault(val,0)+1);
        }

        for(int cnt: map.keySet()){
            if(map.get(cnt) > n/2){
                return cnt;
            }
        }

        return -1;

        

        
    }
}