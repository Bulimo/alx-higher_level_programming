#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of list
 * Return: 0 if no cycle, 1 if there's a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast_ptr = NULL;
	listint_t *slow_ptr = NULL;

	if (list == NULL)
		return (0);
	fast_ptr = list;
	slow_ptr = list;
	while (fast_ptr != NULL && slow_ptr != NULL && fast_ptr->next != NULL)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;
		if (fast_ptr == slow_ptr)
		{
			fast_ptr = NULL;
			slow_ptr = NULL;
			return (1);
		}
	}
	fast_ptr = NULL;
	slow_ptr = NULL;
	return (0);
}
