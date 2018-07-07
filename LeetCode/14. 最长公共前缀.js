// 编写一个函数来查找字符串数组中的最长公共前缀。

// 如果不存在公共前缀，返回空字符串 ""。

// 示例 1:

// 输入: ["flower","flow","flight"]
// 输出: "fl"
// 示例 2:

// 输入: ["dog","racecar","car"]
// 输出: ""
// 解释: 输入不存在公共前缀。
// 说明:

// 所有输入只包含小写字母 a-z 。


/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
  if (strs.length <= 0) {
    return "";
  }
  var result = strs[0];
  var temp = "";

  for (var i = 1; i < strs.length; i++) {
    //判断第一个字符是否相同，如果不同，则不用再比较
    if (result[0] !== strs[i][0]) {
      result = "";
      break;
    }
    //循环比较
    for (var j = 0; j < strs[i].length; j++) {
      if (result[j] == strs[i][j]) {
        temp += strs[i][j];
      }
    }
    result = temp;
    temp = "";
  }


  return result;
};