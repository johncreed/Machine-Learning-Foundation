#include <cstdio>
#include <stdlib.h>
#include <vector>
#include <typeinfo>
#include <algorithm>
#include <cmath>
#include <utility>
#include <tuple>
#include <cstdlib>
using namespace std;

/*==========================Define Tree Node=======================*/

class node{
	public:
		bool  is_leaf=0;
		int class_val;
		int index=0;
		double cut=0;
		node *left=NULL;
		node *right=NULL;
		bool check_leaf();
};

bool node::check_leaf(){
		if(is_leaf==0) return false; else return true;
}

class node* newNode(int index,double cut){
	class node* node = new(class node);
	node->index = index;
	node->cut = cut;
	return(node);
};

/*======================Define single input format=======================*/

class S{
	public:	
		double x[3];
		S (double,double,double);
};

S::S (double a,double b, double c){
	x[0]=a,x[1]=b,x[2]=c;
}

bool sort_f_one(const S &a, const S &b){ return a.x[0] < b.x[0];}
bool sort_f_two(const S &a, const S &b){ return a.x[1] < b.x[1];}
bool sort_f_third(const S &a, const S &b){ return a.x[2] < b.x[2];}


/*===========================Define Functioin============================*/

using Iter = vector<S>::iterator;
using Iter_const = vector<S>::const_iterator;
using Iter_f = vector<node*>:: iterator;

void print_data(vector<S> &a){
		for(Iter it=a.begin();it<a.end();it++){
			printf("%lf %lf %.0lf\n", it->x[0], it->x[1], it->x[2] );
		}
}

double gini(vector<S> &a){
	double c_one=0, c_two=0;
	for(Iter it = a.begin();it < a.end(); it++){
		if( it->x[2] == 1){ c_one++;} else { c_two++;}
	}
	double N = a.size();
	if(N==0) return 0; else return 1-pow(c_one/N,2)-pow(c_two/N,2);
}

tuple<vector<S>,vector<S>,double,double> decision_stump(vector<S> &a){
	double best_score= a.size();
	int index = 0;
	double cut = 0;
	vector<S> left;
	vector<S> right;
	for(int i=0; i < 2; i++){ 
			if(i==0) sort(a.begin(),a.end(),sort_f_one); else sort(a.begin(), a.end(),sort_f_two);
			//printf("*********SORT******\n");
			//print_data(a);
			for(Iter it = a.begin(); it < a.end(); it++){
				vector<S> one (a.begin(),it);
				vector<S> two (it,a.end());
				double score  = one.size() * gini(one) + two.size() * gini(two);
				if (score < best_score){
					best_score = score;
					index = i;
					if(one.empty()) cut = two[0].x[index]; else cut = (one.back().x[index]+two.front().x[index])/2;
					left = one;
					right = two;
				}
			}
	}
	return tuple<vector<S>,vector<S>,double,double> (left,right,index,cut);
}

bool is_y_diff(vector<S> &data){
		double first = data[0].x[2];
		for(Iter it = data.begin(); it < data.end(); it++){
				if(it->x[2] != first) return true;
		}
		return false;
}

bool is_x_diff(vector<S> &data){
		pair<double,double> first (data[0].x[0],data[0].x[1]);
		for (Iter it = data.begin(); it < data.end(); it++){
				if(first != pair<double,double> (it->x[0],it->x[1])) return true;
		}
		return false;
}

void read_file(int argc,char** argv, vector<S> &data,int index){
		if (argc < 3){
			perror("Please enter the file name.");
			exit(1);
		}
		FILE *pFile;
		pFile = fopen(argv[index],"r");
		if(pFile != NULL){
				double a,b,c;
				while(fscanf(pFile, "%lf %lf %lf", &a,&b,&c) != EOF){
					data.emplace_back(S(a,b,c));
				}	
		}
		fclose(pFile);
}

int leaf_class(vector<S> &a){
		int one = 0, two = 0;
		for(Iter it = a.begin(); it<a.end();it++){
				if(it->x[2] == 1) one++; else two++;
		}
		if(one > two) return 1; else return -1;
}

class node* built_tree(vector<S> &a){
		//printf("Branching\n");
		class node *node = new(class node);
		if ( !(is_y_diff(a) && is_x_diff(a))){
			node->is_leaf = 1;
			node->class_val = leaf_class(a);
			return node;
		}
		else{
			//printf("spliting\n");
			tuple<vector<S>,vector<S>,double,double> cut = decision_stump(a);
			//printf("end split\n");
			vector<S> left = get<0>(cut);
			vector<S> right = get<1>(cut);
			//printf("left size: %lu right size: %lu\n",left.size(),right.size());
			node->index = get<2>(cut);
			node->cut = get<3>(cut);
			
			//printf("====================Left_%lf index_%d======================\n",node->cut,node->index);
			//if(left.size() != 0) print_data(left);
			//printf("===================Right_%lf index_%d======================\n",node->cut,node->index);
			//if(right.size() != 0) print_data(right);

			if(left.size() != 0) node->left = built_tree(left);
			if(right.size() != 0) node->right = built_tree(right);
			return node;

		}
}

double err_cal(class S &x, node *node){
		class node *curr=node;
		double value=0;
		if(curr->check_leaf()){
				if(x.x[2] == curr->class_val) return 0; else return 1;
		}
		else{
				if(x.x[curr->index] <= curr->cut) value = err_cal(x,curr->left); else value =  err_cal(x,curr->right);
		}
		return value;
}

double err(vector<S> &a,class node *root){
		double err_val=0;
		double N = a.size();
		for(Iter it=a.begin();it<a.end();it++){
				err_val += err_cal(*it,root);
		}
		return err_val/N;
}

double err_forest(vector<S> &a,vector<node*> &forest){
		double err_val=0;
		double N = a.size();
		double total_vote = forest.size();
		for(Iter it=a.begin(); it < a.end();it++){
				double vote=0;
				for(Iter_f f=forest.begin(); f<forest.end(); f++){
						vote += err_cal(*it,*f);
				}
				if (vote > total_vote/2) err_val++;
		}
		return err_val/N;
}

vector<S> bagging(vector<S> data, int N){
		vector<S> data_r;
		for(int i=0; i < N; i++){
				data_r.emplace_back(data[rand() % N]);
		}
		return data_r;
}

int main(int argc, char** argv){
		vector<S> data;		
		read_file(argc,argv,data,1);
		decision_stump(data);
		class node *root = built_tree(data);
		printf("%lf\n",err(data,root));
		vector<S> test;
		read_file(argc,argv,test,2);
		printf("%lf\n",err(test,root));
		

		int T = 30000;
		printf("===========%d============", T);
		int N = data.size();
		vector<class node*> forest;
		for(int i=0; i < T; i++){
				vector<S> data_n = bagging(data,N);
				class node* root = built_tree(data_n);
				forest.emplace_back(root);
		}
		printf("%lf\n",err_forest(test,forest));

		for(int i=1; i <= 30000; i++){
			vector<class node*> sub_forest (forest.begin(), forest.begin()+i);
			printf("T=%d %lf\n",i,err_forest(test,sub_forest));
		}
}


