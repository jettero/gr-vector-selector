
########################################################################
# Project setup
########################################################################
cmake_minimum_required(VERSION 2.6)
project(grvectorselector CXX C)
enable_testing()

list(APPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/cmake/Modules)

########################################################################
# Install directories
########################################################################
include(GrPlatform) #define LIB_SUFFIX
set(GR_RUNTIME_DIR      bin)
set(GR_LIBRARY_DIR      lib${LIB_SUFFIX})
set(GR_INCLUDE_DIR      include)
set(GR_DATA_DIR         share)
set(GR_PKG_DATA_DIR     ${GR_DATA_DIR}/gnuradio)
set(GR_DOC_DIR          ${GR_DATA_DIR}/doc)
set(GR_PKG_DOC_DIR      ${GR_DOC_DIR}/gnuradio)
set(GR_CONF_DIR         etc)
set(GR_PKG_CONF_DIR     ${GR_CONF_DIR}/gnuradio/conf.d)
set(GR_LIBEXEC_DIR      libexec)
set(GR_PKG_LIBEXEC_DIR  ${GR_LIBEXEC_DIR}/gnuradio)
set(GRC_BLOCKS_DIR      ${GR_PKG_DATA_DIR}/grc/blocks)
set(GRC_EXAMPLES_DIR    ${GR_PKG_DATA_DIR}/examples)

########################################################################
# feature check
########################################################################
include(GrPython)

########################################################################
# Create uninstall target
########################################################################
if (NOT ENABLE_EXTRAS)
    configure_file(
        ${CMAKE_CURRENT_SOURCE_DIR}/cmake/cmake_uninstall.cmake.in
        ${CMAKE_CURRENT_BINARY_DIR}/cmake_uninstall.cmake
    @ONLY)

    add_custom_target(uninstall
        ${CMAKE_COMMAND} -P ${CMAKE_CURRENT_BINARY_DIR}/cmake_uninstall.cmake
    )
endif()

########################################################################
# Add subdirectories
########################################################################
add_subdirectory(python)
add_subdirectory(grc)
add_subdirectory(examples)
