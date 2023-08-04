import java.util.*;

public class EstatisticaDeOrdem {

	public static int orderStatistics(int[] array, int k) {
		return array[ordem(array, k, 0, -1, 0, array.length-1)];
	}

	public static int ordem(int[] array, int k, int cont, int last, int left, int right) {

		if (right > left && cont < k) {
			if (last == left) {
				left += 1;
			} else {
				while (array[left] > array[left+1]) {
					left += 1;
				}
			}

			int i = left;
				for (int o = left; o <= right; o++) {
				if (array[o] > array[left]) {
					i = o;
				}
			}

			for (int j = left; j <= right; j++) {
				//int i = left;
				if (array[j] < array[i]) {
					if (last == -1) {
						i = j;
					} else if (array[j] > array[last]) {
						i = j;
					} /*else if (array[j] == array[last] && j != last) {
						i = j;
					}*/
				}
			}

			/*if (last == left) {
                                left += 1;
                        }*/
			//last = i;
			return ordem(array, k, cont+1, i, left, right);
		}
		return last;
	}


	public static void main(String[] args) {

                int[] arr = new int[] {4, 12, 0, 2, 54, -1, 100, 3};
                System.out.println(Arrays.toString(arr));

                System.out.println(orderStatistics(arr, 1));
                System.out.println(orderStatistics(arr, 2));
                System.out.println(orderStatistics(arr, 3));
                System.out.println(orderStatistics(arr, 4));
                System.out.println(orderStatistics(arr, 5));
                System.out.println(orderStatistics(arr, 6));
                System.out.println(orderStatistics(arr, 7));
                System.out.println(orderStatistics(arr, 8));
                assert orderStatistics(arr, 1) == -1;
                assert orderStatistics(arr, 2) == 0;
                assert orderStatistics(arr, 3) == 2;
                assert orderStatistics(arr, 4) == 2;
                System.out.println(orderStatistics(arr, 5));

                assert orderStatistics(arr, 5) == 4;
                System.out.println(orderStatistics(arr, 6));
                assert orderStatistics(arr, 6) == 12;
                assert orderStatistics(arr, 7) == 54;
                assert orderStatistics(arr, arr.length) == 100;
                System.out.println(Arrays.toString(arr));
	}

}
