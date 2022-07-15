#include "../utilities.hpp"

//ATTENTION: copy_if function (compatible with std::copy_if) 
//needs to be defined before including this file

//define a "double test(int vector_size)" function that returns
//execution time of "copy_if"

utilities::timer timer;
utilities::random_vector_generator gen;

auto pred = [](double num) {return ((int)num % 4) < 2; };

double test(int vector_size) {
	auto vec1 = gen.get_doubles(vector_size);
	decltype(vec1) vec2(vec1.size());

	timer.start();
	copy_if(vec1.begin(), vec1.end(), vec2.begin(), pred);
	timer.stop();
	//use result otherwise compiler will optimize it away:
	if (std::count(vec2.begin(), vec2.end(), 42)) std::cerr << "err42";

	return timer.get();
}

#include "../main.hpp"
