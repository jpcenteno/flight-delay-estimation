#ifndef __CML__HEADER_IMPL__
#define __CML__HEADER_IMPL__

#include <Eigen/Dense>
using namespace std;
using namespace Eigen;

/**
   If the matrix A is ill-conditioned, then this is not a good method, because
   the condition number of ATA is the square of the condition number of A. This
   means that you lose twice as many digits using normal equation than if you
   use the other methods.
*/
struct NormalEquationsSolver{
    static
    VectorXf lstsq(MatrixXf A, VectorXf b) {
        return (A.transpose() * A).ldlt().solve(A.transpose() * b);
    }
};

struct SVDSolver {
    static
    VectorXf lstsq(MatrixXf A, VectorXf b){
        return A.bdcSvd(ComputeThinU | ComputeThinV).solve(b);
    }
};

/**
   (no pivoting, so fast but unstable)
*/
struct QRSolver {
    static VectorXf lstsq(MatrixXf A, VectorXf b) {
        return A.householderQr().solve(b);
    }
};

/**
   (column pivoting, thus a bit slower but more accurate)
*/
struct QRColPivotSolver {
    static VectorXf lstsq(MatrixXf A, VectorXf b) {
        return A.colPivHouseholderQr().solve(b);
    }
};

/**
   (full pivoting, so slowest and most stable)
*/
struct QRFullPivotSolver {
    static VectorXf lstsq(MatrixXf A, VectorXf b) {
        return A.fullPivHouseholderQr().solve(b);
    }
};

#endif
