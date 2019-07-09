package com.boulos.temp;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
	
	public static boolean hasSumTo(List<Integer> nums, Integer k) {
		if (nums.size() < 2) {
			return false;
		}
		
		List<Integer> numsCopy = new ArrayList<>(nums);
		// Sort nums, then narrow down whatever sum exists by iterating
		// from both ends
		numsCopy.sort(null);
		int i = 0, j = numsCopy.size() - 1;
		
		while (i != j) {
			if (numsCopy.get(i) + numsCopy.get(j) == k) {
				return true;
			}
			else if (numsCopy.get(i) + numsCopy.get(j) < k) {
				i++;
			}
			else {
				j--;
			}
		}

		return false;
	}
	
	public static void main(String[] args) throws Exception {
		assert(hasSumTo(Arrays.asList(1, 2, 3), 5));
		assert(!hasSumTo(Arrays.asList(1, 2, 3), 10));
		assert(!hasSumTo(Arrays.asList(1, 3, 4, 6), 8));
		assert(!hasSumTo(Arrays.asList(2, 1, 2), 5));
	}
}
