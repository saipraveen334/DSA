class Solution {

    public String decodeString(String s) {

        Stack<String> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {

            char ch = s.charAt(i);

            if (ch != ']') {

                stack.push(String.valueOf(ch));

            } else {

                String st = "";

                while (!stack.isEmpty() && !stack.peek().equals("[")) {
                    st = stack.pop() + st;
                }

                stack.pop();

                String k = "";

                while (!stack.isEmpty() &&
                       Character.isDigit(stack.peek().charAt(0))) {

                    k = stack.pop() + k;
                }

                int repeat = Integer.parseInt(k);

                StringBuilder res = new StringBuilder();

                for (int j = 0; j < repeat; j++) {
                    res.append(st);
                }

                stack.push(res.toString());
            }
        }

        StringBuilder ans = new StringBuilder();

        for (String str : stack) {
            ans.append(str);
        }

        return ans.toString();
    }
}