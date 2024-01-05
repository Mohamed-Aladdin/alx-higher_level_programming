#include "lists.h"

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: Pointer to pyobject.
 *
 * Return: Void.
 */

void print_python_list_info(PyObject *p)
{
	int n;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

	for (n = 0; n < Py_SIZE(p); i++)
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}
