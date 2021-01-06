//fail
int k=0;
int numberOfSteps (int num){
    while (num!=0){
        if (num%2==0) {
            numberOfSteps(num/2);
            k+=1;
        }
        else {
            numberOfSteps((num-1)/2);
            k+=1;
        }
    }
    return k;
}