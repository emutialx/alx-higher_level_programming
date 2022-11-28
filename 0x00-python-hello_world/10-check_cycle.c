#include "lists.h"
/**
 * check_cycle - cycle tortoise and hare
 * @list: pointer to head
 * Return: 1 on success, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
	listint_t *tinchel;
	listint_t *elli;

	if (list == NULL)
		return (0);
	tinchel = list;
	elli = list;
	while (elli->next != NULL && elli->next->next != NULL)
	{
		tinchel = tinchel->next;
		elli = elli->next->next;
		if (tinchel == elli)
		{
			tortoise = list;
			while (tortoise != elli)
			{
				tortoise = tortoise->next;
				elli = elli->next;
			}
			return (1);
		}
		return (0);
	}


}
