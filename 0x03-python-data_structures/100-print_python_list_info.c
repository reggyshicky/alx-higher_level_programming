#include "/usr/include/python3.4/Python.h"
#include "/usr/include/python3.4/listobject.h"
#include "/usr/include/python3.4/object.h"
#include <stdio.h>

/**
 * print_python_list_info - prints basic info about python lists
 * @p: A PyObject list
 */
void print_python_list_info(PyObject *p)
{
	int size = 0;
	int v = 0;
	PyObject *_object;
	PyListObject *_clon = (PyListObject *) p;
	
	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", (int) _clon->allocated);

	for (; v < size; ++v)
	{		
		_object = PyList_GET_ITEM(p, v);
		printf("Element %d: %s\n", v, _object->ob_type->tp_name);
	}
	return;
}
