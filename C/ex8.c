#include <stdio.h>

int main(int argc, char *argv[])
{

	int areas[] = {10, 12, 13, 14, 20};
	char name[] = "Zed";
	char full_name[] = {
		'Z', 'e', 'd', ' ',
		'A', '.', ' ',
		'S', 'h', 'a', 'w', '\0'
	};

// WARNING: On some systems you may have to change the
// %ld in this code to a %u since it will use unsigned ints
	printf("The size of an int: %ld\n", sizeof(int));
	printf("The size of areas (int[]): %ld\n",
			sizeof(areas));
	printf("The number of ints in areas: %ld\n",
			sizeof(areas) / sizeof(int));
	printf("The first area is %d, the 2nd %d.\n",
			areas[0], areas[1]);

	printf("The size of a char: %ld\n", sizeof(char));
	printf("The size of name (char[]): %ld\n",
			sizeof(name));
	printf("The number of chars: %ld\n",
			sizeof(name) / sizeof(char));

	printf("name=\"%s\" and full_name=\"%s\"\n",
			name, full_name);

	areas[0] = 100;
	printf("areas[0]= %d\n", areas[0]);

	full_name[0] = 'T';
	printf("full_name =\"%s\"\n", full_name);

	// Why is this allowed? areas[] is an array of integers while name[]
	// is an array of characters.
	areas[1] = name[0];
	printf("areas[1]=\"%c\"\n", areas[1]);

	return 0;
}