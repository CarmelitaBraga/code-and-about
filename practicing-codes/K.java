public class K {

	public static int Kminor(int[] array, int k) {
		int cont = 1;
		int major = array[0];
		int minor = array[0];
		for (int i = 0; i < array.length; i++) {
			if (array[i] > major) {
				major = array[i];
			}
			if (array[i] < minor) {
				minor = array[i];
			}
		}

		if (k == array.length) return major;

		int auxm = minor;
		while (k > cont) {
			int auxM = major;
			for (int i = 0; i < array.length; i++) {
				if (array[i] < auxM && array[i] > minor) {
					auxm = array[i];
					auxM = array[i];
				}
			}
			minor = auxm;
			cont++;
		}
		return minor;
	}

	public static void main(String[] args) {
		int[] arr = new int[] {4, 101, 12, 0, 2, 54, -1, 100, 3};
		assert Kminor(arr, 1) == -1;
		System.out.println(Kminor(arr, 2));
		assert Kminor(arr, 2) == 0;
		assert Kminor(arr, 3) == 2;
		assert Kminor(arr, 4) == 3;
		assert Kminor(arr, 5) == 4;
		assert Kminor(arr, 6) == 12;
		assert Kminor(arr, 7) == 54;
		assert Kminor(arr, 8) == 100;
		assert Kminor(arr, 9) == 101;

		int[] arr1 = new int[] {7, -1, 2, 15, 7};
		assert Kminor(arr1, 2) == 2;
		
	}

}
