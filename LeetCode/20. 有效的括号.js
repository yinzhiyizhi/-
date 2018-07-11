// 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

// 有效字符串需满足：

// 左括号必须用相同类型的右括号闭合。
// 左括号必须以正确的顺序闭合。
// 注意空字符串可被认为是有效字符串。

// 示例 1:

// 输入: "()"
// 输出: true
// 示例 2:

// 输入: "()[]{}"
// 输出: true
// 示例 3:

// 输入: "(]"
// 输出: false
// 示例 4:

// 输入: "([)]"
// 输出: false
// 示例 5:

// 输入: "{[]}"
// 输出: true


/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  let map = {
    '(': ')',
    '[': ']',
    '{': '}'
  };
  let arr = [];
  for (let i = 0; i < s.length; i++) {
    if (i === 0) {
      //s[0]=([{   map[s[0]]=)]}   判断是否为([{,不是则返回false   
      if (!map[s[0]]) return false;
      arr.push(s[0]);
      continue;
    }
    if (map[arr[arr.length - 1]] === s[i]) {
      arr.pop();
      continue;
    }
    if (!map[s[i]]) return false;
    arr.push(s[i]);
  }
  return arr.length === 0;
};