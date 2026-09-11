class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []

        for dir in path.split('/'):
            if dir == '..': 
               if res: res.pop()
            elif dir == '' or dir == '.': continue
            else: res.append(dir)

        return '/' + '/'.join(res)