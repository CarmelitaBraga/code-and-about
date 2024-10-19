package main

import "fmt"

type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func dfs(root *TreeNode) int {
	if root != nil {
		leftDepth := dfs(root.Left)
		rightDepth := dfs(root.Right)
		return 1 + max(leftDepth, rightDepth)
	} else {
		return 0
	}
}

func main() {
	root := &TreeNode{Val:10}
	root.Left = &TreeNode{Val:4}
	root.Left.Left = &TreeNode{Val:1}
	root.Right = &TreeNode{Val:12}
	root.Right.Right = &TreeNode{Val: 15}
	root.Right.Left = &TreeNode{Val:11}

	fmt.Println("Maximum Depth is:", dfs(root))

}