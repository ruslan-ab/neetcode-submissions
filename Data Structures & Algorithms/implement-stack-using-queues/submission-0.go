type MyStack struct {
	head *ListNode
}

type ListNode struct {
	val int
	next *ListNode
}

func Constructor() MyStack {
	return MyStack{}
}

func (this *MyStack) Push(x int) {
	n := ListNode{
		val: x,
	}
	if this.head != nil {
		n.next = this.head
	}
	this.head = &n
}

func (this *MyStack) Pop() int {
	v := this.head.val
	if this.head.next != nil {
		this.head = this.head.next
	}
	return v
}

func (this *MyStack) Top() int {
	return this.head.val
}

func (this *MyStack) Empty() bool {
	if this.head == nil {
		return true
	}
	return false
}


/**
 * Your MyStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param2 := obj.Pop();
 * param3 := obj.Top();
 * param4 := obj.Empty();
 */
