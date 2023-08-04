import java.util.*;

public class DoisMaioresGastos {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] sNums = sc.nextLine().split(" ");
		int tamS = sNums.length;
		int[] nums = new int[tamS];

		int maior1 = Integer.MIN_VALUE;
		int maior2 = Integer.MIN_VALUE;
		int idx1 = 0;
		int idx2;

		for (int i = 0; i < tamS; i++) {
			nums[i] = Integer.parseInt(sNums[i]);
			if (nums[i] > maior1) {
				maior1 = nums[i];
				idx1 = i;
			} else if (nums[i] > maior2 && nums[i] <= maior1); {
				maior2 = nums[i];
				idx2 = i;
			}
		}
		System.out.println(maior1 + maior2);
	}
}
