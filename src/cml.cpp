#include "submodules/pybind11/include/pybind11/pybind11.h"
#include "submodules/pybind11/include/pybind11/eigen.h"
#include "cml-impl.h"

namespace py=pybind11;

// el primer argumento es el nombre...
PYBIND11_MODULE(cml_cpp, m) {
    py::class_<NormalEquationsSolver>(m, "normal_equations_solver")
            .def_static("lstsq", &NormalEquationsSolver::lstsq);

    py::class_<SVDSolver>(m, "svd_solver")
        .def_static("lstsq", &SVDSolver::lstsq);

    py::class_<QRSolver>(m, "qr_solver")
        .def_static("lstsq", &QRSolver::lstsq);

    py::class_<QRColPivotSolver>(m, "qr_col_pivot_solver")
        .def_static("lstsq", &QRColPivotSolver::lstsq);

    py::class_<QRFullPivotSolver>(m, "qr_full_pivot_solver")
        .def_static("lstsq", &QRFullPivotSolver::lstsq);
}
