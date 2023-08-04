import java.util.*;

public class OrderStatistics {

        /*public static int orderStatistics(int[] array, int k) {
                int cont = 0;
                int lastIdx = -1;
                //int idxMinor = 0;
                while (cont < k) {
                        int idxMinor = 0;
                        for (int i = 0; i < array.length; i++) {
                                if (array[i] < array[idxMinor]) {
                                        if (lastIdx == -1 || array[i] > array[lastIdx]) {
                                                idxMinor = i;
                                        } else if (array[i] == array[lastIdx] && i != lastIdx) {
                                                idxMinor = i;
                                        }
                                }
			}
                        cont++;
                        lastIdx = idxMinor;
                }
                return array[lastIdx];
        }*/











	public static int orderStatistics(int[] array, int k) {
                int cont = 0;
                int lastIdx = -1;
                int idxMinor = 0;
                while (cont < k) {
                        for (int i = 0; i < array.length; i++) {
				if (lastIdx == -1 && array[i] < array[idxMinor]) {
					idxMinor = i;
				} else if (lastIdx > -1) {
					if (array[i] > array[lastIdx] && array[i] < array[idxMinor]) {
						idxMinor = i;
				}




                                /*if (array[i] < array[idxMinor]) {
                                        if (lastIdx == -1 || array[i] > array[lastIdx]) {
                                                idxMinor = i;
                                        } else if (array[i] == array[lastIdx] && i != lastIdx) {
                                                idxMinor = i;
                                        }
                                }*/
                        }
                        cont++;
                        lastIdx = idxMinor;
                }
		}
                return array[lastIdx];
        
	}
















        public static void main(String[] args) {

		int[] arr = new int[] {4, 12, 0, 2, 54, -1, 100, 2};
                System.out.println(Arrays.toString(arr));
                System.out.println(orderStatistics(arr, 1));
                assert orderStatistics(arr, 1) == -1;
		assert orderStatistics(arr, 2) == 0;
		assert orderStatistics(arr, 3) == 2;
		assert orderStatistics(arr, 4) == 3;
		System.out.println(orderStatistics(arr, 5));
		assert orderStatistics(arr, 5) == 4;
		System.out.println(orderStatistics(arr, 6));
		assert orderStatistics(arr, 6) == 12;
		assert orderStatistics(arr, 7) == 54;
		assert orderStatistics(arr, arr.length) == 100;
		System.out.println(Arrays.toString(arr));








               /*int[] arr = new int[] {4, 25, 12, 33, 34, 0, 9, 2, 54, 99, -1, 100, 2};
                System.out.println(Arrays.toString(arr));
                System.out.println(orderStatistics(arr, 1));
                assert orderStatistics(arr, 1) == -1;
                System.out.println(Arrays.toString(arr));
                System.out.println(orderStatistics(arr, 2));
                assert orderStatistics(arr, 2) == 0;
                System.out.println(Arrays.toString(arr));
                assert orderStatistics(arr, 3) == 2;
                assert orderStatistics(arr, 4) == 2;
                System.out.println(orderStatistics(arr, 5));
		assert orderStatistics(arr, 5) == 4;
                assert orderStatistics(arr, arr.length) == 100;
                //assert orderStatistics(arr, 15) == null;
                //assert orderStatistics(arr, 0) == null;
*/
        }
}
