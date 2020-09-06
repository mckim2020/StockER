# stockER
Machine learning stock in pursuit of happy life! 
![](https://image.shutterstock.com/image-illustration/financial-stock-market-graph-illustration-260nw-1043606782.jpg)

# 1. Data Manipulation: Normalization and Stanarization

![](https://github.com/mckim2020/Pictures/blob/master/forn_distribution.jpg)
![](https://github.com/mckim2020/Pictures/blob/master/inst_distribution.jpg)

Needless to say, data manipulation ahead of machine learning process has to be done in order to maintain our machines' precision, etc. There are two kinds of manipulations that are used nowadays due to data set's distribution property. In other words, whether or not the data set follows Gaussian distribution plays a critical role in selecting which data manpulation process we are going to use. 

If the data set follows Gaussian distribution, where it follows the rule of symmetricity via mean value of itself, "Standarztion Process" is needed. 
On the other hand, if the data set does not follow Gaussian distribution, for example, when it follows "Bell Curve" distribution, "Normalization Process" is needed.

Above two pirctures shows us a brief example of amount of buy and sell distribution of institute in Korea and foreign investors, respectively. Intuitively we can easily figure out ther exists no symmetricity in both data set and thus data Normalization Process is needed. 

# 2. Process Using CNN(Convolutional Neural Network) 

Convolutional Neural Network, also known as CNN, shows its best peroformance for tasks that requires "extraction of main information". Thus, data extraction tasks such as image detection, face discrimination neural network uses CNN. 

![Architecture of CNN](https://github.com/mckim2020/Pictures/blob/master/CNN.jpeg)

The main idea of StockER architecture building was forming a set of data into a image. In other words, any kinds of stock data(in time domain) will be given as a "Picture" to our convolutional neural network. Since we used CNN module of pixels 32 by 32, it will be divided into 4 sectors which is filled with data of  buying and selling of institutes and foreigners, respectively. 

There are two main reasons for using CNN to analyze stock data.

First, 2d convolution process of CNN(Convolutional Neural Network) can represent the relationship between buy&sell of institute and foreigners. 

![Relationship of stock](https://github.com/mckim2020/Pictures/blob/master/put.jpeg)

Second, 
