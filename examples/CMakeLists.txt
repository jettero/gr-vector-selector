
########################################################################
# Install GRC xml files
########################################################################

list(APPEND grc_sources
    vector-selector.xml
)

install(
    FILES ${grc_sources}
    DESTINATION ${GRC_EXAMPLES_DIR}
    COMPONENT "grvectorselector_python"
)
