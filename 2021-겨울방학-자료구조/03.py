"""
3주차: 자료구조-알고리즘-시간복잡도
- 자료구조 및 알고리즘의 개념
- GCD(Greatest Common Divisor) 알고리즘의 세 방법
- 재귀함수(Recursive Function)
- 가상 컴퓨터, 가상 언어, 가상 코드
- 시간복잡도 및 Big-O
"""

if __name__ == "__main__":
    import unittest

    
    def gcd_sub(first_num: int, second_num: int) -> int:
        while (first_num != 0) and (second_num != 0):
            if first_num > second_num:
                first_num -= second_num
                
            else:
                second_num -= first_num
                
        return first_num + second_num
    
    
    def gcd_mod(first_num: int, second_num: int) -> int:
        while (first_num != 0) and (second_num != 0):
            if first_num > second_num:
                first_num %= second_num
                
            else:
                second_num %= first_num
        
        return first_num + second_num
    
    
    def gcd_rec(first_num: int, second_num: int) -> int:
        if (first_num == 0) or (second_num == 0):
            
            return first_num + second_num
        
        elif first_num > second_num:
            """
            아래와 같이 재귀함수가 실제로 실행되는 부분 또한 `return` 문으로 반환을 해야 한다.
            다시 말해 실제 마지막에 실행되는 결괏값의 조건인 `(first_num == 0) or (second_num == 0)`에서만 `return`을 사용하는 게 아니라,
            재귀함수로 다시 실행될 `gcd_rec()` 함수 실행 부분도 `return`을 통해 실행시켜야 한다.
            그렇지 않으면 아무 것도 반환하지 않게 되기 때문에 실제 반환 결과는 `None`이 된다.
            """
            
            return gcd_rec(first_num%second_num, second_num)
        
        else:
            
            return gcd_rec(first_num, second_num%first_num)
        
    
    def prefix_sum_first(X: list, n: int) -> list[int]:
        S: list[int] = []
        
        for i in range(n):
            S.append(0)
            for j in range(i+1):
                S[i] += X[j]
                
        return S
    
    
    def prefix_sum_second(X: list, n: int) -> list[int]:
        S: list[int] = []
        
        S.append(X[0])
        for i in range(1, n):
            S.append(S[i-1] + X[i])
            
        return S   
    
    
    def sum(A: list[int], n: int) -> list[list[int]]:
        B: list[list[int]] = [ [0] * n for _ in range(n) ]
        
        for i in range(n):
            num_sum: int = 0
            for j in range(i, n):
                num_sum += A[j]
                B[i][j], B[j][i] = num_sum, num_sum
                
        return B
    
    
    class TestGCDMethods(unittest.TestCase):
        def setUp(self) -> None:
            self._test_cases: list[tuple[int]] = [
                (16, 2, 2), (18, 32, 2), (24, 4, 4)
            ]
        
        
        def test_gcd_sub(self) -> None:
            for test_case in self._test_cases:
                first_num: int = test_case[0]
                second_num: int = test_case[1]
                result: int = test_case[2]
                
                self.assertEqual(gcd_sub(first_num, second_num), result)
        
        
        def test_gcd_mod(self) -> None:
            for test_case in self._test_cases:
                first_num: int = test_case[0]
                second_num: int = test_case[1]
                result: int = test_case[2]
                
                self.assertEqual(gcd_mod(first_num, second_num), result)


        def test_gcd_rec(self) -> None:
            for test_case in self._test_cases:
                first_num: int = test_case[0]
                second_num: int = test_case[1]
                result: int = test_case[2]
                
                self.assertEqual(gcd_rec(first_num, second_num), result)            
    
    
    class TestPrefixSum(unittest.TestCase):
        def setUp(self) -> None:
            self._test_case: dict[str, int | list[int]] = {
                "n": 4,
                "X": [ 36, -436, -652, -487 ],
                "result": [ 36, -400, -1052, -1539 ]
            }
                
                
        def test_prefix_sum_first(self) -> None:
            n: int = self._test_case["n"]
            X: list[int] = self._test_case["X"]
            result: list[int] = self._test_case["result"]
                        
            self.assertEqual(prefix_sum_first(X=X, n=n), result)
        
        
        def test_prefix_sum_second(self) -> None:
            n: int = self._test_case["n"]
            X: list[int] = self._test_case["X"]
            result: list[int] = self._test_case["result"]
            
            self.assertEqual(prefix_sum_second(X=X, n=n), result)
    
    
    class TestSum(unittest.TestCase):
        def setUp(self) -> None:
            self._test_case: dict[
                str, int | list[int] | list[list[int]]
            ] = {
                "n": 8,
                "A": [41, 34, 44, 56, 89, 23, 60, 27],
                "result": [
                    [41, 75, 119, 175, 264, 287, 347, 374],
                    [75, 34, 78, 134, 223, 246, 306, 333],
                    [119, 78, 44, 100, 189, 212, 272, 299],
                    [175, 134, 100, 56, 145, 168, 228, 255],
                    [264, 223, 189, 145, 89, 112, 172, 199],
                    [287, 246, 212, 168, 112, 23, 83, 110],
                    [347, 306, 272, 228, 172, 83, 60, 87],
                    [374, 333, 299, 255, 199, 110, 87, 27]
                ]
            }
        
        
        def test_sum(self) -> None:
            n: int = self._test_case["n"]
            A: list[int] = self._test_case["A"]
            result: list[list[int]] = self._test_case["result"]
            
            self.assertEqual(sum(A=A, n=n), result)
    
    
    unittest.main()
                
    