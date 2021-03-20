# javascript自执行函数

自执行函数使你的函数在定义后就立即被执行。

## 作用
1. 封装大量的工作而不会遗留下全局变量。
2. 定义的所有变量都会成为立即执行函数的局部变量
3. 隔绝作用域

## 写法

JSLint推荐写法：前后加括号
```js
(function (){//可以添加函数名
    alert(1);
},());
```

# this、apply、call、bind、箭头函数

- [面试官问：JS的this指向](https://juejin.cn/post/6844903746984476686)
- [(重点看)面试感悟,手写bind,apply,call](https://juejin.cn/post/6844903891092389901#heading-0)--箭头函数this为父作用域的this，不是调用时的this
- [JS中的箭头函数与this](https://juejin.cn/post/6844903573428371464)
- [你还没搞懂this？](https://segmentfault.com/a/1190000016680885)
- [this、apply、call、bind](https://juejin.cn/post/6844903496253177863)

手写call、apply这些也要了解下[实现call、apply、bind](https://juejin.cn/post/6874901113062031367#heading-0)