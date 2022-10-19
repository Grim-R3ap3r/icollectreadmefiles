#include<iostream>
using namespace std;
struct student
 {
char name[20];
int rollno;
};
int main()
{
int i, n;
cout<<”How many students are there in OOPS  ”;
cin>>n;
struct student[n];
for(i=0;i<n;i++)
{
    cout<<"Enter the name of "<<i+1<<"th student";
    cin>>student[i].name;
    cout<<"Enter the roll number of "<<i+1<<"th student";
    cin>>student[i].rollno;
}

for(i=0;i<n;i++)
{
    cout<<"The name and roll no. of the "<<i+1<<"th student are :"<<student[i].name<<" and "<<student[i].rollno<<""<<endl;
}
}
