class ProductOfNumbers {
    private List<Integer> products;
    private int product;

    public ProductOfNumbers() 
    {
        products = new ArrayList<>();
        product = 1 ;
        
    }
    
    public void add(int num) 
    {
        if (num != 0)
        {
            product *= num ;
            products.add(product) ;
        }
        else
        {
            products.clear() ;
            product = 1 ;

        }
        
    }
    
    public int getProduct(int k) 
    {
        if (products.size() < k)
        {
            return 0 ;
        }
        else if (products.size() == k)
        {
            return product ;
        }
        else
        {
            return products.get(products.size() - 1) / products.get(products.size() - k - 1);
        }
        
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers obj = new ProductOfNumbers();
 * obj.add(num);
 * int param_2 = obj.getProduct(k);
 */