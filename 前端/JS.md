# 作用域：函数作用域、块级作用域、模块作用域

- var：

    1.存在声明提升，也就是说，只要有`var a`，那么a就会被提升至代码开始，但并没有赋值
    ![var](./img/var.png)

- let:

    即使把函数内的var变为let也会报错。因为函数内部重新声明了一次，但是在声明前就调用了，所以会报错。
    ![let](./img/let.png)

- const:
    ![const](./img/const.png)

# 隐式类型转换
- 
    ![隐式类型转换](./img/隐式类型转换.png)
    [一文看懂JS里隐式转换、toString() 和 valueOf()](https://blog.csdn.net/weixin_42752574/article/details/106065486)

# 数据类型以及类型转换

[优秀博客，包括隐式类型转换也有在讲](https://juejin.cn/post/6844903854882947080#heading-10)

先放上几篇参考文章：
- [JavaScript专题之类型判断(上)](https://github.com/mqyqingfeng/Blog/issues/28)
- [JavaScript深入之头疼的类型转换(上)](https://segmentfault.com/a/1190000022167898)
- [JavaScript 基本数据类型知识总结](https://juejin.cn/post/6866362567473381383)
- [JS 的类型转换(内有练习题)](https://juejin.cn/post/6844904095774425101#heading-0)

几个概念：
- 内部属性：
>所有 typeof 返回值为 "object" 的对象（如数组）都包含一个内部属性 [[Class]]（我 们可以把它看作一个内部的分类，而非传统的面向对象意义上的类）。这个属性无法直接访问， 一般通过 Object.prototype.toString(..) 来查看。例如：
```
Object.prototype.toString.call( [1,2,3] );  // "[object Array]" 
Object.prototype.toString.call( /regex-literal/i ); //"[object RegExp]"
```

- toString()方法：

当调用对象自身的toString方法时，若对象是Object类型，则会实际上调用prototyp。toString方法，如上所示，另外还有几条规则：

    - 数组的 toString 方法将每个数组元素转换成一个字符串，并在元素之间添加逗号后合并成结果字符串。
    - 函数的 toString 方法返回源代码字符串。
    - 日期的 toString 方法返回一个可读的日期和时间字符串。
    - RegExp 的 toString 方法返回一个表示正则表达式直接量的字符串。

- valueOf()方法：

表示对象的原始值。默认的 valueOf 方法返回这个对象本身，数组、函数、正则简单的继承了这个默认方法，也会返回对象本身。日期是一个例外，它会返回它的一个内容表示: 1970 年 1 月 1 日以来的毫秒数。
```
var date = new Date(2017, 4, 21);
console.log(date.valueOf()) // 1495296000000
```

- 原始值与引用值：

原始值存储在栈中，是简单的数据段，他们的值能够被变量直接访问到。五种原始类型的值都是原始值，包括`Boolean,Number,String,null,undefined`。当对原始值进行复制时（把一个变量复制给另一个新的变量）,实际上此时是复制的栈中的数据，并新开辟了一个新的栈，所以两个原始值是互不影响的。

引用值存储在堆中，变量实际能访问到的是一个指向堆中存储数据的地址。对象类型的值都是引用值，如`Object,Array,Date`等。当对引用值进行复制时，实际上是把自身指向实际值的指针赋值给了新的变量。所以当改变实际值时，两个变量的值都会随之改变。

- 堆栈

这里说到了堆栈，就该继续了解一下这个概念。
[直接看文章](https://www.zhihu.com/question/19729973)
![堆栈](./img/堆栈.png)

1. Boolean值的比较

基本类型的比较较为简单，略。

若是对象与String、Boolean、Number比较时，会采取隐式类型转换。先调用对象的`valueOf(),toString()`方法后，再进行比较。

![BOOL1](./img/bool比较1.png)

比如这个例子，`a==!!a`，实际上等号左边就按上述所说的隐式类型转换进行，而等号右边因为加上！！号，则会被判断为bool值，那么进行转换时，会进行Boolean方法的隐式转换。由于转换为bool类型为false值的只有`+0,-0,null,undefined,'',NaN`，其余都会是true值。

所以来看这个例子，[].valueOf().toString() --> [].toString() --> ''，而等号右边!!a-->!!Boolean([]) --> !!true --> true。此时右边是bool值，则对左边在进行一次隐式转换，即为false了。

2. Number值的比较

主要看NaN：[JavaScript中的 NaN 与 isNaN](https://www.cnblogs.com/onepixel/p/5281796.html)

一个表达式中如果有减号 (-)、乘号 (*) 或 除号 (/) 等运算符时，JS 引擎在计算之前，会试图将表达式的每个分项转化为 Number 类型（使用 Number(x) 做转换）。如果转换失败，表达式将返回 NaN 。

另外，Number（‘a’）会返回一个NaN，默认const a = 'a'则会让a是一个string类型值，但若是加上一元运算符'+'（正号，不是加号，如果是加则会隐式转换到string进行计算），那么+a会返回一个NaN，因为此时会进行Number的转换。

## 还是靠例子来理解吧，光说估计过几天就看不懂了

- 例子1：

```js
undefined == false // false。
null == false // false
```
原因是，[StackOvWhy (null == false) and (null == true) both return false?
erflow上的解释](https://stackoverflow.com/questions/27632391/why-null-false-and-null-true-both-return-false)
当 == 两边有boolean值时，会优先转为number值，其中true-->1而false-->+0。

而Number(undefined)-->NaN。Number(null)-->0.

所以 `+null == false // true`

- 例子2：
```js
[] == ![] // true
```
原因在于`!`的优先级要高于`==`。所以先对`![]`进行类型转换。因为`!`是Boolean的方法，所以我们将`[]`转换为Boolean值，即为`true`，因为要对!进行运算，就必须得是Boolean值。然后再按`==`比较。

[MDN运算符优先级](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/Operator_Precedence)
[逻辑运算符](https://zh.javascript.info/logical-operators)：这里有说，逻辑非的作用相当于
1. 将操作数转化为布尔类型：true/false。
2. 返回相反的值。
![逻辑非](./img/逻辑非.png)

而`!!`的作用其实就相当于显示转换`Boolean()`。

## ==的运算细节

找了好久，终于找到这个了，真是很有用。
- [知乎链接：为什么null == 0 返回false](https://www.zhihu.com/question/52666420)
- [ECMA中的解释](https://es6.ruanyifeng.com/?search=%E9%80%97%E5%8F%B7&x=4&y=9#docs/spec)

如下：
1. 如果x不是正常值（比如抛出一个错误），中断执行。
2. 如果y不是正常值，中断执行。
3. 如果Type(x)与Type(y)相同，执行严格相等运算x === y。
4. 如果x是null，y是undefined，返回true。
5. 如果x是undefined，y是null，返回true。
6. 如果Type(x)是数值，Type(y)是字符串，返回x == ToNumber(y)的结果。
7. 如果Type(x)是字符串，Type(y)是数值，返回ToNumber(x) == y的结果。
8. 如果Type(x)是布尔值，返回ToNumber(x) == y的结果。
9. 如果Type(y)是布尔值，返回x == ToNumber(y)的结果。
10. 如果Type(x)是字符串或数值或Symbol值，Type(y)是对象，返回x == ToPrimitive(y)的结果。
11. 如果Type(x)是对象，Type(y)是字符串或数值或Symbol值，返回ToPrimitive(x) == y的结果。
12. 返回false。



## 转数字

- Number(null)=0;
- Number(undefined)=NaN

## 转Boolean

只有`+0,-0,null,undefined,'',NaN`为false，其余都为true。



# 变量类型

[你真的掌握变量和类型了吗](https://juejin.cn/post/6844903854882947080)

## 原始类型与引用类型

### 再谈堆栈

栈空间的分配是由系统自动分配的，存储在栈中的数据占用的空间都比较小，可以直接进行操作，运行效率很高。但栈空间中的值是不可改变的。例：
```js
let a=4;
let b=4;//(由于js不能查看内存地址，我其实挺好奇a、b地址到底相不相等，看网上有说其实这种小的值都是自带一个const的，所以他们的地址是相等的)
let c=a；//c之后仍等于一个4，说明值不可变
a=5;//此时对a的值进行改变，但实际上你只是改变了a的指向，在栈中新开辟了一个空间，使它的值为5，而不是对4这个值进行改变的。虽然这个例子似乎无法说明原本a、b的地址是否相等，b此时自然能等于4，如果说地址是相等的，那就说明4这个值并没有改变。如果能看内存地址，看一下a、b地址应该很一目了然
```

堆空间的分配是人为自己指定的，存储在堆中的数据占用的空间一般都比较大，运行效率很低，不能直接进行访问，都是通过引用地址来进行读取的。在堆中存储的值大小不定，是可以动态调整的。

### 对变量的复制

原始类型和引用类型的复制是不一样的。复制原始类型时，都是在栈中新开辟空间，然后把被复制的值存储进去，再让新变量指定它。而引用类型是复制的存储在堆中的地址。这些应该都懂，也忘不了。

[js中对象的赋值、拷贝的区别](https://segmentfault.com/a/1190000021667397)

总结来说就是赋值只是把地址给新变量，新旧变量仍指向同一个堆内存。而拷贝是重新开辟了新空间，浅拷贝的基本类型是独立分开了，引用类型的内存地址还是一样的。深拷贝是全部隔离开来。

![拷贝](./img/拷贝.png)

### 比较

都是在比较栈中的值，理解这点应该就能懂
```js
let obj = {name:'heool'};
let obj2 = {name:'heool'};
console.log(obj === obj2);//false
```

### 值传递和引用传递

直接给出重点：ECMAScript中函数都是值传递！。

- 原始类型：

```js
let name = 'ConardLi';
function changeValue(name){
  name = 'code秘密花园';
}
changeValue(name);
console.log(name);//ConardLi
```
这个应该好理解，不说了。

- 引用类型：

先上例子：

```js
let obj = {};
function changeValue(obj1){
  obj1.name = 'ConardLi';
  obj1 = {name:'code秘密花园'};
}
changeValue(obj);
console.log(obj.name); // ConardLi
```

这个例子充分说了函数是值传递。引用类型的值传递，实际上传入的是地址，这个地址是指向得堆中的数据。所以我们可以通过这个地址来间接的访问堆中的数据。`obj1 = {name:'code秘密花园'};`其实相当于说，后面大括号内的内容，是新开辟了一个堆空间，然后把obj1指向这个堆，此时obj1的栈空间从原本是obj指向的地址变为了新的这个地址。相当于一个对obj1的栈中值的覆盖。而如果是引用传递，我自己的理解哈，obj1就相当于obj的别称，所以改变地址就能对obj起到效果。而值传递就是会把存储的值给覆盖掉，就像是上面“再谈堆栈”里说的那样：a的值变为了5，而c的值却没变，因为只改变了栈中的值，两个是独立分开的。

## Symbol类型

特性：
- 独一无二：通过Symbol()创建的变量，是绝不相等的。如果想创建两个相等的symbol，可以通过`Symbol.fot(key)`来创建。当参数为对象时，将调用对象的toString()方法。

```js
var sym1 = Symbol();  // Symbol() 
var sym2 = Symbol('ConardLi');  // Symbol(ConardLi)
var sym3 = Symbol('ConardLi');  // Symbol(ConardLi)
var sym4 = Symbol({name:'ConardLi'}); // Symbol([object Object])
console.log(sym2 === sym3);  // false
```

- 原始类型：typeof返回symbol

- 不可枚举：不能通过传统的方法获得其symbol属性，通过`getOwnPropertySymbols()`来获取

```js
var obj = {
  name:'ConardLi',
  [Symbol('name2')]:'code秘密花园'
}
Object.getOwnPropertyNames(obj); // ["name"]
Object.keys(obj); // ["name"]
for (var i in obj) {
   console.log(i); // name
}
Object.getOwnPropertySymbols(obj) // [Symbol(name)]
```

## Number类型

### 为什么0.1+0.2 ！== 0.3

须知，计算机中存储数据都是以二进制存储的，当对数据进行运算时，会先转换为二进制来运算，大多数小数的二进制都是无限循环的，由于存储的原因，就会出现精度缺失的问题。

JS遵循IEEE 754标准存储数据，js使用的是64位双精度浮点数编码。
![IEEE754](./img/IEEE754.png)

题外话，符号指符号位，指数位指科学计数法时，指数最大位数，尾数就是平时我们看到并使用的。

而当对数据进行舍位时，会采取1进位的办法，所以在我们存储0.1的时候，其53位恰好为1，舍去后进行进位，也即是52位由0变为1。所以计算出来的0.3和直接由0.3舍位得来的两个值是不同的。所以其实这里就是个巧合，恰好0.1进位，0.2、0.3没进位。0.2+0.6===0.8就是true。

## 其他引用类型

Array、Date、RegExp、Function自不用多说，再来看看其他的。

### 包装类型

比如Number、Boolean、String。通过如`new Number(value)`创建的类型，他们是一个引用类型，也即是Object类型。故`123 === new Number(123) //false`

>引用类型和包装类型的主要区别就是对象的生存期，使用new操作符创建的引用类型的实例，在执行流离开当前作用域之前都一直保存在内存中，而自基本类型则只存在于一行代码的执行瞬间，然后立即被销毁，这意味着我们不能在运行时为基本类型添加属性和方法。

其实上面这句话就是说栈的创建和删除都是系统自动来搞，堆要自己来弄。

### 装箱和拆箱

其实也就是自动的进行一个过程。比如我们操作基础类型时，后台自动装箱一个对象，使得我们可以像访问引用类型那样，使用其方法和属性。

有趣的面试题：如何让`a == 1 && a == 2 && a == 3`。

根据上面的拆箱转换，以及==的隐式转换，我们可以轻松写出答案：
```js
const a = {
   value:[3,2,1],
   valueOf: function () {return this.value.pop(); },
} 
```

重点在于思考过程：为了实现上面的条件，那明显基本类型Number不可能做到，那么只能是引用类型了。引用类型要与基本类型进行`==`比较，那么默认会先调用ValueOf()然后toString()。于是我们可以在这上面下文章。因为有三个值，那显然该用个数组储存，接着对每次都pop掉一个数即可了。

思考过程就是循序渐进，去逆推！

# 深拷贝

[如何写出一个惊艳面试官的深拷贝?](https://segmentfault.com/a/1190000020255831#comment-area)：我只能说一句牛逼

1. 基本的对象、数组类型递归深拷贝（✔）
2. 防止循环引用
3. 优化性能
4. 考虑更多类型


# 作用域、上下文、const、var、let

## 作用域

**作用域是一个可访问变量、函数、对象的集合，决定代码区域中变量和其他资源的可见性。作用域就是一个独立的地盘，让变量不会外泄、暴露出去。也就是说作用域最大的用处就是隔离变量，不同作用域下同名变量不会有冲突。**

我们知道var是有变量提升的效果的，但它也会被圈到它所在的上下文中而不会出去。

但是**if、while语句等不会形成作用域**：
```js
if (true) {
    // 'if' 条件语句块不会创建一个新的作用域
    var name = 'Hammad'; // name 依然在全局作用域中
}
console.log(name); // logs 'Hammad'
```

### 全局作用域、函数作用域

>ES6之前JS没有块级作用域，只有全局作用域和函数作用域。ES6新增了let和const命令来体现块级作用域。

```js
var outVariable = "我是最外层变量"; //最外层变量
function outFun() { //最外层函数
    var inVariable = "内层变量";
    function innerFun() { //内层函数
        console.log(inVariable);
    }
    innerFun();
}
console.log(outVariable); //我是最外层变量
outFun(); //内层变量
console.log(inVariable); //inVariable is not defined
innerFun(); //innerFun is not defined
```

这里有两个作用域，一个是由window创建的全局作用域，一个是function创建的函数作用域。

**全局作用域**：最外层函数

**函数作用域**：由函数生成的作用域，函数内部声明的所有变量在函数体内始终都是可见的，可以在整个函数的范围内使用及复用。

这里涉及到了var变量提升的知识点，之后再说。

### 块级作用域

**块级作用域**：作用域基础上，由花括号包含的代码块就是块级作用域。

## 作用域链

**自由变量**：如果当前作用域中没有需要使用的变量，那就沿着“父级”作用域去找那个变量，找到了它，它就是一个自由变量。也即是说当前作用域中没定义的变量就是个自由变量。（父级作用域描述不准确，看下文）

**作用域链**：如果作用域中没有变量，我们需要去查找它，这个查询的顺序就是去**创建**该作用域的地方，找包含着它的邻近的一级作用域找该变量。而不是在执行上下文的父级去找。比如这个例子：

```js
var x = 10
function fn() {
  console.log(x)
}
function show(f) {
  var x = 20
  (function() {
    f() //10，而不是20
  })()
}
show(fn)
```
去创建了fn()的那个地方找包含了fn()的最近一层作用域（这里就是全局作用域）找自由变量。

## 执行上下文

