>c++一旦有变量溢出了就会报错（我不知道自己的编译器会不会，至少leetcode那边会报错）所以我们不能通过`a+b > INT_MAX?`的语句判断a、b之和会不会溢出

# 加法溢出判断

```c++
    // c = a + b;
    if(a > INT_MAX - b)return 0;
    if(a < INT_MIN - b)return 0;
```

因为加法不能直接用，既然是与INT_MAX/INT_MIN比较，那么自然想到了减法。用INT_MAX/INT_MIN减去其中一个数然后与另一个数比较就可以了。

# 乘法溢出判断

```c++
    //c = a * b;
    if(a > INT_MAX / b)return 0;//b为不为0的一方，不过如果a，b其中一个为0其实也没有判断溢出的必要了。
    if(a < INT_MIN / b)return 0;  
```

道理和加法那里是一样的。因为减法和除法绝对不会溢出。

# 加法与乘法都有的时候

```c++
    //res = a * c + b; 
    if(a > INT_MAX / c || (a == INT_MAX / c && b > INT_MAX % c))return 0;
    if(a < INT_MIN / c || (a == INT_MIN / c && b < INT_MIN % c))return 0;
```

前半部分乘法和上面的情况一样，后半部分的区别就出来了，因为时刻带着乘法，如果用法那种把`a * c`当作一个整体放一起就可能会有溢出的情况。当`a * c`的结果为一个溢出的负数时，第一个if语句就会发生`runtime error`。所以采用了这种拼凑模数的方法。一般常见的c估计都为10吧，记不住这个反正每次都当`c = 10`然后带入去想想其他地方该为多少然后推出这个公式即可（因为`c = 10`时的公式很好记嘛）

```c++
    //res = a * 10 + b;
    if(res>INT_MAX/10 || (res==INT_MAX/10 && count > 7))return 0;
    if(res<INT_MIN/10 || (res==INT_MIN/10 && count < -8))return 0;
```
