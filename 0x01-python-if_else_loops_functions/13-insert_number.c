#include <stdlib.h>
#include "lists.h"
#include <stdio.h>

/**
  * insert_node - inserts a number into a sorted list
  * @head: pointer to a pointer to first node
  * @number: number to be inserted
  * Return: new node address or NULL on failure
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *iter_node = NULL;
	listint_t *new_node = NULL;
	listint_t *next_node = NULL;

	if (head == NULL)
		return (NULL);

	iter_node = *head;
	next_node = iter_node->next;
	while (iter_node && next_node)
	{
		if (number >= iter_node->n && number < next_node->n)
			break;
		iter_node = next_node;
		next_node = iter_node->next;
	}
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = iter_node->next;
	iter_node->next = new_node;
	return (new_node);
}
