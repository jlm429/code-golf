public class mergeSort {

    //exception handling
    public static void mergeSorter(int[] array) {
        mergeSortMethod(array, 0, array.length-1);
    }


    //exception handling
    private static void mergeSortMethod(int[] array, int low, int high) {

        if (low < high) {
            int middle = (low + high) / 2;
            mergeSortMethod(array, low, middle);
            mergeSortMethod(array, middle + 1, high);
            merge(array, low, middle, high);
        }
    }

    private static void merge(int[] array, int low, int middle, int high) {
        int n1 = middle - low+1;
        int n2 = high - middle;

        int[] helperLeft = new int[n1 + 1];
        int[] helperRight = new int[n2 + 1];

        for (int i = 0; i < n1; i++) {
            helperLeft[i] = array[low + i];
        }

        for (int i = 0; i < n2; i++) {
            helperRight[i] = array[middle + i + 1];
        }

        helperLeft[n1] = Integer.MAX_VALUE;
        helperRight[n2] = Integer.MAX_VALUE;

        int i2 = 0;
        int j2 = 0;

        for (int k = low; k <= high; k++) {
            if (helperLeft[i2] <= helperRight[j2]) {
                array[k] = helperLeft[i2];
                i2 = i2 + 1;
            }

            else {
                array[k] = helperRight[j2];
                j2 = j2 + 1;
            }
        }
    }
}
