import numpy as np

A = np.matrix([[1, 2], [3, 4]])
B = np.matrix([[0, 5], [10, 15]])

C = np.matrix([[None, None], [None, None]])

C[0, 0] = A[0, 0] * B[0, 0] + A[0, 1] * B[1, 0]
C[0, 1] = A[0, 0] * B[0, 1] + A[0, 1] * B[1, 1]
C[1, 0] = A[1, 0] * B[0, 0] + A[1, 1] * B[1, 0]
C[1, 1] = A[1, 0] * B[0, 1] + A[1, 1] * B[1, 1]

print(C)

# Same result
print(np.matmul(A, B))

# Same result
print(A@B)


class LinearRegressionOperator:
    def __init__(self, reg_coeff=0.0):
        self.weights = None
        self.reg_coeff = reg_coeff

    def fit(self, X, y):
        X = np.c_[np.ones(X.shape[0]), X]
        reg_term = self.reg_coeff * np.eye(X.shape[1])
        self.weights = np.linalg.inv(X.T @ X + reg_term) @ X.T @ y

    def predict(self, X):
        X = np.c_[np.ones(X.shape[0]), X]
        return X @ self.weights




