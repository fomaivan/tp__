set(COVERAGE_NAME "03-coverage")
set(SOURCE_DIR_MAIN "${03-weather_SOURCE_DIR}")
set(COVERAGE_TARGET "03-coverage-weather")
set(SOURCES ${03-source-files})
set(TARGET_NAME "03-weather")

message(INFO ${SOURCES})

set(TEST_SOURCES WeatherMock.h WeatherTestCase.cpp WeatherMock.cpp WeatherTestCase.h)
run_coverage(
        "${SOURCES}"
        "${TARGET_NAME}"
        "${COVERAGE_NAME}"
        "${COVERAGE_TARGET}"
        "${TEST_SOURCES}"
)