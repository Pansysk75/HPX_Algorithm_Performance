#include "../utilities.hpp"

//ATTENTION: transform function (compatible with std::transform) 
//needs to be defined before including this file

//define a "double test(int vector_size)" function that returns
//execution time of "transform"

utilities::timer timer;
utilities::random_vector_generator gen;

auto lam = [](double num) {return num + ((int)num % 4); };

double test(int vector_size) {
	auto vec1 = gen.get_doubles(vector_size);
	decltype(vec1) vec2(vec1.size());

	timer.start();
	transform(vec1.begin(), vec1.end(), vec2.begin(), lam);
	timer.stop();
	//use result otherwise compiler will optimize it away:
	if (std::count(vec2.begin(), vec2.end(), 42)) std::cerr << "err42";

	return timer.get();
}

#include "../main.hpp"
