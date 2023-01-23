#include "../GrML_cpp/pybind11/pybind11/include/pybind11/pybind11.h"
#include <Python.h>

namespace py = pybind11;

int SUM(int i, int j)
{
    return i + j;
}


 
PYBIND11_MODULE(GrML, m) {

    m.doc() = "Doc string";

    m.def("sum", &SUM, R"pbdoc(
        sum function
    )pbdoc");

#ifdef VERSION_INFO
    m.attr("__version__") = VERSION_INFO;
#else
    m.attr("__version__") = "dev";
#endif
}