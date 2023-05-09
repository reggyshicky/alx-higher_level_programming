#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - inserts a numuber into a linked list
 * @head: head of the linked linked
 * @number: number to be inserted in linked list
 * Return: address of new node, or NULL-failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *c_rrent = NULL, *n_node = NULL, *tmp = NULL;

	if (n_node == NULL)
		return (NULL);
	n_node->n = number;
	if (*head)
	{
		c_rrent = *head;
		if (number <= c_rrent->n)
		{
			n_node->next = c_rrent;
			*head = n_node;
		}
		else
		{
			while (c_rrent->next)
			{
				if (number <= c_rrent->next->n)
				{
					tmp = c_rrent->next;
					c_rrent->next = n_node;
					n_node->next = tmp;
					return (*head);
				}
				c_rrent = c_rrent->next;
			}
			tmp = c_rrent->next;
			c_rrent->next = n_node;
			n_node->next = tmp;
		}
		return (*head);
	}
	n_node->next = NULL;
	*head = n_node;
	return (*head);
}
