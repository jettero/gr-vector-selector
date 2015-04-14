
########################################################################
# Install GRC xml files
########################################################################

list(APPEND grc_examples
    vector-selector-demo1.grc
    vector-selector-demo2.grc
)

install(
    FILES ${grc_examples}
    DESTINATION ${GRC_EXAMPLES_DIR}
    COMPONENT "grvectorselector_python"
)
