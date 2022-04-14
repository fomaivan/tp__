//
// Created by akhtyamovpavel on 5/1/20.
//


#pragma once

#include <gtest/gtest.h>
#include "Functions.h"

class LeapTestCase : public ::testing::Test {
 public:
  LeapTestCase() = default;
};

TEST_F(LeapTestCase, DevidesInto400) {
    ASSERT_TRUE(IsLeap(800));
}
TEST_F(LeapTestCase, DoesntDevideInto4) {
    ASSERT_FALSE(IsLeap(55));
}
TEST_F(LeapTestCase, DevidesInto100) {
    ASSERT_FALSE(IsLeap(500));
}
TEST_F(LeapTestCase, DevidesInto4) {
    ASSERT_TRUE(IsLeap(88));
}
TEST_F(LeapTestCase, InvalidArgumentTest2) {
    ASSERT_THROW(IsLeap(-5), std::invalid_argument);
}
TEST_F(LeapTestCase, InvalidArgumentTest1) {
    ASSERT_THROW(IsLeap(0), std::invalid_argument);
}

