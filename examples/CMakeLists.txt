
########################################################################
# Install GRC xml files
########################################################################

list(APPEND grc_examples
    vector-selector.grc
)

install(
    FILES ${grc_examples}
    DESTINATION ${GRC_EXAMPLES_DIR}
    COMPONENT "grvectorselector_python"
)
