#include<stdio.h>
struct school
{
	
	long int roll;
	float marks;

}s1,s2;
void main(int argc, char const *argv[])
{
	
	s1.roll=15616;
	s1.marks=61649.31;

	s2=s1;
	printf("%li\n",s2.roll );
}
