public class OrderStatisticsSelection {
	
	public static int getOrderStatistics(int[] array, int k) {
                return array[statisticsSelection(array, k, 0, -1)];
        }

        private static int statisticsSelection(int[] array, int k, int cont, int lastIdx) {
                if (cont < k) {
                        lastIdx = selection(array, lastIdx);
                        return statisticsSelection(array, k, ++cont, lastIdx);
                }
                return lastIdx;
        }


        private static int selection(int[] array, int lastIdx) {
                int i = 0;
                for (int j = 1; j < array.length; j++) {
			if (array[j] < array[i]) {
				if (lastIdx < 0) {
					i = j;
				} else if (array[j] > array[lastIdx]) {
					i = j;
				} else if (array[j] == array[lastIdx] && j != lastIdx) {
					i = j;
				}
			}
		}
		return i;
        }

	public static void main(String[] args) {
		System.out.println(getOrderStatistics(new int[] {7, 3, 5, -2, 4, 0, 17, 29, 4}, 3));
		assert getOrderStatistics(new int[] {7, 3, 5, -2, 4, 0, 17, 29, 4}, 3) == 3;
		assert getOrderStatistics(new int[] {9, 0, 5, 7, 2, -1}, 2) == 0;
		assert getOrderStatistics(new int[] {2, -1}, 1) == -1;
		assert getOrderStatistics(new int[] {7, 3, 5, -2, 4, 0, 17, 29, 4}, 1) == -2;
		assert getOrderStatistics(new int[] {7, 3, 5, -2, 4, 0, 17, 29, 4}, 2) == 0;
		assert getOrderStatistics(new int[] {7, 3, 5, -2, 4, 0, 17, 29, 4}, 4) == 4;
		assert getOrderStatistics(new int[] {7, 3, 5, -2, 4, 0, 17, 29, 4}, 5) == 4;

	}
}
