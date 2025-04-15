import numpy as np

class Quadratic:
    def __init__(self, Q: np.ndarray, q: np.ndarray):
        assert Q.shape[0] == Q.shape[1], "Q must be a square matrix"
        assert Q.shape[0] == q.shape[0], "Q and q must have the same number of rows"
        self.Q = Q
        self.q = q
        self.n = Q.shape[0]

    def function(self, x: np.ndarray) -> float:
        return 0.5 * (x.T @ self.Q @ x) + self.q.T @ x
    
    def gradient(self, x: np.ndarray) -> np.ndarray:
        return self.Q @ x + self.q
    
    def hessian(self, x: np.ndarray) -> np.ndarray:
        return self.Q

class Quartic:
    def __init__(self, Q: np.ndarray, sigma: float = 1e-4):
        assert Q.shape[0] == Q.shape[1], "Q must be a square matrix"
        self.Q = Q
        self.sigma = sigma
        self.n = Q.shape[0]
        self.I = np.eye(self.n)

    def function(self, x: np.ndarray) -> float:        
        return 0.5 * (x.T @ x) + (self.sigma / 4) * (x.T @ self.Q @ x)**2

    def gradient(self, x: np.ndarray) -> np.ndarray:
        return x + self.sigma * (x.T @ self.Q @ x) * (self.Q @ x)
    
    def hessian(self, x: np.ndarray) -> np.ndarray:
        x = x.reshape(-1, 1)
        return self.I + self.sigma * (2 * self.Q @ x @ x.T + x.T @ self.Q @ x) @ self.Q
    

class Rosenbrock2D:
    def function(self, x: np.ndarray) -> float:
        return (1 - x[0])**2 + 100 * (x[1] - x[0]**2)**2
    
    def gradient(self, x: np.ndarray) -> np.ndarray:
        grad = np.zeros_like(x)
        grad[0] = -2 * (1 - x[0]) - 400 * x[0] * (x[1] - x[0]**2)
        grad[1] = 200 * (x[1] - x[0]**2)
        return grad
    
    def hessian(self, x: np.ndarray) -> np.ndarray:
        H = np.zeros((2, 2))
        H[0, 0] = 2 - 400 * x[1] + 1200 * x[0]**2
        H[0, 1] = -400 * x[0]
        H[1, 0] = -400 * x[0]
        H[1, 1] = 200
        return H


class RosenbrockND:
    def __init__(self, n: int):
        assert n >= 2, "Dimension must be at least 2"
        self.n = n

    def function(self, x: np.ndarray) -> float:
        return np.sum((1 - x[:-1])**2 + 100 * (x[1:] - x[:-1]**2)**2)
    
    def gradient(self, x: np.ndarray) -> np.ndarray:
        grad = np.zeros_like(x)

        grad[0] = -2 * (1 - x[0]) - 400 * x[0] * (x[1] - x[0]**2)

        for i in range(1, self.n - 1):
            grad[i] = 200 * (x[i] - x[i - 1]**2) - 2 * (1 - x[i]) - 400 * x[i] * (x[i + 1] - x[i]**2)

        grad[-1] = 200 * (x[-1] - x[-2]**2)

        return grad
    
    def hessian(self, x: np.ndarray) -> np.ndarray:
        H = np.zeros((self.n, self.n))

        H[0, 0] = 2 - 400 * x[1] + 1200 * x[0]**2
        H[self.n - 1, self.n - 1] = 200

        for i in range(1, self.n - 1):
            H[i, i] = 202 + 1200 * x[i]**2 - 400 * x[i + 1]
            H[i, i - 1] = -400 * x[i]
            H[i, i + 1] = -400 * x[i]

        return H
    

