#pragma once

#include <gtest/gtest.h>
#include "cpr/cpr.h"

#define private public
#include "WeatherMock.h"
#include <string>

class WeatherTestCase : public ::testing::Test {
public:
  cpr::Response bad_response;
  cpr::Response moscow_response;
  cpr::Response singapour_response;
  
  
  std::string temp_in_singapure = "{\"cod\":\"200\",\"message\":0.0036,\"cnt\":40,\"list\":[{\"dt\":1485799200,\"main\":{\"temp\":300.00}}]}";
  
  std::string temp_in_moscow = "{\"cod\":\"200\",\"message\":0.0036,\"cnt\":40,\"list\":[{\"dt\":1485799200,\"main\":{\"temp\":100.00}}]}";
  
  std::string result_string_less = "Weather in Moscow is colder than in Singapour by 200 degrees";
  std::string result_string_greater = "Weather in Singapour is warmer than in Moscow by 200 degrees";

  WeatherMock my_weather;

  
  WeatherTestCase() {
    this->bad_response = cpr::Response();
    this->bad_response.status_code = 100;
    
    this->moscow_response = cpr::Response();
    this->moscow_response.status_code = 200;
    this->moscow_response.text = this->temp_in_moscow;
    
    this->singapour_response = cpr::Response();
    this->singapour_response.status_code = 200;
    this->singapour_response.text = this->temp_in_singapure;
  }
};


TEST_F(WeatherTestCase, GetForCityInvalidArgumentTest) {
  using ::testing::_;
  using ::testing::Return;
  EXPECT_CALL(my_weather, Get(_))
    .WillOnce(Return(bad_response));
  
  ASSERT_THROW(my_weather.GetDifferenceString("Moscow", "Singapour"), std::invalid_argument);
}

TEST_F(WeatherTestCase, DifferenceTest) {
  using ::testing::Return;
  EXPECT_CALL(my_weather, Get("Moscow"))
  .Times(2)
  .WillRepeatedly(Return(moscow_response));
  EXPECT_CALL(my_weather, Get("Singapour"))
  .Times(2)
  .WillRepeatedly(Return(singapour_response));
  
  ASSERT_EQ(my_weather.GetDifferenceString("Moscow", "Singapour"), result_string_less);
  ASSERT_EQ(my_weather.GetDifferenceString("Singapour", "Moscow"), result_string_greater);

}

TEST_F(WeatherTestCase, ApiKeySettingTest) {
  my_weather.SetApiKey("test api key");
  ASSERT_EQ(my_weather.api_key_, "test api key");
}
