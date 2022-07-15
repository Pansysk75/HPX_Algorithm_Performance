function(add_exe target)
    get_filename_component(alg_name ${CMAKE_CURRENT_SOURCE_DIR} NAME)
    add_hpx_executable(
        ${alg_name}_${target} 
        SOURCES ${target}.cpp
        HEADERS ../utilities.hpp
        INSTALL_SUFFIX ${alg_name}/
        COMPILE_FLAGS
    )
    set_target_properties(${alg_name}_${target} PROPERTIES OUTPUT_NAME ${target})
endfunction()


 set(subdirs 
    copy_if
    for_each
    transform
)

foreach(subdir ${subdirs})
    message("Adding subdir ${subdir}")
    add_subdirectory(${subdir})
endforeach(subdir)