class DataFit:
    def __init__(self, y: np.ndarray = np.array([1.5, 2.25, 2.625])):
        self.y = y
    
    def function(self, x):
        y = self.y
        return (y[0] - x[0] + x[0] * x[1])**2 + (y[1] - x[0] + x[0] * x[1]**2)**2 + (y[2] - x[0] + x[0] * x[1]**3)**2

    def gradient(self, x):
        y = self.y
        df_dx = (2 * (y[0] - x[0] + x[0] * x[1]) * (-1 + x[1]) + 
                2 * (y[1] - x[0] + x[0] * x[1]**2) * (-1 + x[1]**2) + 
                2 * (y[2] - x[0] + x[0] * x[1]**3) * (-1 + x[1]**3))

        df_dy = (2 * (y[0] - x[0] + x[0] * x[1]) * x[0] + 
                2 * (y[1] - x[0] + x[0] * x[1]**2) * (2 * x[0] * x[1]) + 
                2 * (y[2] - x[0] + x[0] * x[1]**3) * (3 * x[0] * x[1]**2))

        return np.array([df_dx, df_dy])

    def hessian(self, x):
        x1, x2 = x

        H11 = 2 * x2**6 + 2 * x2**4 - 4 * x2**3 - 2 * x2**2 - 4 * x2 + 6
        H12 = 12 * x1 * x2**5 + 8 * x1 * x2**3 - 12 * x1 * x2**2 - 4 * x1 * x2 - 4 * x1 + 15.75 * x2**2 + 9 * x2 + 3
        H21 = H12 
        H22 = 30 * x1**2 * x2**4 + 12 * x1**2 * x2**2 - 12 * x1**2 * x2 - 2 * x1**2 + 31.5 * x1 * x2 + 9 * x1

        H = np.array([[H11, H12],
                    [H21, H22]])

        return H

    

class Exponential:
    def __init__(self, n: int):
        self.n = n

    def function(self, x: np.ndarray) -> float:
        f = (np.exp(x[0]) -1)/(np.exp(x[0]) + 1) + 0.1 * np.exp(-x[0])

        f += np.sum((x[1:] - 1)**4)

        return f
    
    def gradient(self, x: np.ndarray) -> np.ndarray:
        grad = np.zeros_like(x)
        grad[0] = (2 * np.exp(x[0])) / (np.exp(x[0]) + 1)**2 - 0.1 * np.exp(-x[0])

        for i in range(1, self.n):
            grad[i] = 4 * (x[i] - 1)**3

        return grad
    
    def hessian(self, x: np.ndarray) -> np.ndarray:
        H = np.zeros((self.n, self.n))
        
        H[0, 0] = 2 * np.exp(x[0]) * (1 - np.exp(x[0])) / (np.exp(x[0]) + 1)**3 + 0.1 * np.exp(-x[0])

        for i in range(1, self.n):
            H[i, i] = 12 * (x[i] - 1)**2

        return H

import numpy as np

