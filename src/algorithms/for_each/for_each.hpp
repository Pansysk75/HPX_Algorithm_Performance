#include "../utilities.hpp"

//ATTENTION: for_each function (compatible with std::for_each) 
//needs to be defined before including this file

//define a "double test(int vector_size)" function that returns
//execution time of "for_each"

utilities::timer timer;
utilities::random_vector_generator gen;

auto lam = [](double& num) {num += ((int)num % 4); };

double test(int vector_size){
	auto vec1 = gen.get_doubles(vector_size);

	timer.start();
	for_each(vec1.begin(), vec1.end(), lam);
	timer.stop();
	//use result otherwise compiler will optimize it away:
	if (std::count(vec1.begin(), vec1.end(), 42)) std::cerr << "err42";

	return timer.get();
}

#include "../main.hpp"
