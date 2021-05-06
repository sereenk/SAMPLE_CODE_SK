---
title: "LHS 610: Week 1 HW Assignment 1"
author: "Sereen Kallerackal"
date: "27 January 2021"
output: 'R notebook'
---
# Loading necessary packages
library(tidyverse)
library(haven)
library(NHANES)
library(ggplot2)
library(dplyr)

# Reading the 2 xpt files, where data1 is the 1999-2000 demographic data and data2 is the 2015-2016 data.

data1 <- read_xpt(
  'NHANES 1999-2000 Demographics Data.xpt',
  col_select = NULL
)

data2 <- read_xpt(
  'NHANES 2015-2016 Demographics Data .xpt',
  col_select = NULL
)
# Calculating total number of participants in both data sets 

len1 <- print(length(data1$DMDHRAGE))
len2 <- print(length(data2$DMDHRAGE))

len1
len2

#Calculating summary of age within data1 

smry1 <- summary(data1$DMDHRAGE, na.rm = TRUE)
smry2 <- summary(data2$DMDHRAGE, na.rm = TRUE)

smry1
smry2

# Creating a Bar Plot of the information

#plot for 1999-2000 data
barplot(table(data1$DMDHRAGE), main = "Age distribution", xlab="Frequency")

#plot for 2015-2016 data
barplot(table(data2$DMDHRAGE), main = "Age distribution", xlab="Frequency")
