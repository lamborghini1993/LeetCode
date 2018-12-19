package main

import (
	"fmt"
	"sort"
	"strconv"
)

func threeSum(nums []int) [][]int {
	sort.Ints(nums)
	var items [][]int
	mpa1 := make(map[string]bool)
	fmt.Println(nums)
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			v := 0 - nums[i] - nums[j]
			k, b := findNum(nums, v)
			if b && j < k {
				tmp := []int{nums[i], nums[j], nums[k]}
				s := strconv.Itoa(nums[i]) + "_" + strconv.Itoa(nums[j]) + "_" + strconv.Itoa(nums[k])
				if _, ok := mpa1[s]; ok {
					continue
				}
				mpa1[s] = true
				fmt.Println(tmp)
				items = append(items, tmp)
			}
		}
	}
	return items
}

func findNum(nums []int, v int) (int, bool) {
	l := 0
	r := len(nums) - 1
	b := false
	if nums[0] > v || nums[r] < v {
		return l, b
	}
	var m int
	for l <= r {
		m = (l + r) / 2
		if nums[m] < v {
			l = m + 1
		} else if nums[m] > v {
			r = m - 1
		} else {
			return m, true
		}
	}
	return l, false
}

func main() {
	nums := []int{-1, 0, 1, 2, -1, -4}
	threeSum(nums)
	nums = []int{0,0,0}
	threeSum(nums)
}
