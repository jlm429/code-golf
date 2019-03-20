import java.util.Arrays;

public class shuffleArray {

    private int[] nums;
    private int[] copy;

    public shuffleArray(int[] nums){
        //this.nums=new int[nums.length];
        this.nums=nums;
        this.copy=new int[nums.length];
        for (int i=0; i<nums.length; i++){
            this.copy[i]=nums[i];
        }

    }

    public int[] shuffle(){

        int r=0;
        int temp=0;
        for (int i=0; i<this.nums.length; i++){
            r=(int) (Math.random()* ((this.nums.length-i))+i);
            temp=this.nums[i];
            this.nums[i]=this.nums[r];
            this.nums[r]=temp;
        }
        return nums;

    }

    public int[] reset(){
        return this.copy;
    }

}
