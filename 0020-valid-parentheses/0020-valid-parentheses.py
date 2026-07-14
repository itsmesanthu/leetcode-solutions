class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in s:
            if i in "({[":
                st.append(i)
            else:
                if not st:
                    return False
                top=st.pop()
                if i==")"and top!="(":
                    return False
                if i=="]" and top!="[":
                    return False
                if i=="}"and top!="{":
                    return False
        return not st