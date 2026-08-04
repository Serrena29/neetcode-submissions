class Solution {
    public int[] replaceElements(int[] arr) {

         int max_right = -1;

        for(int i = arr.length -1; i>=0; i--){
            int  temp = arr[i];
            arr[i] = max_right;
            if(temp > max_right){
                max_right = temp;
            }
        }
        return arr;
    }
}