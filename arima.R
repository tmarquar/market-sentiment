library("Quandl")

require(TSA)

myData = Quandl("NASDAQOMX/COMP",start_date="2018-10-01", end_date="2018-10-20")
View(myData)

nasdaqHigh = ts(myData[,"High"])

plot(nasdaqHigh)

acf(nasdaqHigh)
pacf(nasdaqHigh)

#BoxCox.ar(nasdaqHigh)

logHigh = log(nasdaqHigh)
plot(logHigh)

diffHigh = diff(nasdaqHigh)

plot(diffHigh)
acf(diffHigh)
pacf(diffHigh)

m1.110 = arima(nasdaqHigh, order = c(1,1,0))
tsdiag(m1.110)

require(forecast)

auto.arima(nasdaqHigh,stepwise=F,trace=T,ic="bic") 
