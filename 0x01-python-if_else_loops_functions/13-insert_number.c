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
	listint_t *freshnode;

	freshnode = malloc(sizeof(listint_t));
	if (freshnode == NULL)
		return (NULL);

	freshnode->n = number;
	freshnode->next = *head;
	*head = freshnode;

	return (freshnode);
}
