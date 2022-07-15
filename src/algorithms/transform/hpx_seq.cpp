#include <iostream>
#include <string>
#include <algorithm>
#include "hpx/hpx.hpp"
#include "hpx/hpx_main.hpp"

//define a callable "transform" object

struct transform_t {
	template<typename... Args>
	auto operator()(Args&&... args) {
		return hpx::transform(args...);
	}
}transform{};

#include "transform.hpp"

