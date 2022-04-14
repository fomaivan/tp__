//
// Created by akhtyamovpavel on 5/1/20.
//


#pragma once

#include <gtest/gtest.h>
#include "Functions.h"

class AddTestCase: public ::testing::Test{
 public:
    AddTestCase() = default;
};

TEST_F(AddTestCase, AddTest1) {
    ASSERT_EQ(Add(2,3), 5);
}
