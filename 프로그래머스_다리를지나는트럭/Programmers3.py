class Prgrammers:
    def __init__(self):
        pass

    def solution(bridge_length, weight, truck_weights):
        answer = 0

        queue = []

        sum = 0
        idx = 0

        while True:
            if idx == len(truck_weights):
                break
            if len(queue) == bridge_length:
                sum -= queue.pop(0)

            if idx != len(truck_weights) and sum+truck_weights[idx] <= weight:
                queue.append(truck_weights[idx])
                sum += truck_weights[idx]
                idx += 1
            else:
                queue.append(0)

            answer += 1

        answer += bridge_length

        return answer
