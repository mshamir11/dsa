#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;




int getRank(vector<int> preference,int person,int N)
{
    return N - (find(preference.begin(),preference.end(),person)  - preference.begin());                               
}

bool singlesRemaining(int *engagements, int N)
{
    if (find(engagements,engagements+N,-1)==engagements+N)
        return false;
    else
        return true;
}

void match(int i, int top, int *ME,int *WE)
{
    ME[i]=top;
    WE[top]=i;
}
void solveSM(vector<int> *M, vector<int> *W,int N)
{
    int WE[N], ME[N];
    for (int i=0;i<N;i++)
    {
        WE[i]=-1;
        ME[i]=-1;
        while(singlesRemaining(ME,N))
        {
            for (int i=0;i<N;i++)
            {
                if (ME[i]==-1)
                {
                    int top= M[i].back() - 1;
                    M[i].pop_back();
                    if (WE[top]== -1)
                    {
                        match(i,top,ME,WE);                               
                    }
                    else
                    {
                        int competition = WE[top];
                        if (getRank(W[top],i+1,N)>getRank(W[top],competition+1,N))
                        {
                            match(i,top,ME,WE);
                            ME[competition] = -1 ;
                        }
                       
                    }
                    
                }
            }
        }

    }

    for (int i=0;i<N;i++)
    {
        cout <<i+1 << " "<<ME[i]+1 <<endl;
    }
}

int main()
{
    #ifndef ONLINE_JUDGE

    freopen("int.txt","r",stdin);
    freopen("myout.txt","w",stdout);
    #endif
    int T;
    cin >>T;
    while (T--)
    {
        int N;
        cin >> N;
        
        vector <int> women[N], men[N];


        int person;
        

        for (int i=0; i<N;i++)
        {
            cin >>person;
            for (int j=0;j<N;j++)
            {
                cin >> person;
                women[i].push_back(person);
            }
            reverse(women[i].begin(),women[i].end());
        }
        for (int i=0; i<N;i++)
        {
            cin >>person;
            for (int j=0;j<N;j++)
            {
                cin >> person;
                men[i].push_back(person);
            }
            reverse(men[i].begin(),men[i].end());

        }
       solveSM(men,women,N);

    }
}