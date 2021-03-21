# javascript自执行函数

## [javascript自执行函数](https://segmentfault.com/a/1190000006813113)

自执行函数使你的函数在定义后就立即被执行。

## 作用
1. 封装大量的工作而不会遗留下全局变量。
2. 定义的所有变量都会成为立即执行函数的局部变量
3. 隔绝作用域

## 写法

JSLint推荐写法：前后加括号.后面的括号可以用来传递参数。
```js
(function (){//可以添加函数名
    alert(1);
},());
```

# this、apply、call、bind、箭头函数

## 参考博客
- [面试官问：JS的this指向](https://juejin.cn/post/6844903746984476686)
- [(重点看)面试感悟,手写bind,apply,call](https://juejin.cn/post/6844903891092389901#heading-0)--箭头函数this为父作用域的this，不是调用时的this
- [JS中的箭头函数与this](https://juejin.cn/post/6844903573428371464)
- [你还没搞懂this？](https://segmentfault.com/a/1190000016680885)
- [this、apply、call、bind](https://juejin.cn/post/6844903496253177863)

手写call、apply这些也要了解下[实现call、apply、bind](https://juejin.cn/post/6874901113062031367#heading-0)

## 常规函数中的this

>this是使用call方法调用函数时传递的第一个参数，它可以在函数调用时修改，在函数没有调用的时候，this的值是无法确定。

### 纯粹的函数调用（默认绑定）

#### 直接调用函数
```js
function test(name) {
    console.log(name)
    console.log(this)
}
test('Jerry')  //调用函数
```

上面的写法只是简写，完整写法如下

```js
function test(name) {
    console.log(name)
    console.log(this)
}
test.call(undefined, 'Tom')
```

call方法接受的第一个参数就是this，这里实际上是传入了一个undefined。

>非严格模式下，传入undefined或者null作为call的context值，那么context默认为window对象。严格模式下，context默认为undefined。

所以这题输出一个window。

### 对象中函数的调用（隐式绑定）

```js
const obj = {
    name: 'Jerry',
    greet: function() {
        console.log(this.name)
    }
}
obj.greet()  //第一种调用方法
obj.greet.call(obj) //第二种调用方法
```

这两种方式是等价的，第一种只是第二种的简写，一个语法糖。第二种调用实际上就是我们接下来要介绍的显示绑定了。

### 上面这两种调用，归根结底就是看函数前面的.是谁（被调用函数不含有其他更高优先级的情况下）

### 显示绑定call、apply、bind

关于这仨儿的介绍后面说

```js
const obj1 = {
    name: 'joy',
    getName() {
        console.log(this); 
        console.log(this.name); 
    }
};

const obj2 = {
    name: 'sam'
};

obj1.getName.call(obj2); //obj2 sam
obj1.getName.apply(obj2); //obj2 sam
const fn = obj1.getName.bind(obj2);
fn();//obj2 sam
```

这种方法主要用途就是可以自己指定this指向谁，更加的灵活方便。关于三者区别看后文。

### new绑定

this指向为new声明的对象

```js
function Vehicle() {
    this.a = 2
    console.log(this);
}
let test = new Vehicle(); //this指向Vehicle这个new出来的对象
test;//this->test
```

### 箭头函数

[JS中的箭头函数与this](https://juejin.cn/post/6844903573428371464)

箭头函数的this指向始终是自己所在作用域的沿作用域链向上的一层this。即函数所在作用域的父作用域为箭头函数的this。

```js
    var name = "windowsName";

    var a = {
        name : "Cherry",

        func1: function () {
            console.log(this.name)     
        },

        func2: function () {
            setTimeout( () => {
                this.func1()
            },100);
        }

    };

    a.func2()     // Cherry
```

#### 作用域

这里又要说一下作用域了，看这个例子

```js
const obj = {
    a: function() { console.log(this) },
    b: {
    	c: () => {console.log(this)}
	}
}
obj.a()   //没有使用箭头函数打出的是obj
obj.b.c()  //打出的是window对象！！
```

这里虽然花括号很多，但实际上箭头函数所在作用域只是obj而已。

并不是只要有花括号就产生了块级作用域。花括号形成代码块，再加上其他条件才会形成块级作用域。

修改为这样就是指向obj了：

```js
const obj = {
    a: function() { console.log(this) },
    b: function(){
    	return () => {console.log(this)}
	}
}
obj.b()()  
```

#### setTimeout setInterval的this指向

这俩的this指向在严格模式下默认为undefined，非严格模式下默认为window。

##### 改变它俩的this指向

###### 参考
[关于setInterval和setTImeout中的this指向问题](https://www.cnblogs.com/zsqos/p/6188835.html)


### 在函数内部使用_this=this

这种记录原本this的方法，应该适用于全部强制改变this指向，不受其他的影响。

#### 链接

[在函数内部使用 _this = this](https://juejin.cn/post/6844903496253177863#heading-3)

多用来改变setTimeout的值。

### 优先级

>箭头函数 -> new绑定 -> 显示绑定call/bind/apply -> 隐式绑定 -> 默认绑定

这个大部分下似乎确实是这样，所以判断的时候要看看调用的函数里面有没有其他的东西比如箭头函数影响this指向。

然后是setTimeout这俩兄弟，就默认这俩非严格模式下指向window，然后看有没有可以改变它俩this指向的条件，没有的话就是window了。（主要我测试的时候不知道怎么用new改变，然后看博客也没说new，它俩应该算是默认绑定这一个最低优先级的呀。。）

```js
var num = 0;
function Obj (){
    this.num = 1,
    this.getNum = function(){
        console.log(this.num);
    },
    this.getNumLater = function(){
        setTimeout(function(){
            console.log(this.num);
        }, 1000)
    }
}
var obj = new Obj; 
obj.getNum();//1　　打印的是obj.num，值为1
obj.getNumLater()//0　　打印的是window.num，值为0
```
这个例子似乎能说明new对setTimeout没用。

## 箭头函数

好，this说完了，再梳理一下里面涉及到的东西

### 写法

#### 只能用赋值式写法，不能用声明式写法

```js
const test = (name) => {
    console.log(name)
}
test('Jerry')
```

#### 如果参数一个，可以不加括号，如果没有参数或者多于一个，需要加括号

```js
const test = name => {
    console.log(name)
}
test('Jerry')

const test2 = (name1, name2) => {
    console.log(name1 + ' and ' + name2)
}
test2('Tom', 'Jerry')
```

#### 如果函数体只有一句话，可以不加花括号

```js
const test = name => console.log(name) 
```

#### 如果函数体没有括号，可以不写return，箭头函数会帮忙return

```js
const add = (p1, p2) => p1 + p2
add(10, 25)
```

### this指针

记住，只要存在箭头函数，this指针一定指向箭头函数所在作用域的父作用域。（用一个其他值如_this记录this值另说，上面有提到）

## bind、apply、call

这个等改天了解了手写后再来看吧