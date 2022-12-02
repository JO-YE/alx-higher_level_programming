#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
* check_cycle - function that checks if a singly linked list 
* has a cycle in it.
* @list: linked list
* Return: Always 0
*/
int check_cycle(listint_t *list)
{
	listint_t *temp = list->next;

	while(temp)
	{
		if (temp == list)
			return(1);
		temp = temp->next;
	}
	return(0);
}
/* got to read more on this topic */
