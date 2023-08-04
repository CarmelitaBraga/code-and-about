public class MedianQuickSort {

	public static void sort(int[] array, int leftIndex, int rightIndex) {
		//int median = (rightIndex + leftIndex) / 2;
		if (leftIndex < rightIndex) {
			int idxPivot = partition(array, leftIndex, rightIndex);
			sort(array, leftIndex, idxPivot-1);
			sort(array, idxPivot+1, rightIndex);
		}
	}

	private static int partition(int[] array, int left, int right) {
		int median = (left + right) / 2;
		int idxPivot = medianSelection(array, left, right, median, 0, 0);
		swap(array, idxPivot, left);
		int i = left;
		for (int j = i + 1; j <= right; j++) {
			if (array[j] <= array[i]) {
				i++;
				swap(array, i, j);
			}
		}
		swap(array, i, left);
		return i;


	}

	private static int medianSelection(int[] array, int left, int right, int median, int cont, int last) {
		int i = left;
		int j = i+1;
		if (cont < median) {
			while (j <= right) {
				if (array[j] < array[i]) {
					if (last == -1 || array[j] > array[last]) {
						i = j;
						System.out.println("here");
					}
				}
				j++;
			}
			return medianSelection(array, left, right, median, ++cont, i);
		}
		return i;

/*
		int cont = 0;
		int i = left;
		int j = i + 1;
		int before = left;
		while (cont < median && j <= right) {
			if (array[j] < array[i]) {
				if (array[j] > array[before]) {
					i = j;
				}
			}
		}

*/	}

	private static void swap(int[] array, int i, int j) {
		int aux = array[i];
		array[i] = array[j];
		array[j] = aux;
	}

	public static void main(String[] args) {
		int[] arr = new int[] {78, 3, 41, -1, 2, 4, 10, 8, 11, 5, 7, 71, 99};
		System.out.println(medianSelection(arr, 0, 12, 6, 0, -1));
		assert medianSelection(arr, 0, 12, 6, 0, 0) == 7;
	}

}