class Genhumps:
    def function(self, x: np.ndarray) -> float:
        f_val = 0.0
        for i in range(4):
            f_val += np.sin(2 * x[i])**2 * np.sin(2 * x[i+1])**2 + 0.05 * (x[i]**2 + x[i+1]**2)
        return f_val

    def gradient(self, x: np.ndarray) -> np.ndarray:
        """
        Computes the gradient of f with respect to x:
            grad[0] = 0.1*x[0] + 4*sin(2*x[0])*sin(2*x[1])^2*cos(2*x[0])
            grad[i] = 0.2*x[i] + 4*sin(2*x[i-1])^2*sin(2*x[i])*cos(2*x[i])
                      + 4*sin(2*x[i])*sin(2*x[i+1])^2*cos(2*x[i]) for i=1,2,3
            grad[4] = 0.1*x[4] + 4*sin(2*x[3])^2*sin(2*x[4])*cos(2*x[4])
        """
        grad = np.zeros(5)
        # First element
        grad[0] = 0.1 * x[0] + 4 * np.sin(2 * x[0]) * (np.sin(2 * x[1])**2) * np.cos(2 * x[0])
        # Last element
        grad[4] = 0.1 * x[4] + 4 * (np.sin(2 * x[3])**2) * np.sin(2 * x[4]) * np.cos(2 * x[4])
        # Middle elements (i=1,2,3)
        for i in range(1, 4):
            grad[i] = (
                0.2 * x[i]
                + 4 * (np.sin(2 * x[i-1])**2) * np.sin(2 * x[i]) * np.cos(2 * x[i])
                + 4 * np.sin(2 * x[i]) * (np.sin(2 * x[i+1])**2) * np.cos(2 * x[i])
            )
        return grad

    def hessian(self, x: np.ndarray) -> np.ndarray:
        """
        Computes the Hessian matrix of f. The nonzero elements are:
        
        Diagonals:
            H[0,0] = -8*sin(2*x[0])^2*sin(2*x[1])^2 + 8*sin(2*x[1])^2*cos(2*x[0])^2 + 0.1
            H[1,1] = -8*sin(2*x[0])^2*sin(2*x[1])^2 + 8*sin(2*x[0])^2*cos(2*x[1])^2
                     -8*sin(2*x[1])^2*sin(2*x[2])^2 + 8*sin(2*x[2])^2*cos(2*x[1])^2 + 0.2
            H[2,2] = -8*sin(2*x[1])^2*sin(2*x[2])^2 + 8*sin(2*x[1])^2*cos(2*x[2])^2
                     -8*sin(2*x[2])^2*sin(2*x[3])^2 + 8*sin(2*x[3])^2*cos(2*x[2])^2 + 0.2
            H[3,3] = -8*sin(2*x[2])^2*sin(2*x[3])^2 + 8*sin(2*x[2])^2*cos(2*x[3])^2
                     -8*sin(2*x[3])^2*sin(2*x[4])^2 + 8*sin(2*x[4])^2*cos(2*x[3])^2 + 0.2
            H[4,4] = -8*sin(2*x[3])^2*sin(2*x[4])^2 + 8*sin(2*x[3])^2*cos(2*x[4])^2 + 0.1
        
        Off-diagonals (symmetric):
            H[0,1] = 2*cos(4*x[0] - 4*x[1]) - 2*cos(4*x[0] + 4*x[1])
            H[1,2] = 2*cos(4*x[1] - 4*x[2]) - 2*cos(4*x[1] + 4*x[2])
            H[2,3] = 2*cos(4*x[2] - 4*x[3]) - 2*cos(4*x[2] + 4*x[3])
            H[3,4] = 2*cos(4*x[3] - 4*x[4]) - 2*cos(4*x[3] + 4*x[4])
        """
        H = np.zeros((5, 5))
        x1, x2, x3, x4, x5 = x[0], x[1], x[2], x[3], x[4]
        
        # Diagonal entries
        H[0, 0] = -8 * (np.sin(2*x1)**2) * (np.sin(2*x2)**2) + 8 * (np.sin(2*x2)**2) * (np.cos(2*x1)**2) + 0.1
        H[1, 1] = (
            -8 * (np.sin(2*x1)**2) * (np.sin(2*x2)**2)
            + 8 * (np.sin(2*x1)**2) * (np.cos(2*x2)**2)
            -8 * (np.sin(2*x2)**2) * (np.sin(2*x3)**2)
            + 8 * (np.sin(2*x3)**2) * (np.cos(2*x2)**2)
            + 0.2
        )
        H[2, 2] = (
            -8 * (np.sin(2*x2)**2) * (np.sin(2*x3)**2)
            + 8 * (np.sin(2*x2)**2) * (np.cos(2*x3)**2)
            -8 * (np.sin(2*x3)**2) * (np.sin(2*x4)**2)
            + 8 * (np.sin(2*x4)**2) * (np.cos(2*x3)**2)
            + 0.2
        )
        H[3, 3] = (
            -8 * (np.sin(2*x3)**2) * (np.sin(2*x4)**2)
            + 8 * (np.sin(2*x3)**2) * (np.cos(2*x4)**2)
            -8 * (np.sin(2*x4)**2) * (np.sin(2*x5)**2)
            + 8 * (np.sin(2*x5)**2) * (np.cos(2*x4)**2)
            + 0.2
        )
        H[4, 4] = -8 * (np.sin(2*x4)**2) * (np.sin(2*x5)**2) + 8 * (np.sin(2*x4)**2) * (np.cos(2*x5)**2) + 0.1
        
        # Off-diagonal entries
        H[0, 1] = 2 * np.cos(4*x1 - 4*x2) - 2 * np.cos(4*x1 + 4*x2)
        H[1, 0] = H[0, 1]
        
        H[1, 2] = 2 * np.cos(4*x2 - 4*x3) - 2 * np.cos(4*x2 + 4*x3)
        H[2, 1] = H[1, 2]
        
        H[2, 3] = 2 * np.cos(4*x3 - 4*x4) - 2 * np.cos(4*x3 + 4*x4)
        H[3, 2] = H[2, 3]
        
        H[3, 4] = 2 * np.cos(4*x4 - 4*x5) - 2 * np.cos(4*x4 + 4*x5)
        H[4, 3] = H[3, 4]
        
        return H
