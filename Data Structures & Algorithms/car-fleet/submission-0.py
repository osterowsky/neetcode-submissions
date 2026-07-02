class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            cars.append((position[i], time))
        
        cars.sort(key=lambda x: x[0])
        
        cur, fleet = cars[len(cars) - 1][1], 1
        for i in range(len(cars) -2, -1, -1):
            car_time = cars[i][1]
            if car_time > cur:
                fleet += 1
                cur = car_time
        
        return fleet