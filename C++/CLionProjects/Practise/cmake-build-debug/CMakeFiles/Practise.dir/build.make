# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.29

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/malik/.local/share/JetBrains/Toolbox/apps/clion/bin/cmake/linux/x64/bin/cmake

# The command to remove a file.
RM = /home/malik/.local/share/JetBrains/Toolbox/apps/clion/bin/cmake/linux/x64/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/malik/Dev/college_stuff/C++/CLionProjects/Practise

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/malik/Dev/college_stuff/C++/CLionProjects/Practise/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/Practise.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/Practise.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/Practise.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/Practise.dir/flags.make

CMakeFiles/Practise.dir/main.cpp.o: CMakeFiles/Practise.dir/flags.make
CMakeFiles/Practise.dir/main.cpp.o: /home/malik/Dev/college_stuff/C++/CLionProjects/Practise/main.cpp
CMakeFiles/Practise.dir/main.cpp.o: CMakeFiles/Practise.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/home/malik/Dev/college_stuff/C++/CLionProjects/Practise/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/Practise.dir/main.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/Practise.dir/main.cpp.o -MF CMakeFiles/Practise.dir/main.cpp.o.d -o CMakeFiles/Practise.dir/main.cpp.o -c /home/malik/Dev/college_stuff/C++/CLionProjects/Practise/main.cpp

CMakeFiles/Practise.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/Practise.dir/main.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/malik/Dev/college_stuff/C++/CLionProjects/Practise/main.cpp > CMakeFiles/Practise.dir/main.cpp.i

CMakeFiles/Practise.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/Practise.dir/main.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/malik/Dev/college_stuff/C++/CLionProjects/Practise/main.cpp -o CMakeFiles/Practise.dir/main.cpp.s

# Object files for target Practise
Practise_OBJECTS = \
"CMakeFiles/Practise.dir/main.cpp.o"

# External object files for target Practise
Practise_EXTERNAL_OBJECTS =

Practise: CMakeFiles/Practise.dir/main.cpp.o
Practise: CMakeFiles/Practise.dir/build.make
Practise: CMakeFiles/Practise.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/home/malik/Dev/college_stuff/C++/CLionProjects/Practise/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable Practise"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/Practise.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/Practise.dir/build: Practise
.PHONY : CMakeFiles/Practise.dir/build

CMakeFiles/Practise.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/Practise.dir/cmake_clean.cmake
.PHONY : CMakeFiles/Practise.dir/clean

CMakeFiles/Practise.dir/depend:
	cd /home/malik/Dev/college_stuff/C++/CLionProjects/Practise/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/malik/Dev/college_stuff/C++/CLionProjects/Practise /home/malik/Dev/college_stuff/C++/CLionProjects/Practise /home/malik/Dev/college_stuff/C++/CLionProjects/Practise/cmake-build-debug /home/malik/Dev/college_stuff/C++/CLionProjects/Practise/cmake-build-debug /home/malik/Dev/college_stuff/C++/CLionProjects/Practise/cmake-build-debug/CMakeFiles/Practise.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/Practise.dir/depend

