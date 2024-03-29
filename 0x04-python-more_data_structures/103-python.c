#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - prints some basic info about Python bytes objects.
 * @p: Pointer to pyobject.
 *
 * Return: Void.
 */

void print_python_bytes(PyObject *p)
{
	long int s, i, l;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	s = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", s);
	printf("  trying string: %s\n", str);

	if (s >= 10)
		l = 10;
	else
		l = s + 1;
	printf("  first %ld bytes:", l);

	for (i = 0; i < l; i++)
	{
		if (str[i] >= 0)
			printf(" %02x", str[i]);
		else
			printf(" %02x", 256 + str[i]);
	}

	printf("\n");
}

/**
 * print_python_list - prints some basic info about Python lists objects.
 * @p: Pointer to pyobject.
 *
 * Return: Void.
 */

void print_python_list(PyObject *p)
{
	PyListObject *l;
	PyObject *ob;
	long int s, i;

	s = ((PyVarObject *)(p))->ob_size;
	l = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", s);
	printf("[*] Allocated = %ld\n", l->allocated);

	for (i = 0; i < s; i++)
	{
		ob = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((ob)->ob_type)->tp_name);

		if (PyBytes_Check(ob))
			print_python_bytes(ob);
	}
}
