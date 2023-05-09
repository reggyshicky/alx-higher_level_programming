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
	listint_t *n_node;
	listint_t *trail; /*temp*/

	trail = *head;

	n_node = malloc(sizeof(listint_t));
	if (n_node == NULL)
		return (NULL);
	n_node->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		n_node->next = *head;
		*head = n_node;
		return (n_node);
	}
	while (trail->next != NULL)
	{
		if ((trail->next)->n >= number)
		{
			n_node->next = trail->next;
			trail->next = n_node;
			return (n_node);
		}
		trail = trail->next;
	}
	n_node->next = NULL;
	trail->next = n_node;
	return (n_node);
}
