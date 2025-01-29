#bill splitter
ttl_bill=int(input('enter the total amount:'))
ttl_ppl=int(input('total no.of people:'))
tip_percentage=int(input('enter tip percentage:'))
each_should_pay=(ttl_bill+(tip_percentage/100))/ttl_ppl
print(each_should_pay)