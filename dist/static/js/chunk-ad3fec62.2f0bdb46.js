(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-ad3fec62"],{"1a23":function(t,a,n){var e,i;!function(o,s){e=s,i="function"===typeof e?e.call(a,n,a,t):e,void 0===i||(t.exports=i)}(0,(function(t,a,n){var e=function(t,a,n,e,i,o){function s(t){var a,n,e,i,o,s,r=t<0;if(t=Math.abs(t).toFixed(l.decimals),t+="",a=t.split("."),n=a[0],e=a.length>1?l.options.decimal+a[1]:"",l.options.useGrouping){for(i="",o=0,s=n.length;o<s;++o)0!==o&&o%3===0&&(i=l.options.separator+i),i=n[s-o-1]+i;n=i}return l.options.numerals.length&&(n=n.replace(/[0-9]/g,(function(t){return l.options.numerals[+t]})),e=e.replace(/[0-9]/g,(function(t){return l.options.numerals[+t]}))),(r?"-":"")+l.options.prefix+n+e+l.options.suffix}function r(t,a,n,e){return n*(1-Math.pow(2,-10*t/e))*1024/1023+a}function c(t){return"number"==typeof t&&!isNaN(t)}var l=this;if(l.version=function(){return"1.9.3"},l.options={useEasing:!0,useGrouping:!0,separator:",",decimal:".",easingFn:r,formattingFn:s,prefix:"",suffix:"",numerals:[]},o&&"object"==typeof o)for(var u in l.options)o.hasOwnProperty(u)&&null!==o[u]&&(l.options[u]=o[u]);""===l.options.separator?l.options.useGrouping=!1:l.options.separator=""+l.options.separator;for(var d=0,p=["webkit","moz","ms","o"],m=0;m<p.length&&!window.requestAnimationFrame;++m)window.requestAnimationFrame=window[p[m]+"RequestAnimationFrame"],window.cancelAnimationFrame=window[p[m]+"CancelAnimationFrame"]||window[p[m]+"CancelRequestAnimationFrame"];window.requestAnimationFrame||(window.requestAnimationFrame=function(t,a){var n=(new Date).getTime(),e=Math.max(0,16-(n-d)),i=window.setTimeout((function(){t(n+e)}),e);return d=n+e,i}),window.cancelAnimationFrame||(window.cancelAnimationFrame=function(t){clearTimeout(t)}),l.initialize=function(){return!!l.initialized||(l.error="",l.d="string"==typeof t?document.getElementById(t):t,l.d?(l.startVal=Number(a),l.endVal=Number(n),c(l.startVal)&&c(l.endVal)?(l.decimals=Math.max(0,e||0),l.dec=Math.pow(10,l.decimals),l.duration=1e3*Number(i)||2e3,l.countDown=l.startVal>l.endVal,l.frameVal=l.startVal,l.initialized=!0,!0):(l.error="[CountUp] startVal ("+a+") or endVal ("+n+") is not a number",!1)):(l.error="[CountUp] target is null or undefined",!1))},l.printValue=function(t){var a=l.options.formattingFn(t);"INPUT"===l.d.tagName?this.d.value=a:"text"===l.d.tagName||"tspan"===l.d.tagName?this.d.textContent=a:this.d.innerHTML=a},l.count=function(t){l.startTime||(l.startTime=t),l.timestamp=t;var a=t-l.startTime;l.remaining=l.duration-a,l.options.useEasing?l.countDown?l.frameVal=l.startVal-l.options.easingFn(a,0,l.startVal-l.endVal,l.duration):l.frameVal=l.options.easingFn(a,l.startVal,l.endVal-l.startVal,l.duration):l.countDown?l.frameVal=l.startVal-(l.startVal-l.endVal)*(a/l.duration):l.frameVal=l.startVal+(l.endVal-l.startVal)*(a/l.duration),l.countDown?l.frameVal=l.frameVal<l.endVal?l.endVal:l.frameVal:l.frameVal=l.frameVal>l.endVal?l.endVal:l.frameVal,l.frameVal=Math.round(l.frameVal*l.dec)/l.dec,l.printValue(l.frameVal),a<l.duration?l.rAF=requestAnimationFrame(l.count):l.callback&&l.callback()},l.start=function(t){l.initialize()&&(l.callback=t,l.rAF=requestAnimationFrame(l.count))},l.pauseResume=function(){l.paused?(l.paused=!1,delete l.startTime,l.duration=l.remaining,l.startVal=l.frameVal,requestAnimationFrame(l.count)):(l.paused=!0,cancelAnimationFrame(l.rAF))},l.reset=function(){l.paused=!1,delete l.startTime,l.initialized=!1,l.initialize()&&(cancelAnimationFrame(l.rAF),l.printValue(l.startVal))},l.update=function(t){if(l.initialize()){if(t=Number(t),!c(t))return void(l.error="[CountUp] update() - new endVal is not a number: "+t);l.error="",t!==l.frameVal&&(cancelAnimationFrame(l.rAF),l.paused=!1,delete l.startTime,l.startVal=l.frameVal,l.endVal=t,l.countDown=l.startVal>l.endVal,l.rAF=requestAnimationFrame(l.count))}},l.initialize()&&l.printValue(l.startVal)};return e}))},"2fb4":function(t,a,n){"use strict";n("f61e")},"87ee":function(t,a,n){},"92ef":function(t,a,n){},b7b4:function(t,a,n){"use strict";n.r(a);var e=function(){var t=this,a=t.$createElement,n=t._self._c||a;return n("div",{staticClass:"app-container"},[n("nx-github-corner"),t._v(" "),n("div",{staticClass:"item"},[n("h4",[t._v("数据展示")]),t._v(" "),n("nx-data-display",{attrs:{option:t.option}})],1),t._v(" "),n("div",{staticClass:"item"},[n("h4",[t._v("选项卡展示")]),t._v(" "),n("nx-data-tabs",{attrs:{option:t.easyDataOption}})],1),t._v(" "),n("div",{staticClass:"item"},[n("h4",[t._v("卡片的展示")]),t._v(" "),n("nx-data-card",{attrs:{option:t.easyDataOption0}})],1),t._v(" "),n("div",{staticClass:"item"},[n("h4",[t._v("带数字的展示")]),t._v(" "),n("nx-data-icons",{attrs:{option:t.easyDataOption1}})],1),t._v(" "),n("div",{staticClass:"item"},[n("h4",[t._v("简易展示")]),t._v(" "),n("nx-data-icons",{attrs:{option:t.easyDataOption2}})],1)],1)},i=[],o=function(){var t=this,a=t.$createElement,n=t._self._c||a;return n("div",{staticClass:"nx-data-display"},[n("el-row",{attrs:{span:24}},t._l(t.data,(function(a,e){return n("el-col",{key:e,attrs:{span:t.span}},[n("div",{staticClass:"item",style:{color:t.color}},[n("h5",{staticClass:"count"},[n("nx-count-up",{attrs:{start:14,end:a.count}})],1),t._v(" "),n("span",{staticClass:"splitLine"}),t._v(" "),n("p",{staticClass:"title"},[t._v(t._s(a.title))])])])})),1)],1)},s=[],r=function(){var t=this,a=t.$createElement,n=t._self._c||a;return n("span")},c=[],l=(n("c5f6"),n("1a23")),u=n.n(l),d={name:"nx-count-up",props:{start:{type:Number,required:!1,default:0},end:{type:Number,required:!0,default:0},decimals:{type:Number,required:!1,default:0},duration:{type:Number,required:!1,default:2},options:{type:Object,required:!1,default:function(){return{}}},callback:{type:Function,required:!1,default:function(){}}},data:function(){return{c:null}},watch:{end:function(t){this.c&&this.c.update&&this.c.update(t)}},mounted:function(){this.init()},methods:{init:function(){var t=this;this.c||(this.c=new u.a(this.$el,this.start,this.end,this.decimals,this.duration,this.options),this.c.start((function(){t.callback(t.c)})))},destroy:function(){this.c=null}},beforeDestroy:function(){this.destroy()},start:function(t){var a=this;this.c&&this.c.start&&this.c.start((function(){t&&t(a.c)}))},pauseResume:function(){this.c&&this.c.pauseResume&&this.c.pauseResume()},reset:function(){this.c&&this.c.reset&&this.c.reset()},update:function(t){this.c&&this.c.update&&this.c.update(t)}},p=d,m=n("2877"),f=Object(m["a"])(p,r,c,!1,null,null,null),h=f.exports,v={name:"nx-data-display",components:{nxCountUp:h},data:function(){return{span:this.option.span||8,data:this.option.data,color:this.option.color||"rgb(63, 161, 255)"}},props:{option:{type:Object,default:function(){}}},created:function(){},methods:{}},b=v,_=Object(m["a"])(b,o,s,!1,null,null,null),C=_.exports,g=function(){var t=this,a=t.$createElement,n=t._self._c||a;return n("div",{staticClass:"data-card"},[n("el-row",{attrs:{span:24}},t._l(t.data,(function(a,e){return n("el-col",{key:e,attrs:{span:t.span}},[n("div",{staticClass:"item"},[n("img",{staticClass:"item-img",attrs:{src:a.src}}),t._v(" "),n("div",{staticClass:"item-text",style:{color:t.colorText,backgroundColor:t.bgText}},[n("h3",[t._v(t._s(a.name))]),t._v(" "),n("p",[t._v(t._s(a.text))])])])])})),1)],1)},x=[],V={name:"nx-data-card",data:function(){return{span:this.option.span||6,data:this.option.data||[],colorText:this.option.colorText||"#fff",bgText:this.option.bgText||"#2e323f",borderColor:this.option.borderColor||"#2e323f"}},props:{option:{type:Object,default:function(){}}},created:function(){},mounted:function(){},watch:{},computed:{},methods:{}},w=V,y=Object(m["a"])(w,g,x,!1,null,"a2ff6390",null),F=y.exports,A=function(){var t=this,a=t.$createElement,n=t._self._c||a;return n("div",{staticClass:"data-tabs"},[n("el-row",{attrs:{span:24}},t._l(t.data,(function(a,e){return n("el-col",{key:e,attrs:{span:t.span}},[n("div",{staticClass:"item",style:{background:a.color}},[n("div",{staticClass:"item-header"},[n("p",[t._v(t._s(a.title))]),t._v(" "),n("span",[t._v(t._s(a.subtitle))])]),t._v(" "),n("div",{staticClass:"item-body"},[n("h2",[n("nx-count-up",{attrs:{start:14,end:a.count}})],1)]),t._v(" "),n("div",{staticClass:"item-footer"},[n("span",[t._v(t._s(a.allcount))]),t._v(" "),n("p",[t._v(t._s(a.text))])]),t._v(" "),n("p",{staticClass:"item-tip"},[t._v(t._s(a.key))])])])})),1)],1)},k=[],O={components:{nxCountUp:h},name:"nx-data-tabs",data:function(){return{span:this.option.span||6,data:this.option.data||[]}},props:{option:{type:Object,default:function(){}}}},D=O,j=Object(m["a"])(D,A,k,!1,null,"5b8c17df",null),T=j.exports,q=function(){var t=this,a=t.$createElement,n=t._self._c||a;return n("div",{staticClass:"data-icons"},[n("el-row",{attrs:{span:24}},[t._l(t.data,(function(a){return[n("el-col",{attrs:{span:t.span}},[n("div",{staticClass:"item",class:[{"item--easy":t.discount}]},[n("div",{staticClass:"item-icon",style:{color:t.color}},[n("i",{class:a.icon})]),t._v(" "),n("div",{staticClass:"item-info"},[n("span",[t._v(t._s(a.title))]),t._v(" "),n("h3",{style:{color:t.color}},[n("nx-count-up",{attrs:{start:14,end:a.count}})],1)])])])]}))],2)],1)},N=[],z={name:"nx-data-icons",components:{nxCountUp:h},data:function(){return{span:this.option.span||6,data:this.option.data,color:this.option.color||"rgb(63, 161, 255)",discount:this.option.discount||!1}},props:{option:{type:Object,default:function(){}}}},E=z,M=Object(m["a"])(E,q,N,!1,null,"2f15452a",null),L=M.exports,$=function(){var t=this,a=t.$createElement,n=t._self._c||a;return n("a",{staticClass:"github-corner",attrs:{href:"https://github.com/mgbq/nx-admin",target:"_blank","aria-label":"View source on Github"}},[n("svg",{staticStyle:{fill:"#40c9c6",color:"#fff",position:"absolute",top:"84px",border:"0",right:"0"},attrs:{width:"80",height:"80",viewBox:"0 0 250 250","aria-hidden":"true"}},[n("path",{attrs:{d:"M0,0 L115,115 L130,115 L142,142 L250,250 L250,0 Z"}}),t._v(" "),n("path",{staticClass:"octo-arm",staticStyle:{"transform-origin":"130px 106px"},attrs:{d:"M128.3,109.0 C113.8,99.7 119.0,89.6 119.0,89.6 C122.0,82.7 120.5,78.6 120.5,78.6 C119.2,72.0 123.4,76.3 123.4,76.3 C127.3,80.9 125.5,87.3 125.5,87.3 C122.9,97.6 130.6,101.9 134.4,103.2",fill:"currentColor"}}),t._v(" "),n("path",{staticClass:"octo-body",attrs:{d:"M115.0,115.0 C114.9,115.1 118.7,116.5 119.8,115.4 L133.7,101.6 C136.9,99.2 139.9,98.4 142.2,98.6 C133.8,88.0 127.5,74.4 143.8,58.0 C148.5,53.4 154.0,51.2 159.7,51.0 C160.3,49.4 163.2,43.6 171.4,40.1 C171.4,40.1 176.1,42.5 178.8,56.2 C183.1,58.6 187.2,61.8 190.9,65.4 C194.5,69.0 197.7,73.2 200.1,77.6 C213.8,80.2 216.3,84.9 216.3,84.9 C212.7,93.1 206.9,96.0 205.4,96.6 C205.1,102.4 203.0,107.8 198.3,112.5 C181.9,128.9 168.3,122.5 157.7,114.1 C157.9,116.9 156.7,120.9 152.7,124.9 L141.0,136.5 C139.8,137.7 141.6,141.9 141.8,141.8 Z",fill:"currentColor"}})])])},U=[],R=(n("2fb4"),{}),G=Object(m["a"])(R,$,U,!1,null,"070aa059",null),I=G.exports,B={name:"report",components:{nxDataDisplay:C,nxDataCard:F,nxDataTabs:T,nxDataIcons:L,nxGithubCorner:I},data:function(){return{option:{span:8,color:"#15A0FF",data:[{count:1e3,title:"日活跃数"},{count:3e3,title:"月活跃数"},{count:2e4,title:"年活跃数"}]},easyDataOption:{span:6,data:[{title:"分类统计",subtitle:"实时",count:7993,allcount:10222,text:"当前分类总记录数",color:"rgb(49, 180, 141)",key:"类"},{title:"附件统计",subtitle:"实时",count:3112,allcount:10222,text:"当前上传的附件数",color:"rgb(56, 161, 242)",key:"附"},{title:"文章统计",subtitle:"实时",count:908,allcount:10222,text:"评论次数",color:"rgb(117, 56, 199)",key:"评"},{title:"新闻统计",subtitle:"实时",count:908,allcount:10222,text:"评论次数",color:"rgb(59, 103, 164)",key:"新"}]},easyDataOption0:{span:6,borderColor:"#fff",data:[{name:"鸡你太美",src:"static/img/mock/card/card-3.jpg",text:"擅长唱,跳,rap,篮球"}]},easyDataOption1:{color:"rgb(63, 161, 255)",span:4,data:[{title:"今日注册",count:12678,icon:"icon-cuowu"},{title:"今日登录",count:22139,icon:"icon-shujuzhanshi2"},{title:"今日订阅",count:35623,icon:"icon-jiaoseguanli"},{title:"今日评论",count:16826,icon:"icon-caidanguanli"},{title:"今日评论",count:16826,icon:"icon-caidanguanli"},{title:"今日评论",count:16826,icon:"icon-caidanguanli"}]},easyDataOption2:{color:"rgb(63, 161, 255)",span:4,discount:!0,data:[{title:"错误日志",count:12678,icon:"icon-cuowu"},{title:"数据展示",count:12678,icon:"icon-shujuzhanshi2"},{title:"权限管理",count:12678,icon:"icon-jiaoseguanli"},{title:"菜单管理",count:12678,icon:"icon-caidanguanli"},{title:"权限测试",count:12678,icon:"icon-caidanguanli"},{title:"错误页面",count:12678,icon:"icon-caidanguanli"}]}}},created:function(){},watch:{},mounted:function(){},computed:{}},J=B,P=(n("e38e"),n("d68a"),Object(m["a"])(J,e,i,!1,null,"09e9a252",null));a["default"]=P.exports},d68a:function(t,a,n){"use strict";n("87ee")},e38e:function(t,a,n){"use strict";n("92ef")},f61e:function(t,a,n){}}]);