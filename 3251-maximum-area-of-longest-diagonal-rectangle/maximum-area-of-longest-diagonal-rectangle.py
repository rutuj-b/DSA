class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_area = max_diagonal = 0 
        for l , w in dimensions :
            area = l * w
            diagonal = l*l + w*w
            if diagonal > max_diagonal :
                max_area = area
                max_diagonal = diagonal
            elif diagonal == max_diagonal :
                max_area = max(area , max_area)
        return max_area