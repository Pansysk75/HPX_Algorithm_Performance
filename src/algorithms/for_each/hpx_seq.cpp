#include <iostream>
#include <string>
#include <algorithm>
#include "hpx/hpx.hpp"
#include "hpx/hpx_main.hpp"

//define a callable "for_each" object

struct for_each_t {
	template<typename... Args>
	auto operator()(Args&&... args){
		return hpx::for_each(args...);
	}
}for_each{};


#include "for_each.hpp"
