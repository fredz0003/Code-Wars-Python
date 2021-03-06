import unittest
from RangeExtraction import solution
from RangeExtraction import solution2

class RangeExtractionTests(unittest.TestCase):
    def test(self):
        self.assertEqual(solution([-64, -63, -60, -59, -57, -55, -54, -51, -49, -47, -44, -41, -39, -36, -33, -32, -31, -30, -27, -26, -24, -22, -20, -19, -18, -15, -14, -12, -9, -7, -5]), '-64,-63,-60,-59,-57,-55,-54,-51,-49,-47,-44,-41,-39,-36,-33--30,-27,-26,-24,-22,-20--18,-15,-14,-12,-9,-7,-5')
        self.assertEqual(solution([-92, -90, -87, -84, -83, -80, -77, -75, -73, -72, -71, -68, -66, -64, -61, -58, -57]), '-92,-90,-87,-84,-83,-80,-77,-75,-73--71,-68,-66,-64,-61,-58,-57')
        self.assertEqual(solution([-51, -49, -47, -45, -44, -42, -39, -36, -35, -34, -31, -30, -28]), '-51,-49,-47,-45,-44,-42,-39,-36--34,-31,-30,-28')
        self.assertEqual(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '-6,-3-1,3-5,7-11,14,15,17-20')
        self.assertEqual(solution([-3,-2,-1,2,10,15,16,18,19,20]), '-3--1,2,10,15,16,18-20')
        self.assertEqual(solution([-95, -94, -93, -90, -89, -86, -83, -81, -80, -77, -75, -72, -71, -68, -67, -66, -64, -61, -59]), '-95--93,-90,-89,-86,-83,-81,-80,-77,-75,-72,-71,-68--66,-64,-61,-59')

    # def test2(self):
    #     #self.assertEqual(solution2([-64, -63, -60, -59, -57, -55, -54, -51, -49, -47, -44, -41, -39, -36, -33, -32, -31, -30, -27, -26, -24, -22, -20, -19, -18, -15, -14, -12, -9, -7, -5]), '-64,-63,-60,-59,-57,-55,-54,-51,-49,-47,-44,-41,-39,-36,-33--30,-27,-26,-24,-22,-20--18,-15,-14,-12,-9,-7,-5')
    #     self.assertEqual(solution2([-3,-2,-1,2,10,15,16,18,19,20]), '-3--1,2,10,15,16,18-20')