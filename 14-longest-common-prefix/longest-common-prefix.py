class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res  = ''
        for i in range(len(strs[0])):
            for s in strs:
                if i== len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
        # isme apan phla wala string lenge uske bas har string me jayege aur dekhege ki jo first string liye the uske i index aur abhi wali jo string hai uske i index me same char hai ki nahi agar vo same hua to res me add krege aur jaise hi i last postion me hai ya to abhi ke s ka ith index pe jo char hai vo phle li wali ke ith index wale se match nahi hua to bas return krdo res mtlb iske phle tak ke same tha res 