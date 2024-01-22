#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_bytes - prints some basic info about Python bytes objects.
 * @p: Pointer to pyobject.
 *
 * Return: Void.
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t s, i;
	PyBytesObject *bt = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bt->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		s = 10;
	else
		s = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld bytes: ", s);
	for (i = 0; i < s; i++)
	{
		printf("%02hhx", bt->ob_sval[i]);
		if (i == (s - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_list - prints some basic info about Python lists objects.
 * @p: Pointer to pyobject.
 *
 * Return: Void.
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t s, a, i;
	const char *t;
	PyListObject *l = (PyListObject *)p;
	PyVarObject *v = (PyVarObject *)p;

	s = v->ob_size;
	a = l->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", s);
	printf("[*] Allocated = %ld\n", a);

	for (i = 0; i < s; i++)
	{
		t = l->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, t);
		if (strcmp(t, "bytes") == 0)
			print_python_bytes(l->ob_item[i]);
		else if (strcmp(t, "float") == 0)
			print_python_float(l->ob_item[i]);
	}
}

/**
 * print_python_float - Prints some basic info about Python float objects.
 * @p: Pointer to pyobject.
 *
 * Return: Void.
 */

void print_python_float(PyObject *p)
{
	char *buf = NULL;

	PyFloatObject *flo_ob = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");

	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	buf = PyOS_double_to_string(flo_ob->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buf);
	PyMem_Free(buf);
}
