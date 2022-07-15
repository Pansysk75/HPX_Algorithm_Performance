
//ATTENTION: double test(int) function 
//needs to be defined before including this file

double test_n(int iterations, int vector_size) {
	double time = 0;
	for (int i = 0; i < iterations; i++) {
		time += test(vector_size);
	}
	return time/iterations;
}

int main(int argc, char* argv[])
{
	//handle command line input arguements

	if (argc < 2) {
		std::cout << "Command line arguements not set" << std::endl;
		std::cout << "Please specify vector size, iterations" << std::endl;
		return 1;
	}

	int vector_size = std::stoi(argv[1]);
	int iterations = std::stoi(argv[2]);

	double time = test_n(iterations, vector_size);
	

	//Output result

	std::cout << time;

	return 0;
}