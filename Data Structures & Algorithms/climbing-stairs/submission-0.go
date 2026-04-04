var cache map[int]int

func climbStairs(n int) int {
	cache = make(map[int]int)
	for i:=0; i<n; i++ {
		cache[i] = -1
	}

	return dfs(0, n, cache)
}

func dfs(i int, n int, cache map[int]int) int {
	if i>=n {
		if i==n {
			return 1
		}
		return 0
	}
	if cv, ok := cache[i]; ok && cv != -1 {
		return cv
	}
	res := dfs(i+1, n, cache) + dfs(i+2, n, cache)
	cache[i] = res
	return res
}
