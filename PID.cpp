#include <iostream>
using namespace std;
int main(){
	return 0;
}

double PID(double In){
	out = P_gain*In + I_gain*InSum + D_gain*InDiff;
	InSum += In;
	InDiff = In - InOld;
	InOld = In;
	return out;
}