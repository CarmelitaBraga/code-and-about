import java.util.*;

public class QuickSelect {

	public static int quickSelect(int[] array, int k) {
		return array[select(array, k-1, 0, array.length-1)];
	}
	
	private static int select(int[] array, int k, int left, int right) {
		int i = partition(array, left, right);
		int result = i;
		if (left <= right && i != k) {
			if (i > k) {
				result = select(array, k, left, i-1);
			} else {
				result = select(array, k, i+1, right);
			}
		}
		return result;
	}
	
	private static int partition(int[] array, int left, int right) {
		int i = left;
		int pivot = array[i];
		for (int j = i+1; j <= right; j++) {
			if (array[j] <= pivot) {
				i++;
				swap(array, i, j);
			}
		}
		swap(array, left, i);
		return i;
	}

	private static void swap(int[] array, int i, int j) {
                int aux = array[i];
                array[i] = array[j];
                array[j] = aux;
        }

	public static void main(String[] args) {
                int[] arr = {33, 15, 10, 11, 8, 11}; 
		int[] arr2 = {5, 9, -3, 6, 0, 10, 7, 22, 21, 64, 23, 10, 25, 65, 100, 41, 8, 2, 1};
                System.out.println(Arrays.toString(arr2));
                int k = 1;
                int element = quickSelect(arr2, k); // segundo elemento
                System.out.println(Arrays.toString(arr2));
		System.out.println("Elemento: "+element);
                System.out.println(arr2.length);

		assert quickSelect(arr2, 1) == -3;
		assert quickSelect(arr2, 2) == 0;
		assert quickSelect(arr2, 3) == 1;
		assert quickSelect(arr2, 18) == 65;
		assert quickSelect(arr2, arr2.length) == 100;
		assert quickSelect(arr, 1) == 8;
		assert quickSelect(arr, 3) == 11;
		assert quickSelect(arr, 4) == 11;
		assert quickSelect(arr, 6) == 33;
		assert quickSelect(new int[] {3, 0}, 1) == 0;
		assert quickSelect(new int[] {5}, 1) == 5;

	}
}
