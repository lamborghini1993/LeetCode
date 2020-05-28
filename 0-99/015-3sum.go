package main

import (
	"fmt"
	"sort"
)

func threeSum(nums []int) [][]int {
	sort.Ints(nums)
	var items [][]int
	var i,j,k,s int
	for i = 0; i < len(nums); i++ {
		if i != 0 && nums[i] <= nums[i-1] {
			continue	// 去重相同的
		}
		j = i + 1
		k = len(nums) - 1
		for j < k {
			s = nums[i] + nums[j] + nums[k]
			if s == 0 {
				tmp := []int{nums[i], nums[j], nums[k]}
				items = append(items, tmp)
				j += 1
				k -= 1
				for j < k && nums[j] == nums[j-1] {	
					j += 1	 // 去重相同的
				}
				for j < k && nums[k] == nums[k+1] {	
					k -= 1	// 去重相同的
				}
			} else if s < 0 {
				j += 1
			} else {
				k -= 1
			}
		}
	}
	return items
}

func main() {
	nums := []int{-1, 0, 1, 2, -1, -4}
	fmt.Println(threeSum(nums))
	nums = []int{0,0,0}
	fmt.Println(threeSum(nums))
}
