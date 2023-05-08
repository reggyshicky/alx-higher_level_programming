#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: the singly linked list to scan through
 * Return: 0 if no cycle, 1 if there is cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *start_item = list;
	listint_t *end_item = list;
	int result = 0;
	
	while ((start_item && end_item) && end_item->next)
	{
		start_item = start_item->next;
		if (end_item->next || end_item->next->next)
			end_item = end_item->next->next;
		else
			break;
		if (start_item == end_item)
		{
			result = 1;
			break;
		}
	}
	return (result);
}
