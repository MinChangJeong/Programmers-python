class Programmers2:
    def __init__(self):
        pass

    def solution(self, numbers, target):
        answer = 0;

        idx = 0
        sum = 0
        answer = self.DFS(numbers, idx, sum, target)

        print(answer)
        return answer;

    def DFS(self, numbers, idx, sum, target ):
        if idx == len(numbers) :
            if sum == target :
                return 1
            else : return 0

        else:
            return self.DFS(numbers, idx+1, sum+numbers[idx], target) + self.DFS(numbers, idx+1, sum-numbers[idx], target)

programmers = Programmers2()

numbers = [1,1,1,1,1]
target = 3

programmers.solution(numbers, target)