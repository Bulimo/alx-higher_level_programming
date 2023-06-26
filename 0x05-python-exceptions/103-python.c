#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - prints basic information about Python bytes objects
 * @p: pointer to Python objects
 *
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	Py_ssize_t len = 0, size = 0, i = 0;

	printf("[.] bytes object info\n");

	if (PyBytes_Check(p))
	{
		size = PyBytes_Size(p);
		printf("  size: %lu\n", size);

		str = ((PyBytesObject *)p)->ob_sval;
		printf("  trying string: %s\n", str);

		len = size < 10 ? size + 1 : 10;
		printf("  first %ld bytes:", len);
		for (i = 0; i < len; i++)
			printf(" %x", str[i]);
		printf("%s", "\n");
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}


/**
 * print_python_float - prints basic information about Python float objects
 * @p: pointer to Python objects
 *
 */
void print_python_float(PyObject *p)
{
	double value;

	printf("[.] float object info\n");
	if (PyFloat_Check(p))
	{
		value = ((PyFloatObject *)p)->ob_fval
			printf("  value: %f\n", value);
	}
	else
		printf("  [ERROR] Invalid Float Object\n");
}


/**
 * print_python_list - prints basic info about python lists
 * @p: pointer to a python PyObject
 *
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t p_len, i = 0;
	PyListObject *elem;
	PyObject *type;

	printf("[*] Python List info\n");
	if (PyList_Check(p))
	{

		p_len = ((PyListObject *)(p))->ob_size;
		printf("[*] Size of the Python List = %lu\n", p_len);
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
		for (i = 0; i < p_len; i++)
		{
			elem = ((PyListObject *)p)->ob_item[i];
			if (elem)
			{
				type = PyObject_Type(elem)
					printf("Element %ld: %s\n", i, ((PyTypeObject *)type)->tp_name);
				if (PyBytes_Check(elem))
					print_python_bytes(elem);
				if (PyFloat_Check(elem))
					print_python_float(elem);
			}
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");

}

