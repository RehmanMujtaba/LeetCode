class Solution {
public:
    bool isValid(string s) {
        std::stack <char> stack;

        for (auto chr : s) {
            if (chr == '(') {
                stack.push('(');
            } else if (chr == '{') {
                stack.push('{');
            } else if (chr == '[') {
                stack.push('[');
            }
            if (chr == ')' ) {
               if (stack.size() != 0 && stack.top()=='(') {stack.pop();}
               else {return false;}
            } else if (chr == '}'  ) {
                if (stack.size() != 0 && stack.top()=='{') {stack.pop();}
                else {return false;}
            } else if (chr == ']'  ) {
                if (stack.size() != 0 && stack.top() == '[' ){stack.pop();}
                else {return false;}
            }
        }
        if (stack.size() == 0) return true;
        return false;
    }
};