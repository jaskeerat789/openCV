#include<stdio.h>
struct school
{
	char name[100];
	long int roll;
	float marks;

};


void main(int argc, char const *argv[])
{
	struct school student[5];
	int i;
	for(i=0;i<5;i++)
	{
		scanf("%s",student[i].name);
		scanf("%li",&student[i].roll);
		scanf("%f",&student[i].marks);


	}

	for(i=0;i<5;i++)
	{
		puts(student[i].name);
		printf("%li\n",student[i].roll);
		printf("%f\n\n",student[i].marks);
	}
	
}
