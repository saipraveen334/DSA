class Node {
    int val;
    int key;
    Node prev;
    Node next;

    Node(int key , int val)
    {
        this.key = key;
        this.val = val;
    }
}

class LRUCache {
    private int cap;
    private Map<Integer , Node> cache ;
    private Node left;
    private Node right;


    public LRUCache(int capacity) {
        this.cap = capacity;

        this.cache = new HashMap<>();
        this.left = new Node(0 , 0);
        this.right = new Node(0 , 0);

        this.left.next = this.right ;
        this.right.prev = this.left ;


    }
    private void remove(Node node)
    {
        Node prev = node.prev;
        Node nxt = node.next;

        prev.next = nxt;
        nxt.prev = prev;
    }

    private void insert(Node node)
    {
        Node prev = this.right.prev;
        Node nxt = this.right;

        prev.next = node;
        nxt.prev = node;
        node.next = nxt;
        node.prev = prev;
    }
    public int get(int key) {

        if (cache.containsKey(key))
        {
            Node node = cache.get(key);
            remove(node);
            insert(node);
            return node.val;
        }
        return -1;

        
    }
    
    public void put(int key, int value) {
        if (cache.containsKey(key))
        {
            remove(cache.get(key));
        }
        Node node = new Node(key , value);
        cache.put(key , node);
        insert(node);
        if (cache.size() > cap)
        {
            Node lru = this.left.next;
            remove(lru);
            cache.remove(lru.key);
        }
        
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */