class Programmers1:
    def __init__(self):
        pass

    def solution(self, progresses, speeds):
        answer = []

        remain = []
        for pro, spe in zip(progresses, speeds):
            if (100-pro)%spe == 0 :
                remain.append(int((100-pro)/spe))
            else :
                remain.append(int((100-pro)/spe) +1)

        stack = []

        target = 0
        for re in remain :
            if len(stack) ==0 :
                stack.append(re)
                target = re

                continue
            if re <= stack[0] :
                stack.append(re)
            else :
                answer.append(len(stack))
                while len(stack) :
                    stack.pop()
                stack.append(re)
                target = re

        if len(stack) != 0 :
            answer.append(len(stack))

        print(answer)

        return answer


