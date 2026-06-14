/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {

        ListNode dummy = new ListNode( 0 , head);
        ListNode lprev = dummy;
        ListNode cur = head;

        for( int i = 0 ; i < left - 1 ; i++)
        {
            lprev = lprev.next;
            cur = cur.next;
        }

        ListNode prev = null;

        for(int j = 0 ; j < right - left + 1 ; j++)
        {
            ListNode temp = cur.next;
            cur.next = prev;
            prev = cur;
            cur = temp;
        }

        lprev.next.next = cur;
        lprev.next = prev; 

        return dummy.next;
        
        
    }
}