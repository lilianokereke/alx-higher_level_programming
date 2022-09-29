#include "lists.h"
/**
 * print_dlistint- print elements of the list
 * @h : the head pointer
 * Return: number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	int count = 0;

	while (h)
	{
		printf("%d", h->n);
		h = h->next;
		count++;
	}
	return (count);
}
