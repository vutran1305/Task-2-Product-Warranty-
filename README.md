# Task-2-Product-Warranty-
Product Warranty 


Each Product if it has warranty, there will be a warranty code

This code made from 2 time ( start and stop warranty code)

Format code : PWR/date start warranty/date stop warranty

E.g: PWR/031219/030920 That mean product has warranty from 03/12/2019 to 03/09/2020

And any other format code is not valid



If the product hasn't warranty period, it will receive a 10% discount.

If the product has warranty period, it will not receive discount

If the product hasn't date of warranty, it will receive 10% discount forever


Requirements:


1. Create custom field to store the product warranty


a,product_warranty:Field text


b,Date_to:field date or date time


c,Date_from:field date or date time



-Change date also change warranty value

- Field will not be edit if not edit date


2.Create a group

Name :1. Advanced Sale

Only users in this group can see and edit field warranty involve in product form


3.Create custom field to display estimated discount total

a,Sale_order_discount_estimated: monetary with currency for now

b,Calculated discount total= the total number of discount from discount 


4.Show up warranty  on product form, product tree view

a,Put this field anywhere (convenient position in form view and 	)

B, In order line tree view, must check product must check whether the product is still under warranty, if has ,displayed it as a time interval ex: one year, 2 years, or 30 days,...


5.Create a menu filter to filter all product has warranty valid until today, and create filter to filter in product tree view


6.Create a action to mass update all selected product warranty


7,If order contain warranty show up all of them on my cart (frontend), any where

Product With Warranty: PWR/101219/101220 , PRD/150919/150920...
