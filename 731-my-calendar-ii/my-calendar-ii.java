class MyCalendarTwo {
    private List<int[]> overlap ;
    private List<int[]> nonoverlap ;

    public MyCalendarTwo() {
        overlap = new ArrayList<>();
        nonoverlap = new ArrayList<>();
    }
    
    public boolean book(int startTime, int endTime) {

        for (int[] i: overlap)
        {
            int s = i[0] ;
            int e = i[1] ;

            if (startTime < e && endTime > s)
            {
                return false;
            }

        }
        for(int[] i: nonoverlap)
        {
            int s = i[0];
            int e = i[1];

            if(startTime < e && endTime > s)
            {
                overlap.add(new int[]{ Math.max(startTime , s) , Math.min(endTime , e)}) ;
            }
            
        }
        nonoverlap.add(new int[]{ startTime , endTime}) ;
        return true ;

        
    }
}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo obj = new MyCalendarTwo();
 * boolean param_1 = obj.book(startTime,endTime);
 */