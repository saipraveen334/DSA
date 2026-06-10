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
    public void reorderList(ListNode head) {

        ListNode  slow = head;
        ListNode fast = head;

        while(fast!= null && fast.next != null)
        {
            slow = slow.next; 
            fast = fast.next.next;
        }

        //REVERSE THE SECOND CHAIN 

        ListNode second = slow.next;

        ListNode prev = null;

        slow.next = null;

        while( second != null)
        {
            ListNode nxt = second.next;
            second.next = prev;
            prev = second;
            second = nxt;
        }

        // USE TWO POINTERS TO REORDER LIST 
        ListNode first = head;
        ListNode sec = prev ;

        while(sec != null)
        {
            ListNode temp1 = first.next;
            ListNode temp2 = sec.next;

            first.next = sec;
            sec.next = temp1;

            first = temp1;
            sec = temp2;
        }
        
        
        
    }
}