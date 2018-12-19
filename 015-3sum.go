package main

import (
	"fmt"
	"sort"
	"strconv"
)

func threeSum(nums []int) [][]int {
	sort.Ints(nums)
	var items [][]int
	var i,j,k,s int
	mpa1 := make(map[string]bool)
	for i = 0; i < len(nums); i++ {
		j=i+1
		k=len(nums)-1
		for j < k {
			s = nums[i] + nums[j] + nums[k]
			if s == 0 {
				tmp := []int{nums[i], nums[j], nums[k]}
				t := strconv.Itoa(nums[i]) + "_" + strconv.Itoa(nums[j]) + "_" + strconv.Itoa(nums[k])
				if _, ok := mpa1[t]; ok {
					continue
				}
				mpa1[t] = true
				fmt.Println(tmp)
				items = append(items, tmp)
				break
			} else if s < 0 {
				j += 1
			} else {
				k -= 1
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
			for m < len(nums) - 1 {
				if nums[m+1] == v {
					m += 1
				} else {
					return m, true
				}
			}
			return m, true
		}
	}
	return l, false
}

func main() {
	nums := []int{-1, 0, 1, 2, -1, -4}
	fmt.Println(threeSum(nums))
	nums = []int{0,0,0}
	fmt.Println(threeSum(nums))
}
