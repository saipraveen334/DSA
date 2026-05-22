class FreqStack {

    HashMap<Integer , Integer> cnt;
    HashMap<Integer , Stack<Integer>> stack;
    int maxCnt;

    public FreqStack() {
        cnt = new HashMap<>();
        stack = new HashMap<>();
        maxCnt = 0;

        
    }
    
    public void push(int val) {

        int valCnt = 1 + cnt.getOrDefault(val,0);
        cnt.put(val , valCnt);
        
        if (valCnt > maxCnt)
        {
            maxCnt = valCnt;
        }
        stack.putIfAbsent(valCnt , new Stack<>());
        stack.get(valCnt).push(val);
        
    }
    
    public int pop() {
        int res = stack.get(maxCnt).pop();

        cnt.put(res , cnt.get(res) - 1);
        if(stack.get(maxCnt).isEmpty())
        {
            maxCnt -= 1;
        }

        return res;

        
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack obj = new FreqStack();
 * obj.push(val);
 * int param_2 = obj.pop();
 */