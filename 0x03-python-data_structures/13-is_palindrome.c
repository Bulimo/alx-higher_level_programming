#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - checks if singly linked list is a palindrome
 * @head: pointer to pointer of first node
 * Return: 1 if is palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int len = 0, i = 0;
	int *data;
	listint_t *iter;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	iter = *head;
	while (iter)
	{
		len++;
		iter = iter->next;
	}
	data = malloc(sizeof((*head)->n) * ((len + 1) / 2));
	if (data == NULL)
		exit(1);
	iter = *head;
	while (iter)
	{
		if (i < ((len + 1) / 2))
			data[i] = iter->n;
		else
		{
			if (iter->n != data[len - i - 1])
			{
				free(data);
				return (0);
			}
		}
		i++;
		iter = iter->next;
	}
	free(data);
	return (1);
}
