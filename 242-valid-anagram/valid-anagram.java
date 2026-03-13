class Solution {
    public boolean isAnagram(String s, String t) {

        // USING HASHMAP
        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> hm1 = new HashMap<>();
        HashMap<Character, Integer> hm2 = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            hm1.put(s.charAt(i), hm1.getOrDefault(s.charAt(i), 0) + 1);
            hm2.put(t.charAt(i), hm2.getOrDefault(t.charAt(i), 0) + 1);
        }

        return hm1.equals(hm2);
    }
    }

        //USING FREQUENCY ARRAY

//         if(s.length() != t.length())
//         {
//             return false;
//         }
        

//         int count[] = new int[26];

//         for(int i = 0 ; i < s.length() ; i++)
//         {
//             count[s.charAt(i) - 'a'] += 1;
//             count[t.charAt(i) - 'a'] -= 1;
//         }

//         for (int val : count)
//         {
//             if(val != 0)
//             {
//                 return false;
//             }
//         }
//         return true;

        
//     }
// }