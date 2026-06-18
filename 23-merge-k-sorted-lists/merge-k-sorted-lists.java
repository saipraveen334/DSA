class Solution
{
    public ListNode mergeKLists(ListNode[] lists)
    {
        if (lists == null || lists.length == 0)
        {
            return null;
        }

        List<ListNode> listsCopy = new ArrayList<>(Arrays.asList(lists));

        while (listsCopy.size() > 1)
        {
            List<ListNode> mergedList = new ArrayList<>();

            for (int i = 0; i < listsCopy.size(); i += 2)
            {
                ListNode l1 = listsCopy.get(i);
                ListNode l2 = (i + 1 < listsCopy.size()) ? listsCopy.get(i + 1) : null;

                mergedList.add(mergeList(l1, l2));
            }
            listsCopy = mergedList;
        }
        return listsCopy.get(0);
    }

    private ListNode mergeList(ListNode l1, ListNode l2)
    {
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;

        while (l1 != null && l2 != null)
        {
            if (l1.val < l2.val)
            {
                cur.next = l1;
                l1 = l1.next;
            }
            else
            {
                cur.next = l2;
                l2 = l2.next;
            }
            cur = cur.next;
        }

        if (l1 != null)
        {
            cur.next = l1;
        }
        if (l2 != null)
        {
            cur.next = l2;
        }

        return dummy.next;
    }
}