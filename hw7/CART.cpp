#include <cstdio>
#include <stdlib.h>
#include <vector>
#include <typeinfo>
#include <algorithm>
#include <cmath>
#include <utility>
#include <tuple>
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
};

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
	double N = a.size();
	double index = 0;
	double cut = 0;
	vector<S> left;
	vector<S> right;
	for(int i=0; i < 1; i++){ 
			if(i==0)sort(a.begin(),a.end(),sort_f_one); else sort(a.begin(), a.end(),sort_f_two);
			for(Iter it = a.begin(); it < a.end(); it++){
				vector<S> one (a.begin(),it);
				vector<S> two (it,a.end());
				double score  = one.size() * gini(one) + two.size() * gini(two);
				if (score < best_score){
					best_score = score;
					index = i;
					cut = one.size();
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
				if(it->x[2] != first) return true; else return false;
		}
}

bool is_x_diff(vector<S> &data){
		pair<double,double> first (data[0].x[0],data[0].x[1]);
		for (Iter it = data.begin(); it < data.end(); it++){
				if(first != pair<double,double> (it->x[0],it->x[1])) return true; else return false;
		}
}

void read_file(int argc,char** argv, vector<S> &data){
		if (argc < 2){
			perror("Please enter the file name.");
			exit(1);
		}
		FILE *pFile;
		pFile = fopen(argv[1],"r");
		if(pFile != NULL){
				double a,b,c;
				while(fscanf(pFile, "%lf %lf %lf", &a,&b,&c) != EOF){
					data.emplace_back(S(a,b,c));
				}	
		}
}

int leaf_class(vector<S> &a){
		int one = 0, two = 0;
		for(Iter it = a.begin(); it<a.end();it++){
				if(it->x[2] == 1) one++; else two++;
		}
		if(one > two) return 1; else return -1;
}

class node* built_tree(vector<S> &a){
		class node *node = new(class node);
		if ( !(is_y_diff(a) || is_x_diff(a))){
			node->is_leaf = 1;
			node->class_val = leaf_class(a);
			return node;
		}
		else{
			tuple<vector<S>,vector<S>,double,double> cut = decision_stump(a);
			vector<S> left = get<0>(cut);
			vector<S> right = get<1>(cut);
			int index = get<2>(cut);
			node->index = index;
			if(left.empty()) node->cut = right[0].x[index]; else node->cut = (left.back().x[index]+right.front().x[index]);
			node->left = built_tree(left);
			node->right = built_tree(right);
			return node;
		}
}

int main(int argc, char** argv){
		vector<S> data;		
		read_file(argc,argv,data);
		decision_stump(data);

		class node *root = built_tree(data);
}


