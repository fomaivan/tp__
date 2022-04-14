set(SOURCES ${02-source-files})
set(TARGET_NAME "02-tree")
set(COVERAGE_NAME "02-coverage")
set(SOURCE_DIR_MAIN "${02-tree_SOURCE_DIR}")
set(COVERAGE_TARGET "02-coverage-tree")
message(INFO ${SOURCES})

set(TEST_SOURCES TreeTestCase.cpp TreeTestCase.h)
run_coverage(
	"${TARGET_NAME}"
	"${COVERAGE_NAME}"
	"${COVERAGE_TARGET}"
        "${SOURCES}"
        "${TEST_SOURCES}"
)