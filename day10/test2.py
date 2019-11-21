#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风

# 本模块的功能:<>


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        leng = len(s)
        for i in range(leng):
            for j in range(i+1,leng):
                if s[i] == s[j]:
                    if res < j-i+1:
                        res = j-i+1
                    break
            else:
                print("没被break")
        return res
s = Solution()
print(s.lengthOfLongestSubstring("dvdf"))