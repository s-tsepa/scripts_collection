#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct{
    float x;
    float y;
} Point;

float distance(Point A, Point B){
	float result;
	
	result = pow(
                pow( B.x - A.x, 2) +
                pow(B.y - A.y, 2),
            0.5);
	
	return result;
}

float area(Point A, Point B, Point C){
	float result;

    result = (A.x * B.y - B.x * A.y + B.x * C.y - C.x * B.y + C.x * A.y - A.x * C.y) / 2;
	
	return result;
}

int main(void){

	Point A = { 2.5f, 6 };
    Point B = { 1, 2.2f };
    Point C = { 10, 6 };


    float f = distance(A, B);
	printf("A -- B distance is %f\n", f);


	float a = area(A, B, C);
	printf("Area of triangle ABC is %f\n", a);

	return EXIT_SUCCESS;
}
