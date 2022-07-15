#include <iostream>
#include <string>
#include <algorithm>
#include <execution>


//define a callable "transform" object

struct transform_t {
	template<typename... Args>
	auto operator()(Args&&... args) {
		return std::transform(std::execution::par, args...);
	}
}transform{};

#include "transform.hpp"

