import java.util.*;
public class FloorBinarySearch {

        public static Integer floor(Integer[] array, Integer x) {
                quicksort(array, 0, array.length-1);
                if (x < array[0]) { // (indexOf(array, 0, array.length-1, x) == -1) {
                        return null;
                } else {
                        return array[indexOf(array, 0, array.length - 1, x)];
                }
        }

        private static int indexOf(Integer[] array, int left, int right, int x) {
                int middle = (left + right) / 2;
                int result = middle;//middle;//-1;
                if (left <= right) {
                        if (array[middle] == x){// || middle == left || middle == right) {
                                result = middle;
                        
			/*} else if (array[middle-1] < x && array[middle+1] > x) {
				result = middle;
			*/
			} else if (array[middle] > x) {
                                result = indexOf(array, left, middle-1, x);
                        } else if (array[middle] < x) {
                                result = indexOf(array, middle+1, right, x);
                        } else if (array[middle-1] < x && array[middle+1] > x) {
                                result = middle;
			}
                }

                return result;
        }

        private static void quicksort(Integer[] array, int left, int right) {
                if (left < right) {
                        int idxPivot = partition(array, left, right);
                        quicksort(array, left, idxPivot - 1);
                        quicksort(array, idxPivot + 1, right);
                }
        }

        private static int partition(Integer[] array, int left, int right) {
                int i = left;
                int pivot = array[left];
                for (int j = i+1; j <= right; j++) {
                        if (array[j] <= pivot) {
                                i++;
                                swap(array, i, j);
                        }
                }
                swap(array, i, left);
                return i;
        }

        private static void swap(Integer[] array, int i, int j) {
                int aux = array[i];
                array[i] = array[j];
                array[j] = aux;
        }

        public static void main(String[] args) {
                Integer[] arr = new Integer[] {5, 61, 10, 12, -3, 11, 2, 7};
                Integer[] arrayOrdenado = new Integer[] {-3, 2, 5, 7, 10, 11, 12, 61};
                System.out.println(Arrays.toString(arr));
                quicksort(arr, 0, arr.length-1);
                System.out.println(Arrays.toString(arr));

                assert floor(arr, 7) == 7;
                assert floor(arr, -3) == -3;

		assert floor(new Integer[] {-2, 113, 17, 59, 10, 0}, 10) == 10;
		assert floor(new Integer[] {-2, 3, 0}, -10) == null;
		System.out.println(floor(new Integer[] {-2, 3, 0}, 3));
		System.out.println(floor(new Integer[] {-2, 3}, 3));
		System.out.println(floor(new Integer[] {1, 2, 4, 5, 6}, 3));
		//
		assert floor(new Integer[] {-2, 3, 0}, 3) == 3;
		assert floor(new Integer[] {-2, 3}, 3) == 3;
		assert floor(new Integer[] {1, 2, 4, 5, 6}, 3) == 2;
		assert floor(new Integer[] {1, 2, 4, 5, 6}, 6) == 6;
		assert floor(new Integer[] {1, 2, 4, 5, 6}, 7) == 6;
		assert floor(new Integer[] {0, 2, 4, 5, 6}, 1) == 0;
		assert floor(new Integer[] {1, 2, 4, 5, 6}, 0) == null;
		assert floor(new Integer[] {-2, 3, 0, 11, 12}, 10) == 3;
		assert floor(new Integer[] {66, 39, 31, 20, 25, 56}, 57) == 56;
		assert floor(new Integer[] {-2, 3, 0}, -1) == -2;
		assert floor(new Integer[] {77}, 78) == 77;
		assert floor(new Integer[] {77}, 76) == null;
		assert floor(new Integer[] {77}, 77) == 77;
		assert floor(new Integer[] {77, 0}, 70) == 0;


        }
}
