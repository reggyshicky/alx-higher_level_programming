#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
/**
 * reverse_listint - Function that reverses a singly linked list
 * @head: pointer to the pointer to head of the linked list
 * Return: A pointer to the head of the reversed singly linkec list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *_node = *head;
	listint_t *nxtnode;
	listint_t *prevnode = NULL;

	while (_node)
	{
		nxtnode = _node->next;
		_node->next = prevnode;
		prevnode = _node;
		_node = nxtnode;
	}
	*head = prevnode;
	return (*head);
}
/**
 * is_palindrome - checks if the singly list is a palindrome
 * @head: Pointer to pointer to head of the singly linked list
 * Return: 0 if not palindrome, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tempo, *_rev, *middle;
	size_t size = 0;
	size_t v = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	tempo = *head;
	while (tempo)
	{
		size++;
		tempo = tempo->next;
	}
	tempo = *head;

	while (v < (size / 2) - 1)
	{
		tempo = tempo->next;
		v++;
	}
	if ((size % 2) == 0 && tempo->n != tempo->next->n)
		return (0);
	tempo = tempo->next->next;
	_rev = reverse_listint(&tempo);
	middle = _rev;

	tempo = *head;
	while (_rev)
	{
		if (tempo->n != _rev->n)
			return (0);
		tempo = tempo->next;
		_rev = _rev->next;
	}
	reverse_listint(&middle);
	return (1);
}
