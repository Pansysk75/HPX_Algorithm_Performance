#include <iostream>
#include <string>
#include <algorithm>
#include <execution>

//define a callable "for_each" object

struct for_each_t {
	template<typename... Args>
	auto operator()(Args&&... args){
		return std::for_each(std::execution::par, args...);
	}
}for_each{};

#include "for_each.hpp"
