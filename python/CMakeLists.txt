
########################################################################
# Setup python install
########################################################################
include(GrPython)

list(APPEND python_sources
    vector_selector.py
    __init__.py    # virtual_channel_mux.py
)

GR_PYTHON_INSTALL(
    FILES ${python_sources}
    DESTINATION ${GR_PYTHON_DIR}/grvectorselector
    COMPONENT "grvectorselector_python"
)

########################################################################
# Handle the unit tests
########################################################################
include(GrTest)

list(APPEND extras_qa_sources
    #TODO
)
#assume super tree
if(ENABLE_EXTRAS)
    list(APPEND GR_TEST_PYTHON_DIRS ${CMAKE_SOURCE_DIR}/gruel/src/python)
    list(APPEND GR_TEST_PYTHON_DIRS ${CMAKE_BINARY_DIR}/gruel/src/swig)
    list(APPEND GR_TEST_PYTHON_DIRS ${CMAKE_SOURCE_DIR}/gnuradio-core/src/python)
    list(APPEND GR_TEST_PYTHON_DIRS ${CMAKE_BINARY_DIR}/gnuradio-core/src/lib/swig)
    list(APPEND GR_TEST_TARGET_DEPS volk gruel gnuradio-core)
endif()

foreach(py_qa_test_file ${extras_qa_sources})
    set(py_qa_test_file ${CMAKE_CURRENT_SOURCE_DIR}/${py_qa_test_file})
    get_filename_component(py_qa_test_name ${py_qa_test_file} NAME_WE)
    list(APPEND GR_TEST_TARGET_DEPS gnuradio-extras)
    GR_ADD_TEST(${py_qa_test_name} ${PYTHON_EXECUTABLE} ${PYTHON_DASH_B} ${py_qa_test_file})
endforeach(py_qa_test_file)
