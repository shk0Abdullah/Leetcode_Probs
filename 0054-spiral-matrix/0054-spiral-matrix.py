class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # starting from the top list pop traverse the right most until you hit -1 index and
        # then traverse back to the top from left most elements you have traversed
        self.output = []
        self.matrix = matrix
        while self.matrix:
            try:
                self.traverse_from_top()
                self.traverse_right_most()
                self.traverse_from_bottom()
                self.traverse_left_most()
            except: 
                pass

          
        print (self.output)
        return self.output

    def traverse_right_most(self):
        for matric in self.matrix:
            self.output.append(matric.pop(-1))
    def traverse_left_most(self):
        for matric in self.matrix[-1::-1]:
            self.output.append(matric.pop(0))
    def traverse_from_top(self):
        ls = self.matrix.pop(0)
        self.output.extend(ls)
    def traverse_from_bottom(self):
        try:
            ls = self.matrix.pop()
        except:
            return -1
        self.output.extend(ls[-1::-1])


